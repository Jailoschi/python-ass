#!/usr/bin/python3
"""
calculate_average function module
"""

def calculate_average(num1, num2, num3):
  """ 
  Calculates the average of three numbers

  Args:
    num1 (float): first number
    num2 (float): second number
    num3 (float): third number

  Returns:
    Average of the three numbers
  """
  return (num1 + num2 + num3) / 3

# use float() for input of values as per requirement
# user input here
print("The average of {}, {} and {} is {}".format(num1, num2, num3, 
                                                  calculate_area(num1, num2, num3)))
