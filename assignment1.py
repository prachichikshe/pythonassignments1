#1. Write a python script for creating directory,displaying its contents.

import os
os.mkdir('program')
os.chdir('program')
os.system('touch a.txt')
os.system('touch a1.txt')
print os.listdir(os.curdir)
print os.listdir('..')

"""Output
python assignment1.py['a.txt', 'a1.txt']"""

