import customer_data
import random
import json


# # print("hello, world")

# # greeting = "Hello, World!"
# # age = 23
# # pi = 3.14

# # print(age)
# # print(greeting)
# # print(pi)

# # age = 3.14
# # print(age)

# name = input("What is your name?")
# age = int(input("What is your age?"))

# # print("Hello, " + name)

# # print("Hello, {}".format(name))
# print(f"Hello, {name}")
# # print(f"Next year you will be {age + 1} years old")


# if age < 3:
#     print("you are a baby")
# elif age < 19:
#     print("you are a child")
# else:
#     print("you are an adult")
# # print("good luck")
    
# # loops
# number = 5

# while number != 10:
#     number = int(input("please type '10':"))

# print("thank you for typing '10'")


# for num in range(1, 51, 2):
#     print(f"the number is {num}")

# # functions
# def greet(name):
#     print(f"hello, {name}")

# greet("Michael")
# greet("Bob")

# def celsius_to_fahrenheit(degrees_celsius):
#     degrees_fahrenheit = degrees_celsius * 1.8 + 32
#     return degrees_fahrenheit

# print(celsius_to_fahrenheit(0))
# print(celsius_to_fahrenheit(30)) 
# print(celsius_to_fahrenheit(100))


# # classes
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def greet(self):
#         print(f"Hello, {self.name}")

# alice = Person("Alice", 25)
# alice.greet()


# # lists
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# count = len(numbers)
# print(f"There are {count} numbers in the list")
# numbers[5] = "Hi!"

# copy = numbers[:]
# print(copy) # copy the list


# fifth_element = numbers[4]
# print(fifth_element)

# all_but_first = numbers[1:]
# print(all_but_first)

# first_only = numbers[0:1]
# print(first_only)

# odds = numbers[0::2]
# print(odds)

# for num in numbers:
#     print(f"{num} squared is: {num * num}")



# modules
# new_customer = customer_data.get_new_customer_info()
# customer_data.customers[new_customer[0]] = new_customer[1]

# for key, value in  customer_data.customers.items():
#     print(f"{key} is {value} years old")

# numbers = []

# for i in range(20):
#     new_num = random.randint(0, 100)
#     numbers.append(new_num)
    
# print(numbers)
# numbers.sort()
# print(numbers)

# movies_file = open("movies.json")

# movies_file.close()

# with open("movies.json") as movies_file:
#     count = 0
#     for line in movies_file:
#         print(f"#{count}: {line}", end = "") # = "" means remove the extra like that print inserts
#         count += 1 ## count number of lines
#     print(f"There were {count} lines in the file")

#     content = movies_file.read() # reads all of the data from the file into a string
#     print(content) 


# print("file has been closed")

with open("movies.json") as movies_file:
    content = movies_file.read() 
    data = json.loads(content)
    for movie in data:
        print(movie["name"])  # prints all the titles

# print(data) # prints all the data

line = "this is a line of text"
normal_flows = ["here", "are", "some", "words", "to", "search", "for", "text"]

for flow in normal_flows:
    is_in_line = flow in line
    print(f"{flow} is in line? {is_in_line}")

aggregated_result = any(flow in line for flow in normal_flows)
print(aggregated_result)

if not any(flow in line for flow in normal_flows):
    print("none of the words was found in the line")
else:
    print("at least one of the words was found in the line")
