# IU Semester 1 : basic grade calculator
# This script helps me track my goals for my applied AI degree
print("--- IU Grade Goal Tracker---")

# getting user input
module_name = input("enter the module name (e.g.,python, math): ")
current_points = float(inout("How many points do you have so far? (0-50): "))
target_grade = float(input(" What is your targeted total points?   (e.g., 90 for an A): "))

#basic logic to find the gap
needed_points = target_points - current points
print("\n--- Results  for " + moudule_name + ".....")
if needed points <= 0 :
  print("Good! you reached your goal!")
elif needed_points > 50 :
  print(" goal is very close! You still need " + str(needed_points) + " points more, You got it!" )
else:
  print(" keep pushing you got it!")
        
        
                           


                      
      
