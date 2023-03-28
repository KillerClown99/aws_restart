myString= "This is a string"
print(myString)
print(type(myString))
print(myString + " is of data type " + str(type(myString)))

firstString =  "Water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)

name = input("What is your name ? " )
print(name)

color = input("What is your favourite color ? " )
print(color)

animal = input("What is your favourite animal ? " )
print(animal)

print(name,  "you like a ",color,animal)

#another way
print("{} you like {} {}!" .format(name,color,animal))
 
