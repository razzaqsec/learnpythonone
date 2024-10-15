# 30 Python tuple 

NewTuple=(1,2,3,"usha","talha") 

print(type(NewTuple))

# negative indexing 

mm=(1,2,3,"usha","talha")

print(mm[-1])

print(mm[-2])

# Range of Indexes :

print(mm[3:5])

# ex 2 

bb = (1,2,3,4,5,"Ayesha","Fatema","Talha")

print(bb[5:8])

print(bb[0:5])

print(bb[0:8])



# Update TupLes :

name = ("rahim","Abir","usha","amir","Siddiq","Aashraf")
b=list(name)
b.append("mohammod")
name=tuple(b)
print(name )

# ex 2 

nam= ("rim","reha","rumman","hiya")
a=list(nam)
a.append("rahma")
nam=tuple(a)
print(nam)

# N:B = Ekane tuple k List e convert kore name Add korsi then aabr tuole e convert korsi....


# Ex 3 

fruits=("apple","orange","banana","kiwi")
x = list(fruits)
x.append("cherry")
fruits=tuple(x)
print(x)
      
      # ex 4

web=("facebook","instagram","google","X","apple0",)

brand = list(web)
brand.append("samsung")
web=tuple(brand)
print(brand)

# Unpack Tuples :

sim= ("gp","banglalink","robi","airtel","teletalk")
a,b,c,d,e=sim
print(a)

# ex 2  

(*a,b)=sim
print(b)


(a,*b,e)=sim
print(b)

 # ex 3 

friend = ("usah","fahim","hanif","jamshed","badsha","siddik")
a,b,c,d,e,f= friend

(*a,)=friend

print(a)

# ex 4 

browser=("opera","uc","chorme","Safari","internet","mozila")
a,b,c,d,e,f= browser

(a,*b)=browser
print(a)
print(*b)

#  Loop tuples ::: _-===
#
for x in range(len(browser)):
        print(x)

for i in browser:
        print(i)

        i = 0 
        while i < len(browser):
                print(browser[i])
                i+=1


            # ex 3 

mm = ("riya","kiya","miya","lol","momeu")

i = 0 
while i < len(mm):
        print(mm[i])

        i+=1



# Loop tuple exercise :----

coin=("momo","saga","milan","oreo","coco")

i=0
while i < len(coin):
        print(coin[i])
        i+=1 




#        34   Join Tuples 


#               1. count   2. index

name = ("usha","talha","ayedhs","fatema","lo0ve")

x=name.index("usha")
print(x)

y=name.index("talha")
print(y)

name.count("fatema")
print(name.count("fatema"))



# ex 2 

brand= ("samsung","apple","huawei","mi","oppo","realme","oneplus")

print(brand.index("apple"))

print(brand.index("realme"))

print(brand.count("oneplus"))



# end 36 porjonto 