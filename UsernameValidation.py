#Challenge:
#Have the function CodelandUsernameValidation(str) take the str parameter being passed and determine if the string is a valid username according to the following rules:

#1. The username is between 4 and 25 characters.
#2. It must start with a letter.
#3. It can only contain letters, numbers, and the underscore character.
#4. It cannot end with an underscore character.

#If the username is valid then your program should return the string true, otherwise return the string false.

#Examples:
#Input: "aa_"
#Output: false

#Input: "u__hello_world123"
#Output: true

#---------------------------------------------------------------------------------------------------

import re

def CodelandUsernameValidation(strParam):
  validation = ""
  regex_letter_list = r'[A-Za-záàâãéèêíïóôõöúçñ]'
  regex_all_list = r'^[a-zA-Z0-9_]+$'

  if re.search(regex_letter_list, strParam[0]) and strParam[-1] != "_" and len(strParam) > 3 and len(strParam) < 26:
    for i in strParam:
      if re.search(regex_all_list, i):
        validation = "true"
      else:
        validation = "false"
        break
  
  else:
    validation = "false"
  
  return validation

print(CodelandUsernameValidation(input("Text here --> ")))
