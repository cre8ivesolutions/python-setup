print("Hello from inside a file!")

def hello():
    print ("hello user") 

def pack(one, two, three):
    return (one, two, three)

def eat_lunch(breakfast, *lunch):
    if breakfast == "":
        print ("My lunchbox is empty!")
    else:
        print ("First I eat " + breakfast + ". Next I eat " + lunch)
    
print(pack(1, 2, 3))