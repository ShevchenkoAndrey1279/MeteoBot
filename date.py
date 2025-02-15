import requests 
from bs4 import BeautifulSoup  

class CityNotFoundError(Exception):
    pass

def date(day): 
    URL = "https://pogoda.mail.ru/prognoz/moskva/14dney/" 
    HEADERS = {  
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
    "accept": "*/*"
    }
    html = requests.get(URL, headers=HEADERS) 

    if html.status_code == 200: 
        soup = BeautifulSoup(html.text, "html.parser") 
        
        soup_info = soup.find('div', id=f"day{day}")  
        text = soup_info.text

        return text
    else:
        return None






