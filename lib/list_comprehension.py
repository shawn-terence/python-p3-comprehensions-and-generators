#!/usr/bin/env python3

def return_evens(num_list):
    even=[number  for number in num_list if number %2==0]
    print(even)
    return even
    pass

def make_exclamation(sentence_list):
    exclamated=[sentence +"!" for sentence in sentence_list]
    print(exclamated)
    return exclamated
    pass
make_exclamation(["Hello", "I'm doing great", "Python is fun"])