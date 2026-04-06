"""
函数调用模块
包含所有业务函数，互相调用，并打印日志
不关心日志格式，只关注业务逻辑
"""

import random
from loguru import logger

# 调用深度计数器
call_depth = 0
MAX_DEPTH = 20


def should_return():
    """判断是否应该返回(达到最大深度)"""
    return call_depth >= MAX_DEPTH


def func_a():
    """函数A - 可能调用func_b或func_c"""
    global call_depth
    call_depth += 1

    if should_return():
        logger.debug("  达到最大深度,返回")
        call_depth -= 1
        return

    choice = random.choice(['b', 'c', 'd'])
    if choice == 'b':
        func_b()
    elif choice == 'c':
        func_c()
    else:
        func_d()

    call_depth -= 1


def func_b():
    """函数B - 可能调用func_a或func_e或func_f"""
    global call_depth
    call_depth += 1

    if should_return():
        logger.debug("  达到最大深度,返回")
        call_depth -= 1
        return

    choice = random.choice(['a', 'e', 'f'])
    if choice == 'a':
        func_a()
    elif choice == 'e':
        func_e()
    else:
        func_f()

    call_depth -= 1


def func_c():
    """函数C - 可能调用func_d或func_g或func_h"""
    global call_depth
    call_depth += 1

    if should_return():
        logger.debug("  达到最大深度,返回")
        call_depth -= 1
        return

    choice = random.choice(['d', 'g', 'h'])
    if choice == 'd':
        func_d()
    elif choice == 'g':
        func_g()
    else:
        func_h()

    call_depth -= 1


def func_d():
    """函数D - 可能调用func_a或func_e或func_i"""
    global call_depth
    call_depth += 1

    if should_return():
        logger.debug("  达到最大深度,返回")
        call_depth -= 1
        return

    choice = random.choice(['a', 'e', 'i'])
    if choice == 'a':
        func_a()
    elif choice == 'e':
        func_e()
    else:
        func_i()

    call_depth -= 1


def func_e():
    """函数E - 可能调用func_b或func_f或func_j"""
    global call_depth
    call_depth += 1

    if should_return():
        logger.debug("  达到最大深度,返回")
        call_depth -= 1
        return

    choice = random.choice(['b', 'f', 'j'])
    if choice == 'b':
        func_b()
    elif choice == 'f':
        func_f()
    else:
        func_j()

    call_depth -= 1


def func_f():
    """函数F - 可能调用func_c或func_g或func_k"""
    global call_depth
    call_depth += 1

    if should_return():
        logger.debug("  达到最大深度,返回")
        call_depth -= 1
        return

    choice = random.choice(['c', 'g', 'k'])
    if choice == 'c':
        func_c()
    elif choice == 'g':
        func_g()
    else:
        func_k()

    call_depth -= 1


def func_g():
    """函数G - 可能调用func_a或func_d或func_l"""
    global call_depth
    call_depth += 1

    if should_return():
        logger.debug("  达到最大深度,返回")
        call_depth -= 1
        return

    choice = random.choice(['a', 'd', 'l'])
    if choice == 'a':
        func_a()
    elif choice == 'd':
        func_d()
    else:
        func_l()

    call_depth -= 1


def func_h():
    """函数H - 可能调用func_b或func_e或func_m"""
    global call_depth
    call_depth += 1

    if should_return():
        logger.debug("  达到最大深度,返回")
        call_depth -= 1
        return

    choice = random.choice(['b', 'e', 'm'])
    if choice == 'b':
        func_b()
    elif choice == 'e':
        func_e()
    else:
        func_m()

    call_depth -= 1


def func_i():
    """函数I - 可能调用func_c或func_f或func_n"""
    global call_depth
    call_depth += 1

    if should_return():
        logger.debug("  达到最大深度,返回")
        call_depth -= 1
        return

    choice = random.choice(['c', 'f', 'n'])
    if choice == 'c':
        func_c()
    elif choice == 'f':
        func_f()
    else:
        func_n()

    call_depth -= 1


def func_j():
    """函数J - 可能调用func_d或func_g或func_o"""
    global call_depth
    call_depth += 1

    if should_return():
        logger.debug("  达到最大深度,返回")
        call_depth -= 1
        return

    choice = random.choice(['d', 'g', 'o'])
    if choice == 'd':
        func_d()
    elif choice == 'g':
        func_g()
    else:
        func_o()

    call_depth -= 1


def func_k():
    """函数K - 可能调用func_a或func_h或func_p"""
    global call_depth
    call_depth += 1

    if should_return():
        logger.debug("  达到最大深度,返回")
        call_depth -= 1
        return

    choice = random.choice(['a', 'h', 'p'])
    if choice == 'a':
        func_a()
    elif choice == 'h':
        func_h()
    else:
        func_p()

    call_depth -= 1


