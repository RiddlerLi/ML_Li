__author__ = 'Administrator'
# -*- coding:utf-8 -*-

import re
from os import listdir
from nltk import pos_tag

def list1(string):
    words = re.findall(r'[a-zA-Z]+\-*[a-zA-Z]+\b', string)
    return words

def tag(word_list):
    t = pos_tag(word_list)
    return t

def file_read(filename):
    with open(filename, 'r') as fp:
        article = fp.read()
    return article

def most_words_num(t_list):
    str_dict = {}
    pattern = re.compile(r'N+|V+')
    for item,tag in t_list:
        if item in str_dict and re.match(pattern,tag):
            str_dict[item] += 1
        elif item not in str_dict and  re.match(pattern,tag):
            str_dict[item] = 1
    max_value = max([str_dict[key] for key in str_dict])
    count =[key for key in str_dict if str_dict[key]==max_value]
    return (max_value, ",".join(count))

if __name__ == '__main__':
    txt_list = listdir('txt')
    print txt_list
    for t in txt_list:
        string = file_read('txt/'+t)
        print string
        words = list1(string)
        print words
        t_list = tag(words)
        print t_list
        times, word = most_words_num(t_list)
        print t.split('.')[0]+' 出现最多的名词或动词为' + str(word) + '，出现了' + str(times) + '次'