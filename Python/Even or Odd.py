def instructions():
   text = '''
Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.
   '''
   return text

def even_or_odd(number):
    if number % 2 == 1:
        return "Odd"
    elif number % 2 == 0:
        return "Even"

#!Bestpratices

def even_or_odd(number):
  return 'Even' if number % 2 == 0 else 'Odd'