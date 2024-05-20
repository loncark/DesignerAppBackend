import asyncio
import aiohttp
import base64
from config import SD_TXT2IMG_URL

payload = {
  "prompt": "a yellow triangle",
  "batch_size": 1,
  "steps": 1,
  "cfg_scale": 1,
  "width": 64,
  "height": 64,
  "restore_faces": False,
  "tiling": False,  
}

url = SD_TXT2IMG_URL

async def fetch_and_save_image(url, payload):
  async with aiohttp.ClientSession() as session:
    async with session.post(url, json=payload) as response:
      if response.status == 200:
        r = await response.json()
        with open("output.png", 'wb') as f:
          f.write(base64.b64decode(r['images'][0]))
      else:
        print(f"Error: {response.status}")

# Example usage with asyncio
asyncio.run(fetch_and_save_image(url, payload))
