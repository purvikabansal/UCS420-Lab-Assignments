#5.1
nums=[10,30,89,45,12]
print("largest number ",max(nums))
print("smallest number ",min(nums))

#5.2
dict={"name":"Reema","branch":"cse","cgpa":10}
key=input("enter the key u want to find ")
if key in dict:
  print("The value of the key is:",dict[key])
else:
 print("key not found in dictionary")

#5.3
nums=[42,15,6,9,4]
print("Ascending order ",sorted(nums))
print("Descending order ",sorted(nums,reverse=True))

#5.4
d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}
merged = {**d1, **d2}
print("Merged dictionary ", merged)


