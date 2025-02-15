from transliterate import translit
import requests 
from bs4 import BeautifulSoup  

def translate(city):

    return translit(city, 'ru', reversed=True)

def weather(city): 
    URL = "https://pogoda.mail.ru/prognoz/" + translate(city).lower() + "/14dney/" 
    HEADERS = {  
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
    "accept": "*/*"
    }
    html = requests.get(URL, headers=HEADERS) 

    if html.status_code == 200: 
        soup = BeautifulSoup(html.text, "html.parser") 
        
        soup_info = soup.find_all('span', class_="text text_block text_bold_medium margin_bottom_10") 
        text = []
        for day in soup_info:
            text.append(day.text)
        

        return text
                 
    else:
        return None

def temperature(city): 
    URL = "https://pogoda.mail.ru/prognoz/" + translate(city).lower() + "/14dney/" 
    HEADERS = {  
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
    "accept": "*/*"
    }
    html = requests.get(URL, headers=HEADERS) 

    if html.status_code == 200: 
        soup = BeautifulSoup(html.text, "html.parser") 
        
        soup_info = soup.find_all('span', class_="text text_block text_light_normal text_fixed color_gray") 
        text = []
        for day in soup_info:
            text.append(day.text)
        

        return text
                 
    else:
        return None

def osadki(city): 
    URL = "https://pogoda.mail.ru/prognoz/" + translate(city).lower() + "/14dney/" 
    HEADERS = {  
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
    "accept": "*/*"
    }
    html = requests.get(URL, headers=HEADERS) 

    if html.status_code == 200: 
        soup = BeautifulSoup(html.text, "html.parser") 
        
        soup_info = soup.find_all('span', class_="text text_block text_light_normal text_fixed") 
        text = []
        for day in soup_info:
            text.append(day.text)

        return text
                 
    else:
        return None 


