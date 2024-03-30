
# dictionaries
customers = {
    "Alice": 32,
    "Bob": 25,
    "Carol": 30
}

# customers["Eve"] = 22
# customers["Malory"] = 50

# customers["Alice"] = 33 # change value
# del customers["Malory"]

# print(customers)

# if "Alice" in customers:
#     print("Alice is in the customers dictionary")

# if "Malory" in customers:
#     print("Malory is in the customers dictionary")    


# for key in customers:
#     print(key)

# for value in customers.values():
#     print(value)  

# # tuple
def get_new_customer_info():
    name = input("Enter the name: ")
    age = int(input("Enter the age: "))
    return (name, age)

##when you import the code fromn another module, it runs all the code (including print statements). Here is how to avoid that using dundername:

if __name__ == '__main__':
    print("inside of the customer data module")