import nltk
import pymorphy3
import nltk

from nltk.tokenize import word_tokenize
from nltk import sent_tokenize


def filter(word1, word2):
  if (word1.tag.POS =='NOUN' or word1.tag.POS == 'ADJF') and (word2.tag.POS == 'NOUN' or word2.tag.POS == 'ADJF'):
    if (word1.tag.case == word2.tag.case) and (word1.tag.number == word2.tag.number) and (word1.tag.gender == word2.tag.gender):
      print(f"{word1.normal_form} {word2.normal_form}")

text_file = open('test_text.txt', 'r')
text_data = text_file.read()


nltk.download('punkt_tab')
tokens = word_tokenize(text_data)

filtered_tokens = []
for token in tokens:
    if token.isalpha():
        filtered_tokens.append(token)

m = pymorphy3.MorphAnalyzer()

for i in range(0, len(filtered_tokens)-1):
      filter(m.parse(filtered_tokens[i])[0], m.parse(filtered_tokens[i+1])[0])