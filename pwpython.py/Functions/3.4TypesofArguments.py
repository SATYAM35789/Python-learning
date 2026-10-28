# Arbitary arguments :- Python allow us to pass variable length arguments. The arguments here are pass as Tuple.
#1
def addAllNumber(*args):
    sum=0
    for i in args:
        sum+=i
    return sum
output = addAllNumber(1,3,5,6,4,)
print("The sum is:",output)