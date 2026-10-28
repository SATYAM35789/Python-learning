# Given three arrays, we have to find common elements in three sorted lists using sets.
#  input: ar1=[1,5,5]
#         ar2=[3,3,4,5,6,7]
#         ar2=[8,7,6,55,5]
#  We use set so 1st list is converted into sets with help of typecasting
#  then we use insection_update(so we got the duplicates) join1 to 2 then 3
l1 = [1,2,2]
l2 = [1,2,2,3,4,5]
l3 = [1,4,5,9,8,7,2,2,]

# type cast
s1 = set(l1)
s2 = set(l2)
s3 = set(l3)

# join using intersection , help to get the  value in another set
# intersection_update will do in same set

s1s2 = s1.intersection(s2) # by this we got deplicate value in s1 and s2.
final_set = s1s2.intersection(s3)
final_set = list(final_set)
print(final_set)