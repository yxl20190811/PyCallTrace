# PyCallTrace - Python 函数调用追踪与分析工具

## 项目概述

这是一个 Python 函数调用追踪与日志分析工具，用于实时监控和可视化展示 Python 程序的函数调用链路。项目包含三个核心组件：

1. **追踪器（main.py）** - 基于 `sys.setprofile()` 实现全局函数调用钩子，自动拦截所有函数的调用/返回/异常事件
2. **业务函数模块（function_calls.py）** - 包含 20 个互相调用的函数（func_a ~ func_t），用于生成随机调用链日志
3. **日志分析器（log_analyzer.html）** - 纯前端可视化工具，支持按线程分组、树状展示调用关系、映射源代码查看

## 技术栈

- **Python 3** - 运行追踪器主程序
- **loguru** - 日志库，用于输出格式化日志
- **HTML/CSS/JavaScript** - 前端日志分析工具（无依赖）

## 项目结构

```
PyCallTrace/
├── main.py              # 追踪器入口：配置日志格式 + sys.setprofile 全局钩子
├── function_calls.py    # 业务函数模块：20 个函数互相调用，生成随机调用链
├── log_analyzer.html    # 日志分析工具：浏览器端可视化日志
├── 1.log                # 示例日志文件（由 main.py 生成）
└── QWEN.md              # 项目说明文档
```

## 运行方式

### 1. 安装依赖

```bash
pip install loguru
```

### 2. 运行追踪器生成日志

```bash
python main.py
```

程序将自动输出追踪日志到控制台，格式为：

```
tid:{线程ID}|enter fun:{函数名}@{文件路径}:{行号}
tid:{线程ID}|exit fun:{函数名}@{文件路径}:{行号}
```

### 3. 使用分析器查看日志

在浏览器中打开 `log_analyzer.html`，然后：

- 点击 **📂 打开日志文件** 选择 `.log` 文件
- 左侧显示按线程 ID 分组的列表
- 点击线程查看树状调用链
- 点击 **📁 映射目录** 选择包含 `.py` 文件的目录，可查看调用栈对应的源代码

## 日志格式

| 类型 | 示例 |
|------|------|
| 函数进入 | `tid:20816\|enter fun:func_t@C:\hh\svn\PyCallTrace\function_calls.py:419` |
| 函数返回 | `tid:20816\|exit fun:should_return@C:\hh\svn\PyCallTrace\function_calls.py:17` |
| 函数异常 | `tid:20816\|exception fun:{函数名}@{文件路径}:{行号}` |
| 普通日志 | `tid:20816\|程序开始执行 - 使用loguru日志库` |

## 核心设计

### 追踪器（main.py）

- 使用 `sys.setprofile(global_tracer)` 设置全局性能分析钩子
- `global_tracer` 函数拦截 `call`、`return`、`exception` 等事件
- 通过 `_should_trace()` 过滤标准库、第三方库和 loguru 内部调用
- 使用 `_in_logging` 标志防止日志递归死锁

### 业务函数（function_calls.py）

- 20 个函数（func_a ~ func_t），每个函数随机选择其他函数调用
- 使用 `call_depth` 全局变量控制最大调用深度（默认 20），防止无限递归
- `main()` 函数随机选择 3 次起始函数进行调用

### 日志分析器（log_analyzer.html）

- 纯前端实现，无需服务器
- 支持按线程分组显示
- 树状调用链可视化，可展开/折叠
- 源代码映射查看（通过读取本地 `.py` 文件）
- LRU 缓存机制，最多缓存 50 个文件

## 开发约定

- 代码使用中文注释
- 日志格式统一使用 `tid:{线程ID}|{事件类型} fun:{函数名}@{文件路径}:{行号}` 模式
- 函数命名：业务函数使用 `func_{字母}` 格式
- 调用深度保护：所有业务函数都检查 `should_return()` 防止栈溢出
