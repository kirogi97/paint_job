#Definition of variables
Wall_space = float(input("Enter square feet to be painted:"))
gallon_cost = float(input("Enter price per gallon of paint:"))
labour_hours = (Wall_space/115)*8
labour_cost = round(labour_hours*20,3)
paint_used = Wall_space/115
paint_cost = round(paint_used*gallon_cost,3)
Total_cost = round(labour_cost+paint_cost,3)
#Print functions for required outputs
print("Number of gallon(s) of paint requied:gal", paint_used)
print("Hours required for this paint job:", labour_hours)
print("The paint cost:$", paint_cost)
print("Labour for this job will cost:$", labour_cost)
print("The total cost of paint job:$", Total_cost)
