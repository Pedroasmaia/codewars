def instructions():
   text = '''
   You are given two interior angles (in degrees) of a triangle.
   Write a function to return the 3rd.
   Note: only positive integers will be tested.
   '''
   return text
def other_angle(a, b):
    x = a + b
    y = 180 - x
    return y