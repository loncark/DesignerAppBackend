# START VPN ON US OR JAPAN SERVER BEFORE RUNNING

import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY) 
model = genai.GenerativeModel('gemini-pro')

def fetchResponse(prompt):
    #prompt = 'Tell me what cats are in one sentence.'
    response = model.generate_content(prompt)

    return response.text

def generateTags(phrase):
    
    prompt = f"""Generate me a list of tags I could use for Etsy SEO optimization of my "{phrase}" listing. Separate these tags using a comma and write out nothing else."""
    response = model.generate_content(prompt)

    return response.text.split(", ")

def generateTitle(phrase):
    prompt = f"""Generate me a list of synonyms I could use in the title of my "{phrase}" listing of Etsy. They should be some phrases that people usually type in the search bar when looking for similar items. The first letter of every word in a synonym should be capitalized. Separate these tags using a comma and write out nothing else."""
    response = model.generate_content(prompt)

    return response.text.split(", ")