def func_l():
    """函数L - 可能调用func_b或func_i或func_q"""
    global call_depth
    call_depth += 1

    if should_return():
        logger.debug("  达到最大深度,返回")
        call_depth -= 1
        return

    choice = random.choice(['b', 'i', 'q'])
    if choice == 'b':
        func_b()
    elif choice == 'i':
        func_i()
    else:
        func_q()

    call_depth -= 1


def func_m():
    """函数M - 可能调用func_c或func_j或func_r"""
    global call_depth
    call_depth += 1

    if should_return():
        logger.debug("  达到最大深度,返回")
        call_depth -= 1
        return

    choice = random.choice(['c', 'j', 'r'])
    if choice == 'c':
        func_c()
    elif choice == 'j':
        func_j()
    else:
        func_r()

    call_depth -= 1


def func_n():
    """函数N - 可能调用func_d或func_k或func_s"""
    global call_depth
    call_depth += 1

    if should_return():
        logger.debug("  达到最大深度,返回")
        call_depth -= 1
        return

    choice = random.choice(['d', 'k', 's'])
    if choice == 'd':
        func_d()
    elif choice == 'k':
        func_k()
    else:
        func_s()

    call_depth -= 1


def func_o():
    """函数O - 可能调用func_e或func_l或func_t"""
    global call_depth
    call_depth += 1

    if should_return():
        logger.debug("  达到最大深度,返回")
        call_depth -= 1
        return

    choice = random.choice(['e', 'l', 't'])
    if choice == 'e':
        func_e()
    elif choice == 'l':
        func_l()
    else:
        func_t()

    call_depth -= 1


def func_p():
    """函数P - 可能调用func_f或func_m或func_a"""
    global call_depth
    call_depth += 1

    if should_return():
        logger.debug("  达到最大深度,返回")
        call_depth -= 1
        return

    choice = random.choice(['f', 'm', 'a'])
    if choice == 'f':
        func_f()
    elif choice == 'm':
        func_m()
    else:
        func_a()

    call_depth -= 1


def func_q():
    """函数Q - 可能调用func_g或func_n或func_b"""
    global call_depth
    call_depth += 1

    if should_return():
        logger.debug("  达到最大深度,返回")
        call_depth -= 1
        return

    choice = random.choice(['g', 'n', 'b'])
    if choice == 'g':
        func_g()
    elif choice == 'n':
        func_n()
    else:
        func_b()

    call_depth -= 1


def func_r():
    """函数R - 可能调用func_h或func_o或func_c"""
    global call_depth
    call_depth += 1

    if should_return():
        logger.debug("  达到最大深度,返回")
        call_depth -= 1
        return

    choice = random.choice(['h', 'o', 'c'])
    if choice == 'h':
        func_h()
    elif choice == 'o':
        func_o()
    else:
        func_c()

    call_depth -= 1


def func_s():
    """函数S - 可能调用func_i或func_p或func_d"""
    global call_depth
    call_depth += 1

    if should_return():
        logger.debug("  达到最大深度,返回")
        call_depth -= 1
        return

    choice = random.choice(['i', 'p', 'd'])
    if choice == 'i':
        func_i()
    elif choice == 'p':
        func_p()
    else:
        func_d()

    call_depth -= 1


def func_t():
    """函数T - 可能调用func_j或func_q或func_e"""
    global call_depth
    call_depth += 1

    if should_return():
        logger.debug("  达到最大深度,返回")
        call_depth -= 1
        return

    choice = random.choice(['j', 'q', 'e'])
    if choice == 'j':
        func_j()
    elif choice == 'q':
        func_q()
    else:
        func_e()

    call_depth -= 1


def main():
    """主函数 - 随机调用其他函数"""
    logger.debug("=" * 80)
    logger.debug("程序开始执行 - 使用loguru日志库")
    logger.debug("=" * 80)

    # 主函数随机选择一个函数开始调用
    functions = [
        func_a, func_b, func_c, func_d, func_e,
        func_f, func_g, func_h, func_i, func_j,
        func_k, func_l, func_m, func_n, func_o,
        func_p, func_q, func_r, func_s, func_t
    ]

    # 随机选择一个函数开始
    start_func = random.choice(functions)
    logger.debug(f"随机选择起始函数: {start_func.__name__}")

    # 调用起始函数
    start_func()

    # 随机选择一个函数开始
    start_func = random.choice(functions)
    logger.debug(f"随机选择起始函数: {start_func.__name__}")

        # 调用起始函数
    start_func()

    # 随机选择一个函数开始
    start_func = random.choice(functions)
    logger.debug(f"随机选择起始函数: {start_func.__name__}")


    # 调用起始函数
    start_func()

    logger.debug("=" * 80)
    logger.debug("程序执行完毕")
    logger.debug("=" * 80)


if __name__ == "__main__":
    # 设置随机种子(可选,用于复现结果)
    # random.seed(42)

    main()
