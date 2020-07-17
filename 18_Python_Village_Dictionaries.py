# https://stackoverflow.com/questions/9542738/python-find-in-list

"""count each word in a sentence"""

sentence = input("Your string: ")

sentence = sentence.split() # split the sentence into a list of words

new_sentence=  list(dict.fromkeys(sentence)) # retain unique words as search items in a second list

# https://www.w3schools.com/python/python_howto_remove_duplicates.asp

for i in new_sentence:

    print(i, sentence.count(i))
    

    
