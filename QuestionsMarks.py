#Challenge: Have the function QuestionsMarks(str) take the str string parameter, which will contain single digit numbers, letters, and question marks, and check if there are exactly 3 question marks between every pair of two numbers that add up to 10. If so, then your program should return the string true, otherwise it should return the string false. If there aren't any two numbers that add up to 10 in the string, then your program should return false as well.
#For example: if str is "arrb6???4xxbl5???eee5" then your program should return true because there are exactly 3 question marks between 6 and 4, and 3 question marks between 5 and 5 at the end of the string.

#Example:
#Input: "pao9sm??1sskj"
#Output: "false"

#---------------------------------------------------------------------------------------------------
def QuestionsMarks(strParam):
  count_number = 0
  count_mark = 0
  count_pair = 0
  validation = "false"

  for i in strParam:

    if i.isdigit():
      count_number += int(i)
      count_pair += 1

    if count_number > 0 and i == "?":
      count_mark += 1

      if count_number != 10 and count_mark == 3 and count_pair == 2:
        count_number = 0
        count_mark = 0
        count_pair = 0

    if count_number == 10 and count_mark == 3 and count_pair == 2:
      validation = "true"

  return validation

print(QuestionsMarks(input()))
