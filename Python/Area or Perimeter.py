def instructions():
   text = '''
   You are given the length and width of a 4-sided polygon. The polygon can either be a rectangle or a square. If it is a square, return its area. If it is a rectangle, return its perimeter
   '''
   return text
def area_or_perimeter(l , w):
    if l == w:
        return l*w
    else:
        perimeter = l*2 + w*2
        return perimeter