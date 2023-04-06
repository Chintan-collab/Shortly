class requestFileInformation(object):
    def __init__(self,url):
        self.url=url
        self.type='YOUTUBE_URL'
        self.text=''
        self.preprocessed_text=''
        self.type_of_input=''
        self.score=None
        self.summarized_text=''
        self.error=''