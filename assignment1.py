import os
os.mkdir('Assignment1')
os.chdir('Assignment2')
os.system('touch a.txt')
os.system('touch a1.txt')
print os.listdir(os.curdir)
print os.listdir('--')