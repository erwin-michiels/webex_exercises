import json
file = open("groups.json")
groups_struc = json.load(file)

#exercise 1:
firstperson_firstgroup = groups_struc["groups"][0]["group"]["members"][0]["person_name"]
print("First person of first group is " + firstperson_firstgroup + ".")

#exercise 2:
print("")
print("List of all names and e-mail addresses:")
for i in groups_struc["groups"]:
    for j in i["group"]["members"]: 
        print(j["person_name"] , j["email"])

#exercise 3:
print("")
print("List of all names and e-mail addresses of group DEVASC_B:")
for i in groups_struc["groups"][1]["group"]["members"]:
    print(i["person_name"] , i["email"])

file.close()