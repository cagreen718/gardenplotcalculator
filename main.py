import math
def gardenPlot():
  print("Welcome to my Garden Plot Calculator")
  print("Note, all calculations are in feet")
  #these are the first messages needed
  
  
def main(): 
  gardenPlot() 
  length= float(input("Please enter the length of one of the sides of the garden:")) 
  print("You entered:",length) 
  arelen=round(length*length,1)
  print("The total square footage of the garden is", arelen,)
#after we got the sides, next is the area of the circle
  radius=float(input("Enter the radius:"))
  print("You entered:",radius)
  rad=radius**2
  area=round(rad*math.pi,1)
  print("The square footage of the fountain is" ,area)
  #after getting the area we have to subtract the area of length by the area of the circle
  foot=round(arelen-area,1)
  print("The square footage of the flower bed is",foot)
  depth=float(input("Enter the depth of the flower bed:"))
  print("You entered:",depth)
  dep=round(depth*foot,1)
  #the product of depth times footage is what the flower bead will need
  print("The flower bed need",dep," cubic feet of soil")
  

main()