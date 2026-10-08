#1 Accept 2 val S and N Print square of first N numbets Starting from S

S = int(input("Enter Start number: "))
N = int(input("Enter N: "))

print(S*S, (S+1)*(S+1), (S+2)*(S+2), (S+3)*(S+3), (S+4)*(S+4))

#2 Reverse the accepted string
str1 = input("Enter string: ")
print(str1[::-1])

#3 Accept sentence from user and count the vowels 
sentence = input("Enter sentence: ")

count = sentence.lower().count('a') + \
        sentence.lower().count('e') + \
        sentence.lower().count('i') + \
        sentence.lower().count('o') + \
        sentence.lower().count('u')

print("Number of vowels:", count)

#4 Remove Duplicates From List
lst = [1, 2, 3, 2, 4, 1, 5]

result = list(set(lst))

print(result)

#5 Reverse the list
lst = [10, 20, 30, 40, 50]

print(lst[::-1])

#6 Accept Sentece from user and count the vowels
sentence = input("Enter sentence: ")

vowels = "aeiouAEIOU"

count = sum(sentence.count(vowel) for vowel in vowels)

print("Number of vowels:", count)