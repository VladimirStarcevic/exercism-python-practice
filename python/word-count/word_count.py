import re
def count_words(sentence):
    word_list = re.findall(r"[a-z0-9]+(?:'[a-z]+)?", sentence.lower())
    word_counter = {}
    for word in word_list:
        word_counter[word] = word_counter.get(word, 0) + 1
    return word_counter

sentence = """That's the password: 'PASSWORD 123'!", cried the Special Agent.\nSo I fled"""
word_dict = count_words(sentence)
for key, value in word_dict.items():
    print(f"{key}: {value}")
