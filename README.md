# LangChain 学习项目

基于 **LangChain 1.x** 的入门学习项目，通过 Jupyter Notebook 记录大模型（LLM）调用、流式输出、批量处理等核心用法的实践笔记。

## 目录结构

| 目录 / 文件 | 内容 |
|---|---|
| `chapter langsmith/` | LangSmith 追踪实践：结合 DeepSeek / Ollama 的模型调用与链路追踪 |
| `chapter01/` | 基础练习（输入输出示例与 Python 脚本） |
| `chapter02/` | 模型调用进阶：批量处理（batch）、流式输出（stream）、模型调用与优化（model invoke / o1-model-init-online）、多模型接入（profile：DeepSeek、OpenAI 兼容接口、通义千问、智谱） |
| `chapter04/` | Git / GitHub 学习笔记 |
| `main.py` | PyCharm 示例脚本 |
| `requirements_full.txt` | 项目依赖清单（LangChain 1.x、Jupyter、Ollama 等） |

## 环境准备

- Python 3.9+
- 安装依赖：

```bash
pip install -r requirements_full.txt
```

- 在项目根目录创建 `.env` 文件，填入你的 API Key（示例）：

```
DEEPSEEK_API_KEY=your_api_key_here
```

> `.env` 已被 `.gitignore` 忽略，不会提交到仓库，请注意保管密钥。

## 快速开始

在 JupyterLab 中打开对应章节的 `.ipynb` 文件，按顺序运行单元格即可：

- 调用在线模型（DeepSeek / 通义千问 / 智谱等）前，先确认 `.env` 中的 API Key 已正确配置；
- 使用本地模型（如 Ollama）需先启动本地服务（`ollama serve`）。

## 说明

- 本仓库主要用于个人学习记录与代码备份；
- 各 notebook 中的模型调用方式以实际代码为准，涉及多家模型服务商，请遵守各服务商的使用条款。
