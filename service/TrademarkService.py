from repository.RealTrademarkRepository import RealTrademarkRepository

class TrademarkService:
  def __init__(self) :
    self.repository = RealTrademarkRepository()

  def fetchAndFilterResponse(self, prompt):
      return self.filterJson(self.repository.fetchData(prompt))      

  def filterJson(self, data):
    transformedData = {}
    transformedData["count"] = data["count"]
    transformedData["items"] = []

    for item in data["items"]:
      newItem = {}
      newItem["description"] = item["description"]
      newItem["keyword"] = item["keyword"]
      newItem["owners"] = []

      for owner in item["owners"]:
        ownerData = {
            "address1": owner.get("address1"),
            "city": owner.get("city"),
            "country": owner.get("country"),
            "name": owner.get("name"),
        }
        newItem["owners"].append(ownerData)

      newItem["status_label"] = item["status_label"]
      transformedData["items"].append(newItem)
      
    return transformedData