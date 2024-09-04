import math
def circumference_of_circle(radius):
  """Calculates the circumference of a circle given its radius.
  Args:
    radius: The radius of the circle.
  Returns:
    The circumference of the circle.
  """
  return 2 * math.pi * radius
# Example usage:
radius = int(input("enter your radius: "))
circumference = circumference_of_circle(radius)
print(f"The circumference of a circle with radius {radius} is {circumference:.2f}")