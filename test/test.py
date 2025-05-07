import threading

# 获取所有活跃线程
for thread in threading.enumerate():
    print(f"线程名称: {thread.name}, 线程ID: {thread.ident}, 是否存活: {thread.is_alive()}")