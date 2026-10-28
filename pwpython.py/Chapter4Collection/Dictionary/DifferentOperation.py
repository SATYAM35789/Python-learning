phone ={
    "john":987897,
    "ria":987898,
    "joy":9878987
}
print(" Creating a dic:",phone)
 # access in Dictiony
print(phone["joy"])
# Using get() to access
print(phone.get("joy"))
# Want to print all Key in dic
print(phone.keys())

# Update Values in Dic
phone["john"]= 9877987
print("after Updation:",phone)

# Add an element in a dic
phone["kia"]=768788
print(phone)

# Add a another dic
more_phpne = {
     "sia":56857908, 
     "tia":868987,"mia":886596
}
print("Another dic :",more_phpne)

phone.update(more_phpne)
print( "adding two dic:" ,phone)

# Remove element from a dictiony
phone.pop("tia")
phone.pop( "sia")
print( "Remove using pop", phone)

phone.popitem()  # Remove the last item
print( "Remove last element using popitem", phone)

# phone.clear()  # This will empty the dic
# print( "Clear the all element in dic:", phone)



