def instructions():
   text = '''
   Create a function that takes 2 integers in form of a string as an input, and outputs the sum (also as a string):
   '''
   return text
def sum_str(a, b):
    if a == "":
        a = 0
    else:
        a = int(a)
    if b == "":
        b = 0
    else:
        b = int(b)
    total = a + b
    total = str(total)
    return total