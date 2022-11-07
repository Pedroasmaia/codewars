def instructions():
   text = '''
   Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. No floats or non-positive integers will be passed.
   '''
   return text
def sum_two_smallest_numbers(numbers):
    a = min(numbers)
    numbers.remove(a)
    b = min(numbers)
    return a+b
#! Best Pratices
def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])