# PyCallTrace - Python 函数调用追踪与分析工具

[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

一个轻量级的 Python 函数调用追踪与日志分析工具，用于实时监控和可视化展示 Python 程序的函数调用链路。帮助你理解程序的执行流程、函数调用关系和代码逻辑。

## ✨ 特性

- 🔍 **实时追踪** - 基于 `sys.setprofile()` 全局钩子，自动拦截所有函数的调用/返回/异常事件
- 📊 **可视化分析** - 纯前端日志分析工具，支持树状展示调用关系
- 🧵 **线程支持** - 按线程 ID 分组显示，支持多线程程序的调用链分析
- 📁 **源码映射** - 点击调用栈即可查看对应的源代码位置
- 🎯 **零侵入** - 无需修改业务代码，直接挂载追踪器
- 🔧 **灵活过滤** - 自动过滤标准库、第三方库和日志库内部调用

## 📦 安装

### 前置要求

- Python 3.6 或更高版本
- 现代浏览器（Chrome、Firefox、Edge 等）

### 安装依赖

```bash
pip install loguru
```

## 🚀 快速开始

### 1. 运行追踪器生成日志

```bash
python main.py
```

程序将自动输出追踪日志到控制台，并将日志重定向到 `1.log` 文件。

### 2. 查看日志分析器

**方式一：直接打开**

在浏览器中直接打开 `log_analyzer.html` 文件

**方式二：使用本地服务器（推荐）**

```bash
python -m http.server 8080
```

然后访问 `http://localhost:8080/log_analyzer.html`

### 3. 使用分析器

1. 点击 **📂 打开日志文件** 选择 `.log` 文件
2. 左侧显示按线程 ID 分组的列表
3. 点击线程查看树状调用链
4. 点击 **📁 映射目录** 选择包含 `.py` 文件的目录，可查看调用栈对应的源代码

## 📁 项目结构

```
PyCallTrace/
├── main.py              # 追踪器入口：配置日志格式 + sys.setprofile 全局钩子
├── function_calls.py    # 示例业务函数模块：20 个函数互相调用，生成随机调用链
├── log_analyzer.html    # 日志分析工具：浏览器端可视化日志（纯前端，无依赖）
├── 1.log                # 示例日志文件（由 main.py 生成）
├── README.md            # 项目说明文档（本文件）
└── QWEN.md              # 详细项目文档
```

## 📝 日志格式

追踪器输出的日志格式如下：

```
tid:{线程ID}|{事件类型} fun:{函数名}@{文件路径}:{行号}
```

### 事件类型

| 类型 | 说明 | 示例 |
|------|------|------|
| `enter` | 函数被调用 | `tid:12345|enter fun:func_a@/path/to/file.py:10` |
| `exit` | 函数正常返回 | `tid:12345|exit fun:func_a@/path/to/file.py:10` |
| `exception` | 函数抛出异常 | `tid:12345|exception fun:func_a@/path/to/file.py:10` |

## 🔧 使用方法

### 追踪自己的项目

将 `main.py` 中的追踪器代码集成到你的项目中：

```python
import sys
import threading

# 复制 main.py 中的 global_tracer 和 _should_trace 函数

# 启用追踪
sys.setprofile(global_tracer)

# 运行你的代码
your_main_function()

# 关闭追踪
sys.setprofile(None)
```

### 自定义过滤规则

修改 `_should_trace()` 函数来自定义需要追踪的函数：

```python
def _should_trace(func_name, filename):
    # 添加你的过滤逻辑
    if 'your_module' not in filename:
        return False
    return True
```

### 调整调用深度

在 `function_calls.py` 中修改 `MAX_DEPTH` 变量：

```python
MAX_DEPTH = 50  # 默认 20
```

## 🏗️ 架构设计

### 追踪器（main.py）

- 使用 `sys.setprofile(global_tracer)` 设置全局性能分析钩子
- `global_tracer` 函数拦截 `call`、`return`、`exception` 等事件
- 通过 `_should_trace()` 过滤标准库、第三方库和 loguru 内部调用
- 使用 `_in_logging` 标志防止日志递归死锁

### 示例业务函数（function_calls.py）

- 20 个函数（func_a ~ func_t），每个函数随机选择其他函数调用
- 使用 `call_depth` 全局变量控制最大调用深度，防止无限递归
- `main()` 函数随机选择 3 次起始函数进行调用

### 日志分析器（log_analyzer.html）

- 纯前端实现，无需服务器
- 支持按线程分组显示
- 树状调用链可视化，可展开/折叠
- 源代码映射查看（通过读取本地 `.py` 文件）
- LRU 缓存机制，最多缓存 50 个文件

## 📊 示例输出

```
================================================================================
程序开始执行 - 使用loguru日志库
================================================================================
随机选择起始函数: func_m
tid:12345|enter fun:func_m@C:\hh\git\PyCallTrace\function_calls.py:217
tid:12345|enter fun:func_c@C:\hh\git\PyCallTrace\function_calls.py:58
tid:12345|enter fun:func_h@C:\hh\git\PyCallTrace\function_calls.py:135
tid:12345|exit fun:func_h@C:\hh\git\PyCallTrace\function_calls.py:135
tid:12345|exit fun:func_c@C:\hh\git\PyCallTrace\function_calls.py:58
tid:12345|exit fun:func_m@C:\hh\git\PyCallTrace\function_calls.py:217
...
================================================================================
程序执行完毕
================================================================================
```

## ❓ 常见问题

### Q: 为什么日志中没有看到某些函数的调用？

A: `_should_trace()` 函数会自动过滤标准库、第三方库和 loguru 内部调用。如果需要追踪这些函数，请修改过滤规则。

### Q: 追踪器会影响程序性能吗？

A: 会有一定性能开销，因为每个函数调用都会触发日志记录。对于生产环境，建议仅在调试时启用。

### Q: 如何复现相同的调用链？

A: 在 `function_calls.py` 的 `main()` 函数中设置随机种子：

```python
random.seed(42)  # 使用固定种子复现结果
```

### Q: 支持异步函数吗？

A: 当前版本支持多线程，但对 `async/await` 异步函数的支持有限。欢迎提交 PR 改进。

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

1. Fork 本仓库
2. 创建你的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交你的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启一个 Pull Request

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情

## 📧 联系方式

如有问题或建议，请提交 Issue 或联系项目维护者。

## 🙏 致谢

- [loguru](https://github.com/Delgan/loguru) - 优秀的 Python 日志库
- Python `sys.setprofile()` - 内置性能分析钩子
