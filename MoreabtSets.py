#Sets are unordered - Difficult to say in which order items are stored.
#No fixed positiuon or index

Exset={1,3,5,7,9,False, True,"Hi",2,4,6,8,0,1,"Python",(2,3,5,7,9),False,'k',34.09,8.99,1234.09898}
print(Exset)

#Items in set are Unchangeable but can add new items to the set.
#Items can be int, string, boolean, list, tuple, dictionary

set1={11,13,15,17,19}
set2={21,"Mac",True}

#Use add to add an item to set
set1.add(51)
print("New set =",set1)

#Use update() to add a different set

set1.update(set2)
print("New set after adding tuple =",set1)

set3=["Rose","Lavender","Tulips"]

set1.update(set3)
print("New set after adding a list to dict=",set1)

set2=(20,40,60)
set1.update(set2)
set3={"Flavor":"Vanilla","Cup size":"Medium","Price":4.69}
set1.update(set3)
print("New set after adding a list to dict=",set1)


set2={1,3,5,7,9,"Sunday"}
#Remove an item
set1.remove(20)
set1.discard("Rose")
print(set1)
set1.pop()
print(set1) #removes a random item
set2.clear() #clears the set and print empty set
print(set2)
#del Exset #removes the set completely
#print(Exset) #Throws an error, Set doesn't exist/defined

#Joining sets
Set1={1,3,5,7,9,False, True,"Hello"}
Set2={2,4,7,9,"Hi",True,"Thursday"}

#Union or | or update() - Joins 2 sets
Unionset = Set1 | Set2
print("Unuon of 2 sets",Unionset)

Unionset=Set1.union(Exset,set1)

#Intersection :return newset with common items, Can use &

Int_Set=Set1 & Set2 # Set1.intersection(Set2)
print("Intersection of set:",Int_Set)

#difference() returns a new set that contains items from 1st set that are not in set2
Set1={"Sunday","Monday","May","June"}
Set2={"July","January","Monday","October"}
Diff_set=Set1.difference(Set2)
print("Difference of set is:",Diff_set)
Diff_set=Set2 - Set1
print("Difference of set is:",Diff_set)

#returns set avoiding common item Use ^ symbol too
Sym_diff=Set1.symmetric_difference(Set2)
print("DSymmetric Difference of set is:",Sym_diff)

#can use methods issubset() and issuperset()

#Unindexed- Throws an error if trying to retrieve an element from set using index

#for x in Sym_diff:
 #   print(Sym_diff[i])
