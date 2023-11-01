
# Making our own types also know as alias

from typing import Union

perType = Union[float, int]

percentages : list[perType] = [88, 99, 50, 51, 70] 

grades : list[str] = []

for  per in percentages:
  grade: str = ""
  
  if per >= 0 and per < 33:
       grade = "Fail"
  elif per >= 33 and per < 40:
    grade = "E"    
  elif per >= 40 and per < 50:
    grade = "D"
  elif per >= 50 and per < 60:
    grade = "C" 
  elif per >= 60 and per < 70:
    grade = "B" 
  elif per >= 70 and per < 80:
    grade = "A"
  elif per >= 80 and per < 100:
    grade = "A+"
    
  grades.append(grade)
  
  print(percentages)
  print(grades)
  
  zip(percentages, grades)
  
  print(list(zip(percentages, grades)))
  
  roll_no : list[int] = list(range(len(percentages)))
  roll_no
  
  print(list(zip(roll_no, percentages, grades)))