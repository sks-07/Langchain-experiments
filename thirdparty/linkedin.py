import requests
import os
import json

def scrape_linkedin_profile(linkedin_URL: str, Trial:bool)-> dict:
    if Trial:
        with open('subham.json','r') as f:
            response = json.load(f)
            data = response['person']
            # return data
            data = {
                k:v for k,v in data.items()
                if v not in ([],"","",None) and k not in ["certifications"]
            }
            
    else:        
        api_endpoint = "https://api.scrapin.io/enrichment/profile"
        params = {
            "apikey": os.environ['SCRAPIN_API_kEY'],
            "linkedInUrl": linkedin_URL
        }
        response = requests.get(
            api_endpoint,
            params=params,
            timeout=10
        )
        
        data = response.json().get('person')
        data = {
                k:v for k,v in data.items()
                if v not in ([],"","",None) and k not in ["certifications"]
            }
    return data
    

if __name__=='__main__':
    URL = 'https://www.linkedin.com/in/subham-kumar-singh-bb03001a0'
    print(scrape_linkedin_profile(URL,1))