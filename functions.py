#Pythonic functions are defined by the reserved word "def"
#followed by the name of the function "def function_name:"

def function():  #simple function
  pass

"""
  Functions can also accept parameters/arguments
  We use the reserved word 'return' to output 
  whatever the function was doing in its body
"""
def calculate_area(length, width):  
  """calculates the area of a rectangle and returns the output"""
  return int(length) * int(width)
    
