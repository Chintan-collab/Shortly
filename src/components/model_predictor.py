from transformers import pipeline
def predictor(chunk,max,min):
    summarizer = pipeline("summarization")
    result = summarizer(chunk, max_length=max, min_length=min, do_sample=False)
    
    return result
