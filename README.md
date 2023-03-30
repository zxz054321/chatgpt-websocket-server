# ChatGPT WebSocket 服务端

ChatGPT 是一个基于大型语言模型的自然语言处理平台，旨在为用户提供强大的自然语言处理和自然语言生成功能。本服务端实现了 ChatGPT 官网的对话和流式传输体验，同时也可以作为 [ChatGPT 微信小程序](https://github.com/zxz054321/chatgpt-miniprogram) 的服务端使用。该平台能够基于用户输入的文本生成自然、流畅的对话，并为用户提供个性化、定制化的语言处理服务。

本文档由 ChatGPT 生成和润色。

## 主要特点

- 基于官方 GPT-3.5 API，提供强大的语言生成和对话功能
- 使用 WebSocket 实现高效的流式传输，提升通信效率
- 实现了密钥池功能，提高请求并发量
- 可以部署到腾讯云函数上运行
- 支持自托管（self-hosting）

## 构建说明

本服务端使用 Python 语言编写，采用 **[websockets](https://github.com/aaugustin/websockets)** 实现 WebSocket 服务器。该库是一个在 Python 中构建 WebSocket 服务器和客户端的库，通过使用它，可以快速轻松地构建 WebSocket 服务器。

### 下载和安装

以下是具体的步骤：

1. 克隆本项目到本地：在终端或命令提示符中输入 `https://github.com/zxz054321/chatgpt-websocket-server`
2. 创建并激活 venv（推荐）：在终端或命令提示符中输入以下命令，创建并激活 venv

- Windows: 
```bash
python -m venv venv
venv\Scripts\activate.bat
```
- Linux/Mac:
```bash
python3 -m venv venv
source venv/bin/activate
```

3. 运行 `pip install -r requirements.txt` 命令安装所需的依赖项
4. 运行 `python app.py` 启动服务

### 配置

在开始使用之前，请在项目根目录新建一个 `pool.txt` 文件，用于配置 OpenAI API 密钥。你可以登录 OpenAI 官网，创建自己的 API 密钥。然后将密钥添加到 `pool.txt` 文件中，每行一个密钥，依次排列。例如：

```
API Key 1
API Key 2
API Key 3
```

请注意，每个 API 密钥都有每分钟请求次数限制，超过限制会导致请求失败。因此，在配置 `pool.txt` 时，建议至少添加两个密钥，以确保服务的稳定性。

## 注意事项

- 使用须遵循相应的法律法规，并承担相应的法律责任

## 演示

- 在微信中搜索 `GPro` 小程序
- 扫描下方的小程序码体验

![download](https://user-images.githubusercontent.com/7540550/228626291-65ccbbb7-ee74-497b-b73d-628fabe876a5.jpg)
