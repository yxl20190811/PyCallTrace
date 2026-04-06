"""
日志格式配置和主程序入口
设置loguru日志格式，调用function_calls模块中的函数
不包含具体业务代码，仅负责日志格式配置和程序入口
"""

import sys
import os
from loguru import logger
import threading


# 配置日志格式
fmt = (
    "<cyan>tid:{thread.id}</cyan>|<green>{file.path}:{line}</green>|<level>{message}</level>"
)

# 移除默认处理器，添加自定义格式
logger.remove()
logger.add(
    sink=sys.stdout,
    level="DEBUG",
    format=fmt,
    colorize=True,
)

# 导入业务函数模块
from function_calls import main as function_calls_main


# 追踪器全局状态
_trace_depth = 0
_in_logging = False  # 防止日志递归死锁


def _should_trace(func_name, filename):
    """判断是否应该追踪该函数"""
    # 过滤内部函数
    if func_name.startswith('<') or filename.startswith('<'):
        return False
    # 过滤标准库和第三方库
    if 'site-packages' in filename or 'dist-packages' in filename:
        return False
    # 过滤 Python 标准库
    if 'Lib\\' in filename or '/lib/' in filename.lower():
        return False
    # 过滤 loguru 内部调用
    if 'loguru' in filename.lower():
        return False
    return True


def global_tracer(frame, event, arg):
    """
    全局函数追踪器 - 处理所有事件类型
    
    事件类型:
    - 'call': 函数被调用
    - 'return': 函数正常返回
    - 'exception': 函数抛出异常
    - 'c_call': C 扩展函数被调用
    - 'c_return': C 扩展函数返回
    - 'c_exception': C 扩展函数抛出异常
    """
    global _trace_depth, _in_logging
    
    func_name = frame.f_code.co_name
    filename = frame.f_code.co_filename
    line_no = frame.f_lineno
    
    # 判断是否应该追踪
    if not _should_trace(func_name, filename):
        return global_tracer
    
    # 防止日志递归死锁
    if _in_logging:
        return global_tracer
    
    try:
        _in_logging = True
        
        if event == 'call':
            print(f"tid:{threading.current_thread().ident}|enter fun:{func_name}@{filename}:{line_no}")
            
        elif event == 'return':
            print(f"tid:{threading.current_thread().ident}|exit fun:{func_name}@{filename}:{line_no}")

            
        elif event == 'exception':
            exc_type, exc_value, exc_tb = arg
            print(f"tid:{threading.current_thread().ident}|exception fun:{func_name}@{filename}:{line_no}")
        elif event == 'c_call':
            # C 扩展函数调用（通常不需要追踪）
            pass
            
        elif event == 'c_return':
            # C 扩展函数返回（通常不需要追踪）
            pass
            
        elif event == 'c_exception':
            # C 扩展函数异常
            #print(f"exception cfun: {func_name}")
            pass
            
    finally:
        _in_logging = False
    
    return global_tracer


sys.setprofile(global_tracer)

if __name__ == "__main__":
    function_calls_main()
sys.setprofile(None)
