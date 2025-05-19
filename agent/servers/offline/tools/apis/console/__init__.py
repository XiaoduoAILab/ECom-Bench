from rich.console import Console
class ConsoleLogger:
    def __init__(self):
        self.console = Console()
        self.verbose = False  # 默认不启用日志
        
    def reset(self, verbose):
        self.verbose = verbose
    
    def print(self, *args):
        self.console.print(*args)
        
    def log(self, *args):
        if self.verbose:
            self.console.log(*args)
        else:
            # 如果没有启用日志，什么都不做
            pass
        
console_model = ConsoleLogger()
console_model.reset(False)  # 设置为不启用日志