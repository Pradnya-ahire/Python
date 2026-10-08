# my_list =[]
# print(my_list)

# fruits = ["apple","banana","cherry"]
# print(fruits)


# numbers = [10,20,30,40]
# print(numbers[0])
# print(numbers[-2])

# numbers.append(50)
# numbers.insert(0,0)
# print(numbers)

# numbers.remove(0) #removes the specified item

# numbers.pop() #removes the last item

# print(numbers)


# # sum
# print("Sum of list numbers is: ",sum(numbers))

# #length
# print("No. of items in the list: ",len(numbers))

# #sorting
# print("List in Ascending order",sorted(numbers))
# print("List in decending order",sorted(numbers, reverse =True))

#1 Create a list of  !0 numbers and Display the Sum of last 4 Elements
l1 = [1,2,3,4,5,6,7,8,9,10]
sub_l1 = l1[6:len(l1)]
print(sub_l1)
print("Sum of Last 4 Element of main list: ",sum(sub_l1))
print("-----------")


#2 Remove the items from the list located at Second and fisth Position
l1.remove(l1[1])
l1.remove(l1[4])
print("After removing 2nd and 5 item: ", l1)
print("-----------")

#3 print the diff btn smllest and highet number of the list
max = (max(l1))
min = (min(l1))
print("Max :",max,"Min :",min)
diff = max - min
print("Difference : ",diff)
print("-----------")


#4 append a new Element in A List which is half of the item located in third pos 
new_ele = l1[3]/2
l1.append(new_ele)
print(l1)
print("-----------")



#5 Print Sum Of 1st 10 Even numbers
n = [1,2,3,4,5,6,7,8,9,10,11]
limit = 10


#6 Accept 2 val S and N Print suare of first N numbets Starting from S

#7 Reverse the accepted string

#8 Accept sentence from user and count the vowels 

#9Remove Duplicates From List

#Reverse the list