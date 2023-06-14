from collections import Counter
import re
import nltk
from nltk.corpus import stopwords

class Summarize():
    def __init__(self, record):
        self.record = record
        self.summary = ''

    def create_summary():
        initial_record = self.record
        modified_record = initial_record.replace('<br>', '')
        modified_record = modified_record.replace('\d{2}-\d{2}-\d{4}\s\d{2}:\d{2}', '')
        modified_record = re.sub('[^a-zA-Z]', ' ', modified_record)
        modified_record = re.sub('\s+', ' ', modified_record)

        
        while True:
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
        """Remove stop words from string and return string."""
        stop_words = set(stopwords.words('english'))
        speech_edit_no_stop = ''
        for word in nltk.word_tokenize(modified_record):
            # word_tokenize will tell the computer about the words in the long string without creating an array allowing us to return a long string 'fixed' with the stopwords removed
            if word.lower() not in stop_words:
                speech_edit_no_stop += word + ' '  
        return speech_edit_no_stop

    def get_word_freq(speech_edit_no_stop):
        """Return a dictionary of word frequency in a string."""
        word_freq = nltk.FreqDist(nltk.word_tokenize(speech_edit_no_stop.lower()))
        return word_freq

    def score_sentences(initial_record, word_freq, max_words):
        """Return dictionary of sentence scores based on word frequency."""
        sent_scores = dict()
        sentences = nltk.sent_tokenize(speech)
        # using the original speech with just the spelling error fixed and the extra spaces removed because we need all the original capital letters and stopwords in the sentences
        for sent in sentences:
            sent_scores[sent] = 0
            words = nltk.word_tokenize(sent.lower())
            sent_word_count = len(words)
            if sent_word_count <= int(max_words):
                for word in words:
                    if word in word_freq.keys():
                        sent_scores[sent] += word_freq[word]
                sent_scores[sent] = sent_scores[sent] / sent_word_count
                # diving by the number of words in the sentence to get the average score for the sentence to normalise the scores and make them comparable for long and short sentences that contain important words, otherwise the longer sentences would have higher scores and there would be a bias towards longer sentences
        return sent_scores

        return modified_record

if __name__ == "__main__":
    with open('./file_output/symptoms.txt', 'r') as f:
        record = f.read()
        print(type(record))
    # mysummary = Summarize.create_summary(record)
    # print(mysummary)