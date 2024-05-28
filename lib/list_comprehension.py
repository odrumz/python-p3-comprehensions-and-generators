#!/usr/bin/env python3

def return_evens(num_list):
    even = [num  for num in num_list if num % 2 == 0]
    return even
print(return_evens([0,1,2,3,4,5,6,7,8]))
    

        

def make_exclamation(sentence_list):
    return [sentence + "!"  for sentence in sentence_list ]