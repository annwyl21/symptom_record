from collections import Counter
import re
import nltk
from nltk.corpus import stopwords

def create_summary(record):
    initial_record = record
    initial_record = initial_record.replace('<br>', '.')
    #modified_record = modified_record.replace('\d{2}-\d{2}-\d{4}\s\d{2}:\d{2}', '') # specifically replaces the date/time stamp
    modified_record = re.sub('[^a-zA-Z]', ' ', initial_record)
    modified_record = re.sub('\s+', ' ', modified_record)

    max_words = 12
    num_sents = 3
                    
    speech_edit_no_stop = remove_stop_words(modified_record)
    word_freq = get_word_freq(speech_edit_no_stop)
    sent_scores = score_sentences(initial_record, word_freq, max_words)

    counts = Counter(sent_scores)
    summary = counts.most_common(int(num_sents))
    print("\nSUMMARY:")
    for i in summary:
        print(i[0])

def remove_stop_words(modified_record):
    stop_words = set(stopwords.words('english'))
    speech_edit_no_stop = ''
    for word in nltk.word_tokenize(modified_record):
        if word.lower() not in stop_words:
            speech_edit_no_stop += word + ' '  
    return speech_edit_no_stop

def get_word_freq(speech_edit_no_stop):
    word_freq = nltk.FreqDist(nltk.word_tokenize(speech_edit_no_stop.lower()))
    return word_freq

def score_sentences(initial_record, word_freq, max_words):
    sent_scores = dict()
    sentences = nltk.sent_tokenize(initial_record)
    for sent in sentences:
        sent_scores[sent] = 0
        words = nltk.word_tokenize(sent.lower())
        sent_word_count = len(words)
        if sent_word_count <= int(max_words):
            for word in words:
                if word in word_freq.keys():
                    sent_scores[sent] += word_freq[word]
            sent_scores[sent] = sent_scores[sent] / sent_word_count
    return sent_scores

if __name__ == "__main__":
    with open('./file_output/symptoms.txt', 'r') as f:
        record = f.read()
    
    create_summary(record)
    # mysummary = Summarize.create_summary(record)
    # print(mysummary)