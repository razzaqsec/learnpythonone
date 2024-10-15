name =["usha","Talha","Fatema","Ayesha"]

name[0]= "Abdur Razzaq"

print(name)


# 18 start __ PYTHON LISTS --


li=[1,2,34,5,6,67]
print(type(li))

print(li)

li[2]=9
print(li)

#ex 2

bom=["sumi","mina","hani","ruhi","pori"]



bom[1]="oyse"

print(bom)

# change list item 

# Access List Items

usha=["Facebook","Youtube","Google","Instagram"]

print(usha[0])
usha[0]="Book"
print(usha)


# Add listed Items 

# there have 2 methoeds                1- append 2-insert

usha.append(8801540511775)

print(usha)

# insert 

usha.insert(0, "Apple")
print(usha)

# 21 number class

#Remove class items 

yo=["Usha","Ayesha","Fatema","Talha"]

yo.remove("Usha")
print(yo)

#POP

yo.pop()
print(yo)

# del word

del yo[0]
print(yo)

# clear all 

yo.clear()
print(yo)


# practice 18 to 21 

bow=["sumi","mina","hani","ruhi","pori"]

bow[0]="Prince"
print(bow)

# add list items -------------- append 

bow.append("BYE")
print(bow)

# insert ( je kono  zaygay customized kora zabe nijer iccha moto )

bow.insert(1,"sonya")
print(bow)
# another name replace , trick  
bow[2]="toya"
print(bow)


# remove listed itsem 

bow.remove("sonya")
print(bow)

# pop __----- sobar sesh er ta automatic remove hoiya zaiybo 

bow.pop()
print(bow)

# del --- nirdisto kono list dlt kora

del bow[0]
print(bow)

#clear ----- remove all 

bow.clear()
print(bow)


# 22 LOOP LISTS 


LoopList=["popy","samia","maisha","faria","sumaiya","ruhi","sam","toma"]

for kick in LoopList:
    print(kick)

for i in range(len(LoopList)):
    print(i)

# ex 2 

bb = ["btc","wif","eth","ton","saga","high","crv","solo","saga","not"]

for c in bb:
    print(c)

for m in range(len(bb)):
    print(m)



# W H I L E  

x = 0 
while x < len(bb) :
    print(bb[x])
    x = x+1

while x < len(bb):
    print(bb[x])
    

# EXAMPLE @

my= ["lal","nil","sada","kalo","sobuj"] 
for rong in my:
    print(rong)


for i in range(len(my)):
    print(i)

# W H I L E 

z= 0
while z<len(my):
    print(my[z])
    z=z+1


# 23 !!!! List Comprehension .

mom= [1,2,3,4,5]

db=[i*2 for i in mom]

print(db)

# ex 2 

num=[1,2,3,4,5,6,7,8,9]

double=[i+10 for i in num] 

print(double)

# - 

biyog = [i-1 for i in num]
print(biyog)


# / 
vag=[i/2 for i in num]
print(vag)

# 24 ... Sort Lists 

number=[8,1,4,2,9,0,3,5,7,6]
number.sort()
print(number)

on=["b","d","a","e","c"]
on.sort()
print(on)

# Reverse --------------

dj = [1,2,3,4,5,6,7,8,9]
dj.sort(reverse=True)
print(dj)



ney=['a', 'b', 'c', 'd', 'e']

ney.sort(reverse=True)
print(ney)

# Copy lists 

usha =[ 1,2,3,4,5,6,7,8,9]

fahim=usha.copy()
print(fahim)
print(usha)

# copy lists is very easy haha HAHAHA lol Enjoy my day 31 Aug 2024

# 25 no going Alhamdulillah .... :') 


# 26 Join Two Lists 

# its very Simple 

usha=[1,2,3,4]
talha=[5,6,7,8]

fatema= usha + talha 

print(fatema)


 # very funny HAHAHAHAHA

fruits = ['apple', 'banana', 'cherry']
newlist = [x for x in fruits if x == 'banana']
print(newlist)
