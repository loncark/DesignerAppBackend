import aiohttp
from config import SD_TXT2IMG_URL, SD_IMG2IMG_URL
import json

async def txt2img(payload):
  return await generateImage(SD_TXT2IMG_URL, payload)

        
async def img2img(payload):
  return await generateImage(SD_IMG2IMG_URL, payload)


async def generateImage(url, payload):  # 50 minutes timeout
    async with aiohttp.ClientSession() as session:
        try:
            async with session.post(url, json=payload, timeout=aiohttp.ClientTimeout(total=3000)) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    print(f"Error: {response.status}")
                    return json.dumps({"Error": f"{response.status} Image generation failed."})
        except Exception as e:
            print(e)
            return json.dumps({"Exception": e})



