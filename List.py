this_List = [2,3,98,0,4,2,8,74]
this_List1 = [345,987,765,456,123]
print(this_List)
print(len(this_List))
print(type(this_List))
print(this_List[-4]) #Negative Indexing - prints the last item
print(this_List[1:5]) # prints range of indexes starts at 1 ends at 5 not included
print(this_List[:5]) 
print(this_List[3:])
print(this_List[-6:-1]) # prints range of items in negative order starts at -6 end at -1 not included
if 98 in this_List: # Use in keyword to check if specified item is in the list
    print("yes")

this_List[2] = 48 # replace the item at specified index
this_List[1:4] = [5,76,54,65]
this_List.insert(3,87) # Inserts a new list item at a specified index without replacing any of the existing values
this_List.append(360) # adds a new item at the end of the list
this_List.extend(this_List1) # 
print(len(this_List))
print(this_List)


