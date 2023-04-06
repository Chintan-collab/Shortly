import requests
from bs4 import BeautifulSoup
from src.logger import logging
from youtube_transcript_api import YouTubeTranscriptApi

def get_data_from_url(url):
    print("enter url data")
    r = requests.get(url = url)
    
    soup = BeautifulSoup(r.text , "html.parser")
    text = soup.find_all(['h1','p'])
    logging.info(text)
    text_list = [result_text.text for result_text in text]
    final_text = ' '.join(text_list)
    
    logging.info("final Text -> %s", final_text)
    return final_text

def get_data_from_youtube_url(url):
    print("enter youtube url data")
    video_id = url.split("=")[-1]
    transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
    final_text=''
    for sample in transcript_list:
        final_text = final_text +" "+sample["text"]
    final_text.strip()
    logging.info("final Text -> %s", final_text)
    return final_text

def sentence_seperator(text):
    text = text.replace('.','.<eos>')
    text = text.replace('?','?<eos>')
    text = text.replace('!','!<eos>')
    sentences = text.split('<eos>')
    logging.info("Sentence -> %s",sentences)
    return sentences