# Arbitary arguments
# Keyword arguments or Key value argment def name(**kwargs)
def studentInfo(**kwargs):
    for x,y in kwargs.items():
        print(x ,"is",y)
studentInfo(Name="Urvi",age = 22, city= "Delhi")
studentInfo(Name="Satyam",age = 20, city= "Uttar Pardesh")