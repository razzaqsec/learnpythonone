print("Dictionaries")

# Dictionaries   "43"


studentinfo={
    "usha":{
        "location":"Laksam",
        "study":"14",
        "subject":"zoology",
        "roll":"09",
        "number":"0154051175"

    },
    "talha":{
        "location":"Comilla",
        "study":"01",
        "subject":"BAngla English Math",
        "roll":"78",
        "number":"01687901319"
    },
    "year":"2024"
}

print(studentinfo["usha"])

print(studentinfo["usha"]["subject"])

print(studentinfo["talha"])

   # 44     p  y   t   h  o  n   dictionaries ACCESS: 

print(studentinfo.get("usha"))

print(studentinfo.keys())   


z=studentinfo.keys()
print(z)

print(studentinfo.values())

#  Dictionaries Change ITEM   :           /   45   /    update methoed 

studentinfo["year"]=2003
print(studentinfo)
print(studentinfo["year"])


'                   onno niyom eita /// update methode diye change         '


#           studentinfo.update({"usha":"Apple Lover"})
#           print(studentinfo["usha"])








#     // 46 //   Add item on dictionaries   //   46   //
'Add ba remove korte parbo amra '
# add item   
'             Amra Add korbo kivabe sheitai ekhane dekhalam           haha lol enjoyt '
fatu = {
    "brand":"apple",
    "model":"iPhone",
    "year":"2024",
}
fatu["colour"]="pink"
print(fatu)



'example 1  '
#  studentinfo.pop("usha")        -     # ekhane "usha" remove hoye gese. POP diye nirdisto jekeono valu k remove kora zay..
#  print(studentinfo)                  


#                   popitem er mardhome by diffelt sesher value ta bad dewa zay /..

#ex 1             1. popitem  /  2. .del    //  3.   .clear





#          studentinfo.clear()
#          print(studentinfo) 


# 47 //////////        4    7       ////////////

for x in studentinfo:          # keys gula ber korar niyom 
    print(x)

print("shov keys output kore dekhar niyom  example # 2 ")

for u in studentinfo.keys():
    print(u)


 # keys er vitor value gula show korbe sudhu 


for a in studentinfo.values():    

    print(a)

# keys & value 2 ta eksathe dekhte caile ===== ""items""  dite hobe 

for item in studentinfo.items():
    print(item)


# Copy dictinories 

print(studentinfo)

#Example 1 

print("Example 1 ")
mydict=studentinfo.copy()
print(mydict)

#example 2 

x=dict(studentinfo)
print(x)

