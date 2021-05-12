# -*- coding: utf-8 -*-
"""
Created on Wed May 12 22:38:02 2021

@author: Hafiz Muhammad Adeel
"""


#importing required package 
import re

#defining a generator function with the default regrex string
def get_Model_loss(regex='^[\d\w]+(\d.\d+).hdf5$'):
    reg = re.compile(regex)
    #interating through the files and keep looping untill we have the loss
    while True:
        file_name = yield
        file_matched = reg.match(file_name)
        result = None if match is None else float(match.group(1))
        yield result
#defining the coroutine to send value into degnerator
def send_gen(gen, item):
    #sending None to every newly created generator to get the appropriate 
    #line of generator
    gen.send(None)
    result = gen.send(item)
    return result

def main():
    #Model Weights files
    filenames = ['ML_model.h5','Model_weights_c7e3450.15.hdf5','weights_ercd3_0.hdf5']
    #calling generator dunction to keep reading the weight files
    gen = get_Model_loss()
    for filename in filenames:
        #calling coroutine to pass generator value
        result = send_gen(gen, filename)
        if not result:
            continue
        #printing the result
        print(result)
if __name__ == '__main__':
    main()