import re
from queue import Queue
from sys import stdin

if __name__ == '__main__':
    for line in stdin:
        delim = Queue()
        for c in line:
            if c == '.' or c == '?' or c == '!':
                delim.put(c)
        sentences = re.split('[.?!]', line)
        for sentence in sentences:
            if sentence != '' and sentence != '\n':
                sentence = sentence.strip().capitalize()
                sentence = ' '.join(sentence.split())
                if not delim.empty():
                    sentence += delim.get()
                else:
                    sentence += '.'
                print(sentence)

'''

    1 2 3 4
    

'''
        
