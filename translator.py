# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 15:20:47 2019

@author: cousi
"""
## in this program we take input from file
"""
from translate import Translator
translator = Translator(to_lang="el")
myfile = open("text.txt")
text = myfile.read()
tra = translator.translate(text)
print(tra)
"""
"""

from translate import Translator
translator = Translator(to_lang="hi")

with open("text.txt") as myfile:
    text = myfile.read()
    output =  translator.translate(text)
    print(output)
    
    """
### taking input from user and translating the data hindi
    
from translate import Translator

translator = Translator(to_lang="hi")
data = input("enter the sentence: ")
print("translation of ","\"",data.upper(),"\"","in hindi is:")
output = translator.translate(data)
print(output)