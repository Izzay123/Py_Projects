# Make a program that finds and replaces the input from supplied text. Produces count of total replacements beforehand.
text = input('Type your text to check: ')

par1 = input('Word to replace: ')
par2 = input('Word replacing it: ')
print(text.count(par1))
print(text.replace(par1,par2))