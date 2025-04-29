<div align="center">
    <img alt="vision_agent" height="200px" src="https://hellomiku.com/img/logo.png"> 
      
# MIKU Search MCP Server
[**中文**](https://github.com/GobinFan/MIKU_MCP_Server/blob/main/README.md) | English

</div>

## About MIKU

AI MIKU is an innovative AI search engine based on multi-agent technology, dedicated to providing users with accurate, personalized, and real-time search experiences. The Miku MCP Server is the core service component of the MIKU ecosystem, responsible for handling and distributing intelligent search requests. It supports multiple languages and search modes, making it easy for developers to integrate and extend.  
Learn more about MIKU at: [hellomiku.com](https://hellomiku.com)

## Main Features

- AI-powered intelligent search service supporting multiple languages (Simplified Chinese, Traditional Chinese, English, Japanese, Korean, Russian, Arabic).
- Supports both simple_search and deep_search modes to meet different needs.
- API KEY authentication to ensure data security.

---

## Response Example

```json
{
  "conversation_id": "7825bca7-370f-4eea-98cd-bfc76b9db742",
  "code": 200,
  "source": [
    {
      "title": "[1] Miku, Fast and Accurate AI Search Engine, Auto-generates Outline Mind Maps",
      "snippet": "Miku is a fast and accurate AI search engine. The search results can be automatically summarized and generate outlines or mind maps. Visit the Miku website and log in with your phone number. After logging in, you can ask questions directly. We choose deep search and ask about our media accounts. It retrieves and summarizes the accounts, though not all are found. Next, we ask about Wotu Club and see how the official site is summarized. It successfully retrieves and summarizes, also finding the Wotu AIGC site (recently launched), summarizing its main content and features. Miku...",
      "url": "https://mparticle.uc.cn/article.html?uc_param_str=frdnsnpfvecpntnwprdssskt#!wm_aid=92b5fb194a3b4fa9b8bd94b8b4e70ac9!!wm_id=13e3c42778d74908bfa6486a1b34908c",
      "date": "",
      "source_web": "mparticle.uc.cn",
      "web_icon": "https://mparticle.uc.cn/favicon.ico",
      "index": "1"
    }
    // ...more results
  ],
  "related_question": [
    "Introduce the AI search engine MIKU",
    "Features and advantages of MIKU AI search engine",
    "Comparison between MIKU AI search engine and others",
    "Technical architecture and application scenarios of MIKU AI search engine"
  ],
  "response": "The AI search engine Miku is an innovative intelligent search tool that leverages advanced AI technology to provide users with fast and accurate search experiences. By deeply analyzing user search intent, Miku delivers personalized results to meet individual needs. It supports various search methods, including keyword search, category filtering, and time selection, covering news, articles, images, and videos to ensure users can access content from multiple dimensions. Miku excels in speed and accuracy and can automatically generate outlines and mind maps, helping users better understand and organize results. It also supports deep queries, retrieving and summarizing complex content such as media accounts and official sites, further improving search efficiency."
}
```

---

## Quick Start

1. Get a MIKU Search API KEY

- Visit [https://platform.hellomiku.cn/platform/home/](https://platform.hellomiku.cn/platform/home/) to register and obtain your API KEY.

2. Initialize the virtual environment and install dependencies:

   ```sh
   Install uv (Python package manager) using curl -LsSf https://astral.sh/uv/install.sh
   uv init
   uv venv
   source .venv/bin/activate
   uv pip install -r requirements.txt
   ```

3. Configure the `.env` file and add your API KEY:

   ```
   MIKU_API_KEY=your_api_key_here
   ```

4. Start the service:

   ```sh
   uv run main.py
   ```

---

## MCP Server Configuration Example

### studio (cursor, cline, etc.)

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

### sse (cursor, cline, etc.)

```json
{
  "mcpServers": {
    "miku_search": {
      "url": "https://hellomiku.cn/sse?apikey=<YOUR_MIKU_API_KEY>"
    }
  }
}
```

### sse auth configuration example
cherry Studio example:

<img width="1080" alt="image" src="https://github.com/user-attachments/assets/e924c2c8-6523-4400-9a29-6408ed24c456" />

---

## Reference Docs
- [MIKU Search Open Platform](https://platform.hellomiku.cn/platform/home/)
- [MIKU Search Product Docs](https://hyperspace.feishu.cn/wiki/BokYwwjreiXg8pkffDhcwSnfnub)