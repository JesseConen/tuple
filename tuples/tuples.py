#creating tuples
student_Details = ("Jesse", 17, "Netherlands")

#Packing
address = (224, "Langford Street", "Netherlands")

#unpacking
housenumber, streetname, country = address

print("House Number is: ", housenumber)
print("StreetName is: ", streetname)
print("Country is: ", country)

#looping in tuples
for i in address:
    print(i, end=" ")

#tuple can also be created without parenthesis
my_tuple = 3, 4.6,"dog"
print(my_tuple)

#Nested tuples  - tuple inside tuple

n_tuple = ("mouse", [1,2,3], [4,5,6])

#for nested tuples we need indez number to acces the value
print(n_tuple[0][3]) #acces "s"

#acces "6"
print(n_tuple[2][2])

#Slicing - cutting down tuple into shorter tuple
my_tuple = (1,2,3,4,5,6,7,8,9,10)
print(my_tuple[1:4]) #start_index:end_index (end_index is exclusive)

#First 2 items
print(my_tuple[7:])

#negeative index number
print(my_tuple[:-7])


print(my_tuple[:]) #accessing all the numbers in the tuple




