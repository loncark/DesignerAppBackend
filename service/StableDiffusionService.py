import aiohttp, asyncio
from config import SD_TXT2IMG_URL, SD_IMG2IMG_URL

async def txt2img(payload):
  return await call_api(SD_TXT2IMG_URL, payload)

        
async def img2img(payload):
  return await call_api(SD_IMG2IMG_URL, payload)


async def call_api(url, payload, timeout=3000):  # 50 minutes timeout
    async with aiohttp.ClientSession() as session:
        try:
            async with session.post(url, json=payload, timeout=aiohttp.ClientTimeout(total=timeout)) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    print(f"Error: {response.status}")
                    return None
        except asyncio.TimeoutError:
            print(f"Request timed out after {timeout} seconds")
            return None
        except aiohttp.ClientError as e:
            print(f"Client error occurred: {e}")
            return None



