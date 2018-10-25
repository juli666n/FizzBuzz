for x in range (1,100):
    fizz = x%3
    buzz = x%5
    if fizz==0 and buzz==0:
        print ("fizzbuzz")
    elif buzz==0:
        print("buzz")
    elif fizz==0:
        print ("fizz")
    elif fizz!=0 and buzz!=0:
        print (x)
