print("Hello from inside a file!")

def hello():
    print ("hello user") 

def pack(one, two, three):
    return (one, two, three)

def eat_lunch(foods):
    if len(foods) == 0:
        print ("My lunchbox is empty!")
    else:
       for i in range(len(my_lst)):
       if i == 0:
        print(f"First I eat {foods[0]}")
      else:
        print(f"Next I eat {foods[i]}")
    
hello()
print(pack(1, 2, 3))
eat_lunch(["eggs", "pizza"])