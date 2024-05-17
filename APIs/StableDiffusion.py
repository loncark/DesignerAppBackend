# Define the URL and the payload to send.
url = "http://127.0.0.1:7860/sdapi/v1/txt2img"

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

import asyncio
import aiohttp
import base64

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
