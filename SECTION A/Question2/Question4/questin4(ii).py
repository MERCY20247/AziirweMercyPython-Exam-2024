def word_count(sentence):
    words = sentence.split()
    word_dict = {}
    for word in words:
        word_dict[word] = word_dict.get(word, 0)+1
    return word_dict
sentence = "python exam"
word_counts = word_count(sentence)
print(word_counts) 