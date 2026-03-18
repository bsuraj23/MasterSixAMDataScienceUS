import copy

#Ex1: Shallow copy
# list1 = [1, 2, 3,4]
# list2 = list1[:]
# list1[0]=30
# print(list1,list2) #[30, 2, 3, 4] [1, 2, 3, 4]

#Ex2: deepcopy changes will affect only one copy
list1=[["Name","Grade"],["sam",2]]
#list2=copy.deepcopy(list1) 
list2=copy.copy(list1) #SHALLOW COPY
list1[1][1]=4
print(list1,list2) #[['Name', 'Grade'], ['sam', 4]] [['Name', 'Grade'], ['sam', 2]]

# Ex3: Copy using list() function
# list3 = list(list1)
# print(list3)

# Ex4: Copy using dictionary
dict1 = {"class":4, "teacher": ["Ms.Vlsyuk","Ms.Heller"]}
dict2=copy.deepcopy(dict1)
#dict2=dict1.copy() #SHALLOW COPY
dict2["teacher"].append("sonal")
print(dict1,dict2)


# Ex5: Copy using append in a loop
# list5 = []
# for item in list1:
#     list5.append(item)
# print(list5)

# Ex6: Copy using list comprehension
# list6 = [x for x in list1]
# print(list6)

# Ex7: Copy using extend()
# list7 = []
# list7.extend(list1)
# print(list7)