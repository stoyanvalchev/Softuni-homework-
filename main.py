name = input()
grades= 0
bad_note = 0
sum = 0
while True:
     grade = float(input())
     grades +=1


     if grade < 4:
          bad_note += 1

          if bad_note == 2:
               print(f"{name} has been excluded at {grades} grade")
               break
          grades -= 1
     else:
          sum += grade
     if grades == 12:
          avg = sum / 12
          print(f"{name} graduated. Average grade: {avg:.2f}")
          break
