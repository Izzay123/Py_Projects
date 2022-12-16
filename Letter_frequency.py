#Letter frequency as a percentage from a statement
in1 = input('Text to scour: ')
in2 = input('Letter to check: ')

a = in1.count(in2)
b = len(in1)

print(str(int((a/b)*100))+'%')