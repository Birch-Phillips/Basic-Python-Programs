def reverse(a_string):
  if a_string == "":
    return ""
  return reverse(a_string[1:]) + a_string[0] 
  
print(reverse(input("Enter text to reverse:\n")))
