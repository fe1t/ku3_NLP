#!/usr/bin/python

import re

def find_before(pos):
    if pos < 0:
        return ""
    if text[pos][0].isupper():
        return find_before(pos - 1) + text[pos] + " "
    return ""

def find_after(pos):
    if pos >= len(text):
        return ""
    if text[pos][0].isupper():
        return text[pos] + " " + find_after(pos + 1)
    return ""

with open('/home/vagrant/KU/cpe3/NLP/regex/Reuter_Corpus/reut2-000.sgm', 'rb') as f:
    data = f.read().splitlines()

text = "".join(data)
# text = "Comissaria Smith said in its weekly review."
# text = "The circumstances at the time will determine what we do, said Arthur Miller."
text = text.split()

for i in range(0, len(text)):
    if text[i] == 'said':
        words = find_before(i-1)
        if words is not None and words != "":
            print words
        words = find_after(i+1)
        if words is not None and words != "":
            print words

