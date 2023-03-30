import requests
from bs4 import BeautifulSoup

def get_data_from_url(url:str):
    r = requests.get(url = url)
    soup = BeautifulSoup(r.text , "html.parser")
    text = soup.find_all(['h1,h2,h3,h4,h5,h6,p'])
    text_list = [result_text.text for result_text in text]
    final_text = ' '.join(text_list)
    return final_text

def sentence_seperator(text:str):
    text = text.replace('.','.<eos>')
    text = text.replace('?','?<eos>')
    text = text.replace('!','!<eos>')
    sentences = text.split('<eos>')