#Challenge:
#Have the function LongestWord(sen) take the sen parameter being passed and return the longest word in the string. If there are two or more words that are the same length, return the first word from the string with that length. Ignore punctuation and assume sen will not be empty. Words may also contain numbers, for example "Hello world123 567"

#Examples:
#Input: "fun&!! time"
#Output: time

#Input: "I love dogs"
#Output: love

def LongestWord(sen):
  word = ""
  aux = 0
  temp_word = sen[0]
  list_char = [" ", "!", "@", "#", "$", "%", "&", "*", "/", "|", "^", "~", "]", "[", "{", "}", "ª", "º", ";", ":", "<", ">", ",", ".", "´", "`", "'", "?"]  
  
  for i in sen:
    aux += 1

    if i not in list_char:
      word += i

    if i == " ":
      if len(word) > len(temp_word):
        temp_word = word
        word = ""
      else:
        word = ""

    if aux == len(sen):
      if len(word) > len(temp_word):
        temp_word = word
  
  return temp_word

print(LongestWord(input("Text here --> ")))