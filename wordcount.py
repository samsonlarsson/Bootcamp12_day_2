def words(sentence):
    sentence = sentence.split()
    # splits a string of items in a sentence words
    new_dict = {} 
    for word in sentence: 
        if word.isdigit(): 
            word = int(word) 
        if word in new_dict:
            new_dict[word] += 1
        else:
            new_dict[word] = 1

    return new_dict
