import random
import datetime 

placeList = []
dressUpList = []
place1 = input("Enter a place. ")
place2 = input("Enter another place. ")
place3 = input("Enter another place. ")
dressUp1 = input("Enter a noun. ")
dressUp2 = input("Enter another noun. ")
dressUp3 = input("Enter another noun. ")
x = datetime.datetime.now()
y = x.strftime("%A")
name = input("Enter the name of a person. ")
job = input("Enter a past tense verb. ")
income = input("Enter a number.")
arrest = input("Enter another past-tense verb. ")
placeList.append(place1)
placeList.append(place2)
placeList.append(place3)
dressUpList.append(dressUp1)
dressUpList.append(dressUp2)
dressUpList.append(dressUp3)



print(f"On one {y}, a man named {name} went to {placeList[random.randint(0,2)]}. He's retired now, but he {job} for a living, and made ${income} a year. Now, in his freetime, he likes to dress up as a {dressUpList[random.randint(0,2)]}. He likes to go to {dressUpList[random.randint(0,2)]} coneventions, which are always hosted in {placeList[random.randint(0,2)]} for some reason. Last year, at one of the conventions, he was arrested because he {arrest} another convestion goer becuase they were dressed as a {dressUpList[random.randint(0,2)]}.")

