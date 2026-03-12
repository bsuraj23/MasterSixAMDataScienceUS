#CIt is also unordered, unchangeable, unindexed like Set 
# but its immutable

#definimng a frozen set -using frozenset() constructor
Frset=frozenset({"Google","Apple","Microsoft"})
print(Frset)

#Immutable so cannot add or remove items
Frset_dup=Frset.copy()
print(Frset_dup) #Makes a copy of set
# Can use Union, Intersection, Difference, symmetric difference methods like in Set
Frset1=frozenset({"GeminI","Sora","ChatGPT","Microsoft"})
ResSet=Frset | Frset1
print("New Set:",ResSet)

ResSet=Frset & Frset1
print("New Set:",ResSet)

ResSet=Frset.difference(Frset1)
print("New Set:",ResSet)

ResSet=Frset.symmetric_difference(Frset1)
print("New Set:",ResSet)