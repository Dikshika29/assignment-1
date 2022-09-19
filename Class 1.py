#Create a List
mylist=["data" ,"details", "access"]
print(mylist)
mylist1=(4556,769.98,"data")
print(mylist1)
output:
['data', 'details', 'access']
(4556, 769.98, 'data')

#Indexing Number 
mylist1=(4556,769.98,"data")
print(mylist1[-2])
mylist=["data" ,"details", "access"]
print(mylist[0])
output:
769.98
data

#update
mylist1=[4556,769.98,"data"]
mylist1[1]=False
print(mylist1)
output:
[4556, False, 'data']

#append 
mylist1.append("dix")
print(mylist1)
output:
[4556, False, 'data', 'dix']

#insert 
mylist1.insert(1,2000)
mylist1.insert(2,46)
mylist1.insert(1,"dix")
print(mylist1)
outpit:
[200, 'dix', 2000, 46, 2000, 46, 2000]

#Create a tuple
tuple=("dell","Asus","HP",27,45.77)
print(tuple)
output:
('dell', 'Asus', 'HP', 27, 45.77)

#Delete
tuple=("dell","Asus","HP",27,45.77)
del tuple
print(tuple)
output:
<class 'tuple'>

#Create a Dictionary
Dict={
    "Admin":"Dikshika",
     "Password":"Dikshika29",
     "OS":"windows",
     "Ram":"128GB"
     }
print(Dict["Admin"])
print(Dict)
output:
Dikshika
{'Admin': 'Dikshika', 'Password': 'Dikshika29', 'OS': 'windows', 'Ram': '128GB'}

#update
Dict={
    "Admin":"Dikshika",
     "Password":"Dikshika29",
     "OS":"windows",
     "Ram":"128GB"
     }
Dict["model"]=3456
print(Dict)
Dict["Password"]="Dix29"
print(Dict)
output:
{'Admin': 'Dikshika', 'Password': 'Dikshika29', 'OS': 'windows', 'Ram': '128GB', 'model': 3456}
{'Admin': 'Dikshika', 'Password': 'Dix29', 'OS': 'windows', 'Ram': '128GB', 'model': 3456}

#Delete
del Dict["Ram"]
print(Dict)
output:
{'Admin': 'Dikshika', 'Password': 'Dikshika29', 'model': 3456}

#Create a Slicing
A="randomness"
print(A[0:6])
print(A[0])
print(A[6])
print(A[3:])
print(A[ :7])
print(A[-4:])
print(A[:-1])
print(A[4:-3])
print(A[0:100])
print(A[:])
print(A[-9:-3])
print(A[-8:4])
output:
random
r
n
domness
randomn
ness
randomnes
omn
randomness
randomness
andomn
nd

#step index
B="python"
print(B[1])
print(B[2])
print(B[1:5:3])
print(B[1:4:2])
output:
y
t
yo
yh

#negative step indexing
print(B[-1])
print(B[-5])
print(B[-2])
print(B[-1:-4:-2])
output:
n
y
o
nh

#Create a Set 
myset={"A","B","C",23456,45.6879,"A"}
print(myset)
print(len(myset))
output:
{23456, 'C', 'A', 45.6879, 'B'}
5

#Add
myset.add("tele")
print(myset)
output:
{23456, 'C', 'tele', 'A', 45.6879, 'B'}

#Frozen set
myfrozenset=frozenset(["d","a"])
print(myfrozenset)
output:
frozenset({'d', 'a'})

