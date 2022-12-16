# Given a sentence as input, calculate and output the average word length of that sentence.
# To calculate the average word length, you need to divide the sum of all word lengths by the number of words in the sentence.

text = input('Input the text here: ')

a = text.split()
count=0
av = 0
for b in a:
    count = count+1
    av =  av + len(b)
    
print(av/count)