class requestFileInformation(object):
    def __init__(self,url):
        self.url=url
        self.type='URL'
        self.text=''
        self.preprocessed_text=''
        self.type_of_input=''
        self.score=None
        self.summarized_text=''
        self.error=''