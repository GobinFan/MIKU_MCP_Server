# main.py
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv 
import os 
from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP 

load_dotenv()

mcp = FastMCP("MIKU")
 

import aiohttp
import asyncio

@mcp.tool()
async def mikusearch(query: str) -> dict:
    """
    执行AI搜索并返回结果
    
    - **query**: 搜索查询内容 
    - **search_mode**: 搜索模式(simple_search/deep_search),默认simple_search
    - **language_mode**: 语言模式(zh_CN/zh_HK/en_us/ja/ko/ru/ar),默认zh_CN
    """
    
    url = "https://api.hellomiku.cn/api/v1/aisearch"
    headers = {
        "Content-Type": "application/json",
        "Connection": "keep-alive",
        "Accept": "*/*"
    }

    api_key = os.getenv("MIKU_API_KEY") 
    data = { 
        "query": query,
        "api_key": api_key,
        "search_mode": "simple_search",
        "stream_mode": "false",
        "language_mode": "zh_CN"
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=data, headers=headers) as response:
            return await response.json()

if __name__ == "__main__":
    mcp.run(transport="stdio")