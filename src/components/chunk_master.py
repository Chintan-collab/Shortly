from src.utils import sentence_seperator
from src.logger import logging
def chunk_creator(text):
    max_chunk_count = 500
    current_chunk_count = 0
    chunks_list = []

    sentences = sentence_seperator(text)

    for sentence in sentences:
        if len(chunks_list) == current_chunk_count+1:
            if len(chunks_list[current_chunk_count]) + len(sentence.split(' ')) <= max_chunk_count:
                chunks_list[current_chunk_count].extend(sentence.split(' '))
            else:
                current_chunk_count += 1
                chunks_list.append(sentence.split(' '))
        else:
            chunks_list.append(sentence.split(' '))

    for chunks in range(len(chunks_list)):
        chunks_list[chunks] = ' '.join(chunks_list[chunks])
    logging.info("\n Chunk List -. %s",chunks_list)
    return chunks_list