# Student marks analyzer

name = input("What is your name : ")
physics_marks = int(input("How much did you score in Physics :"))
chemistry_marks = int(input("How much did you score in Chemistry :"))
maths_marks = int(input("How much did you score in Maths :"))

total = physics_marks + chemistry_marks + maths_marks
avg = (physics_marks + chemistry_marks + maths_marks)/3

print(f"Hello {name}")
print(F" Your total marks is : {total} ")
print(F"Your average marks in PCM IS : {avg:.2f}")