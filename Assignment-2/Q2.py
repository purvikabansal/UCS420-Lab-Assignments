#2. Create a tuple of marks scored as scores = (45, 89.5, 76, 45.4, 89, 92, 58, 45) and
scores=(45, 89.5, 76, 45.4, 89, 92, 58, 45)

#i. Identify the highest score and its index in the tuple.
highest=max(scores)
print("the highest score in scores :",highest)
index1=scores.index(highest)
print("The index of highest score is: ",index1)

#ii. Find the lowest score and count how many times it appears.
lowest=min(scores)
print("The lowest score is: ",lowest)
count_a=scores.count(lowest)
print("the count of lowest score in scores :",count_a)

#iii. Reverse the tuple and return it as a list.
reversed=list(reversed(scores))
print("Tupple after reversing",reversed)

#iv. Check if a specific score ‘76’ (input by the user) is present in the tuple and
#print its first occurrence index, or a message saying it’s not present.
value=int(input("Enter the value of integer"))
if value in scores:
    index_b=scores.index(value)
    print("the first occurence index:",index_b)   
else:
    print("Integer not found")
