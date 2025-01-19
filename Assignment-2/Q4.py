
#Consider the following two sets, A and B, represenƟng scores of two teams in mulƟple
#matches. A = {34, 56, 78, 90} and B = {78, 45, 90, 23}
A = {34, 56, 78, 90}
B = {78, 45, 90, 23}

# i. Find the unique scores achieved by both teams (union of sets).
union_a= A.union(B)
print("Unique scores are:", union_a)

# ii. IdenƟfy the scores that are common to both teams (intersecƟon of sets).
intersection_a= A.intersection(B)
print("Common scores of both teams are:", intersection_a)

# iii. Find the scores that are exclusive to each team (symmetric difference).
exclusive_a= A.symmetric_difference(B)
print("Exclusive scores are",exclusive_a)

# iv.Check if the scores of team A are a subset of team B, and if team B's scores are
#a superset of team A.
subset = A.issubset(B)
superset = B.issuperset(A)
print(subset)
print(superset)

#v. Remove a specific score X (input by the user) from set A if it exists. If not, print
#a message saying it is not present
score = int(input("Enter the score u want to remove "))
if score in A:
    A.remove(score)
else:
    print("Score not found")

