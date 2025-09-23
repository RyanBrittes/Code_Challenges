#Challenge: Have the function FirstReverse(str) take the str parameter being passed and return the string in reversed order. For example: if the input string is "Hello World and Coders" then your program should return the string sredoC dna dlroW olleH.

#Example
#Input: "Coderbyte"
#Output: "etybredoC"

#---------------------------------------------------------------------------------------------------

def FirstReverse(strParam):
  word = ""
  i = len(strParam) - 1
  
  while i != -1:
    word += strParam[i]
    i -= 1

  return word

print(FirstReverse(input("Text here --> ")))