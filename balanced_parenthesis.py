# Parentheses are balanced, if all opening parentheses have their corresponding closing parentheses.
# Given an expression as input, we need to find out whether the parentheses are balanced or not.
# Implement the balanced() function to return True if the parentheses in the given expression are balanced, and False if not.

def balanced(expression):
    a = expression
    b = []

    for it in a:
        if it == '(':
            b.insert(0,'(')
        elif it == ')':
            try:
                b.pop(0)
            except:
                return False
    if b == []:
        return True
    else:
        return False

print(balanced(input()))