def greet_user(name, greeting="Hello"):
   
    print(f"{greeting}, {name}!")

greet_user("Fitri")              
greet_user("Zayn", "Good morning") 


def sum_numbers(a, b):
    
    return a + b
result = sum_numbers(7, 13) 
print(result)               


fruits = ["apple", "banana", "cherry", "date"]
fruits.append("elderberry")
fruits.remove("banana")
fruits.insert(1, "blueberry")
fruits.sort()
print(fruits) 


for i in range(1, 11):
    if i == 7:
        break
    print(i)


for i in range(1, 11):
    if i % 3 == 0:
        continue
    print(i)



