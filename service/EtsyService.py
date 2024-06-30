#https://openapi.etsy.com/v3/application/listings/active
#findAllListingsActive

import json

def fetchProducts(keyword):
    with open('sample JSONs\EtsyDummyProducts.json', 'r') as file:
        data = json.load(file)
    return data
