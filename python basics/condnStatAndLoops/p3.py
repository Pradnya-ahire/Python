#accept the name and check if its palidrom .

name = input("Enter any name: ")
rev = name[::-1]
if name == rev:
    print("Name is Palindrome")
else:
    print("Name Not Palindrom")

