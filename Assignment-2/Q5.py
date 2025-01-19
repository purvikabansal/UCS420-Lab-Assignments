#Write a program to rename a key city to a location in the following dicƟonary
dictionary={"name":"Kelly","age":25,"salary":8000,"city":"New York"}
if "city" in dictionary:
        dictionary["Location"] = dictionary.pop("city")
        print(f"Updated dictionary:{dictionary}")
else:
        print("Key not found in dictionary")


