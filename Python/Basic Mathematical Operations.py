def instructions():
   text = '''
   Your task is to create a function that does four basic mathematical operations.
   The function should take three arguments - operation(string/char), value1(number), value2(number).
   The function should return result of numbers after applying the chosen operation.
   '''
   return text
def basic_op(operator, value1, value2):
   if operator == '+':
      return value1 + value2
   elif operator == '-':
      return value1 - value2
   elif operator == '*':
      return value1 * value2
   elif operator == '/':
      return value1 / value2

#! Best Pratices
def basic_op(operator, value1, value2):
    return eval(str(value1) + operator + str(value2))