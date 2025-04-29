<div align="center">
    <img alt="vision_agent" height="200px" src="https://hellomiku.com/img/logo.png"> 
      
# MIKU Search MCP Server
中文 | [**English**](https://github.com/GobinFan/Miku_Spider/blob/main/README_EN.md)

</div>

## 关于MIKU 

AI MIKU 是一个基于多智能体（Multiagent）技术的创新型 AI 搜索引擎，致力于为用户提供准确、个性化和实时的搜索体验。Miku MCP Server 作为 MIKU 生态系统的核心服务组件，负责智能搜索请求的处理与分发，支持多语言和多种搜索模式，便于开发者集成和扩展。  
了解更多关于 MIKU 的信息，请访问：[hellomiku.com](https://hellomiku.com)

## 主要功能

- 基于 AI 的智能搜索服务，支持多语言（简体中文、繁体中文、英文、日文、韩文、俄文、阿拉伯文）。
- 支持简单搜索（simple_search）和深度搜索（deep_search）两种模式，满足不同场景需求。
- 通过 API KEY 鉴权，保障数据安全。

---

## 返回示例

```json
{
  "conversation_id": "7825bca7-370f-4eea-98cd-bfc76b9db742",
  "code": 200,
  "source": [
    {
      "title": "【1】Miku, 快速精准的AI搜索引擎, 搜索结果自动生成大纲脑图",
      "snippet": "Miku是一款快速精准的AI搜索引擎，搜索结果可自动总结，生成大纲，也可生成脑图。我们打开Miku官网，可以用手机号码验证登录。登录成功后可以直接进行提问，我们选择深度提问，先来问问知道我们在做的自媒体账号吧！直接检索到自媒体账号，并做出了总结，但是并没有检索出全部的自媒体账号。再来问问知道沃图社么？看看对于官网的总结如何？成功检索并总结，还把沃图AIGC网站也检索出来了（新建站没多久），总结了网站的大概内容与功能。Miku...",
      "url": "https://mparticle.uc.cn/article.html?uc_param_str=frdnsnpfvecpntnwprdssskt#!wm_aid=92b5fb194a3b4fa9b8bd94b8b4e70ac9!!wm_id=13e3c42778d74908bfa6486a1b34908c",
      "date": "",
      "source_web": "mparticle.uc.cn",
      "web_icon": "https://mparticle.uc.cn/favicon.ico",
      "index": "1"
    }
    // ...更多结果
  ],
  "related_question": [
    "介绍一下AI搜索引擎MIKU",
    "MIKU AI搜索引擎的功能和特点",
    "MIKU AI搜索引擎与其他搜索引擎的比较",
    "MIKU AI搜索引擎的技术架构和应用场景"
  ],
  "response": "AI搜索引擎Miku是一款创新的智能搜索工具，利用先进的人工智能技术，致力于为用户提供快速、精准的搜索体验。Miku通过深入分析用户的搜索意图，能够提供个性化的搜索结果，满足用户的个性化需求。该搜索引擎支持多种搜索方式，包括关键词搜索、分类筛选和时间选择等，能够覆盖新闻、文章、图片和视频等多种信息形式，确保用户能够从多维度获取所需内容。Miku不仅在搜索速度和准确性上表现出色，还具备自动生成大纲和脑图的功能，帮助用户更直观地理解和组织搜索结果。此外，Miku还支持深度提问，能够检索并总结复杂的搜索内容，如自媒体账号和官网信息，进一步提升用户的搜索效率。"
}
```

---

## 快速开始

1. 开通 MIKU Search API KEY

- 访问 [https://platform.hellomiku.cn/platform/home/](https://platform.hellomiku.cn/platform/home/) 注册并获取 API KEY。


2. 初始化虚拟环境并安装依赖：

   ```sh 
   安装uv（Python包管理器），使用curl -LsSf https://astral.sh/uv/install.sh 
   uv init
   uv venv
   source .venv/bin/activate
   uv pip install -r requirements.txt
   ```

3. 配置 `.env` 文件，添加你的 API KEY：

   ```
   MIKU_API_KEY=your_api_key_here
   ```

4. 启动服务：

   ```sh
   uv run main.py
   ```

---

## MCP Server 配置示例

### studio

```json
{
  "mcpServers": {
    "miku_search": {
      "command": "uv",
      "args": [
        "--directory",
        "/MIKU_MCP_SERVER",
        "run",
        "main.py"
      ],
      "env": {
        "MIKU_API_KEY": "<YOUR_MIKU_API_KEY>"
      }
    }
  }
}
```

### sse

```json
{
  "mcpServers": {
    "miku_search": {
      "url": "https://hellomiku.cn/sse?apikey=<YOUR_MIKU_API_KEY>"
    }
  }
}
```

---

## 参考文档
- [MIKU Search 开放平台](https://platform.hellomiku.cn/platform/home/)
- [MIKU Search 产品文档](https://hyperspace.feishu.cn/wiki/BokYwwjreiXg8pkffDhcwSnfnub)
