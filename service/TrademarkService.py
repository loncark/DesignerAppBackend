from interface.repositoryInterface.TrademarkCheckRepository import TrademarkCheckRepository

class TrademarkService:
  def __init__(self, repository: TrademarkCheckRepository):
    self.repository = repository

  def getTrademarks(self, prompt):
    return self.filterJson(self.fetchUnfilteredTrademarkData(prompt))

  def fetchUnfilteredTrademarkData(self, prompt):
    return self.repository.getTrademarks(prompt)    

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