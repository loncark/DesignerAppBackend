from interface.Repository import Repository
import aiohttp, json

class RealStableDiffusionRepository(Repository):
    def __init__(self):
        pass
    
    async def generateImage(self, url, payload):
        async with aiohttp.ClientSession() as session:
          try:
              async with session.post(url, json=payload, timeout=aiohttp.ClientTimeout(total=3000)) as response:    # 50 minutes timeout
                  if response.status == 200:
                      return await response.json()
                  else:
                      print(f"Error: {response.status}")
                      return json.dumps({"Error": f"{response.status} Image generation failed."})
          except Exception as e:
              print(e)
              return json.dumps({"Exception": e})