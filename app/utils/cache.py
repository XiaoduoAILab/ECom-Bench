import os
import json
import time
import fcntl
import hashlib
import threading
from typing import Any, Optional

from .config import get_config

# 线程锁，用于内存级别的缓存防并发问题
_cache_locks = {}
_global_lock = threading.Lock()

def get_md5(**params) -> str:
    """
    计算参数的MD5哈希值，用作缓存键
    """
    sorted_values = [str(params[key]) for key in sorted(params.keys())]
    text = "_".join(sorted_values)
    return hashlib.md5(text.encode()).hexdigest()

def get_cache_path(cache_name: str) -> str:
    """
    获取缓存文件路径
    """
    config = get_config()
    cache_dir = config["data"]["directory"]
    return os.path.join(cache_dir, f"{cache_name}.json")

def get_cache_lock(cache_name: str) -> threading.Lock:
    """
    获取指定缓存文件的线程锁对象
    """
    global _cache_locks, _global_lock
    
    with _global_lock:
        if cache_name not in _cache_locks:
            _cache_locks[cache_name] = threading.Lock()
        return _cache_locks[cache_name]

def read_cache(cache_name: str, cache_key: str) -> Optional[Any]:
    """
    从缓存中读取数据
    
    Args:
        cache_name: 缓存名称，对应文件名
        cache_key: 缓存键值
        
    Returns:
        缓存的数据，如果不存在则返回None
    """
    config = get_config()
    if not config["data"]["cache"]:
        return None
        
    cache_path = get_cache_path(cache_name)
    
    # 如果缓存文件不存在，返回None
    if not os.path.exists(cache_path):
        return None
    
    # 获取文件锁进行读取
    with get_cache_lock(cache_name):
        try:
            with open(cache_path, 'r') as f:
                # 获取文件级别的共享锁（读锁）
                fcntl.flock(f, fcntl.LOCK_SH)
                try:
                    data = json.load(f)
                    return data.get(cache_key)
                finally:
                    # 释放锁
                    fcntl.flock(f, fcntl.LOCK_UN)
        except (json.JSONDecodeError, FileNotFoundError):
            # 文件损坏或不存在，返回None
            return None

def write_cache(cache_name: str, cache_key: str, data: Any) -> bool:
    """
    将数据写入缓存
    
    Args:
        cache_name: 缓存名称，对应文件名
        cache_key: 缓存键值
        data: 要缓存的数据
        
    Returns:
        是否成功写入缓存
    """
    config = get_config()
    if not config["data"]["save"]:
        return False
        
    cache_path = get_cache_path(cache_name)
    lock_timeout = config["data"]["lock_timeout"]
    
    # 获取线程锁
    with get_cache_lock(cache_name):
        # 读取现有缓存
        cache_data = {}
        if os.path.exists(cache_path):
            try:
                with open(cache_path, 'r') as f:
                    # 获取独占锁（写锁），设置超时避免死锁
                    start_time = time.time()
                    while True:
                        try:
                            fcntl.flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
                            break
                        except BlockingIOError:
                            # 锁被占用，等待一小段时间后重试
                            if time.time() - start_time > lock_timeout:
                                # 超时失败
                                return False
                            time.sleep(0.1)
                    
                    try:
                        cache_data = json.load(f)
                    except json.JSONDecodeError:
                        # 文件可能损坏，使用空字典
                        cache_data = {}
                    finally:
                        fcntl.flock(f, fcntl.LOCK_UN)
            except FileNotFoundError:
                # 文件不存在，使用空字典
                cache_data = {}
        
        # 更新缓存数据
        cache_data[cache_key] = data
        
        # 写入缓存文件
        try:
            with open(cache_path, 'w') as f:
                # 获取独占锁（写锁）
                start_time = time.time()
                while True:
                    try:
                        fcntl.flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
                        break
                    except BlockingIOError:
                        if time.time() - start_time > lock_timeout:
                            return False
                        time.sleep(0.1)
                
                try:
                    json.dump(cache_data, f, ensure_ascii=False, indent=2)
                    return True
                finally:
                    fcntl.flock(f, fcntl.LOCK_UN)
        except Exception:
            return False