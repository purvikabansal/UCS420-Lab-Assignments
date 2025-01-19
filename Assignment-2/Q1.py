#1. Create a List L that is defined as= [10, 20, 30, 40, 50, 60, 70, 80].

#i. WAP to add 200 and 300 to L.
L=[10,20,30,40,50,60,70,80]

L.append(200)
L.append(300)
print("the list after adding 200 & 300")
print(L)

#ii. WAP to remove 10 and 30 from L.
L.remove(10)
L.remove(30)
print("the list after removal of 20 and 30 is ")
print(L)

#iii. WAP to sort L in ascending order.
L.sort()
print("The sorted list(ascending order):")
print(L)

#iv. WAP to sort L in descending order.
L.reverse()
print("List after sorting in descending order:")
print(L)
