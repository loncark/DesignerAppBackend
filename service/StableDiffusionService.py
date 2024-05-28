import aiohttp
from config import SD_TXT2IMG_URL, SD_IMG2IMG_URL

async def txt2img(payload):
  return await call_api(SD_TXT2IMG_URL, payload)

        
async def img2img(payload):
  return await call_api(SD_IMG2IMG_URL, payload)


async def call_api(url, payload):
   async with aiohttp.ClientSession() as session:
    async with session.post(url, json=payload) as response:
      if response.status == 200:
        return await response.json()
      else:
        print(f"Error: {response.status}")



