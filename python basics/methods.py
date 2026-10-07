text = "  hellow IMCC  "

#1strip removes the spaces from start and end
print("Remove Spaces :",text.strip())

#2coverts the string to uppercase
print("To Upper :",text.upper())

#3coverts to lower case
print("To Lower :",text.lower())

#4 Capita;lize First letter
print("To Capitalize First letters :",text.capitalize())

#5to capitalize each word(Title case)
print(text.title())

#6count occurences of a substring
print("Letter L occurs :",text.count("l")," Times in text")


#7Replace Substring
print(text.replace("IMCC","Python Magic"))

#8finfd the posution of sub str(-1 if not found)
print("position of Imcc in text is :",text.find(IMCC))

#9check if string start or end withcertain substring
print(text.startswith("we"))
print(text.endswith("m"))

#10split string into list by a delimeter
print("Simple Spit",text.split())



