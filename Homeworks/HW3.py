def prime_first(x):
   flag = True
   if x > 0 and x < 500:
       if x == 2:
           print(x)

       elif x>2:
           for i in range (2,x):
               if x % i == 0:
                   flag = False

           if flag == True:
               print(x)

def prime_second(x):
    flag = True
    if x > 500 and x < 1000:
        for i in range(2,x):
            if x % i == 0:
                flag = False
        if flag == True:
            print(x)




for i in range(0,1000):
    if i < 500:
        prime_first(i)
    else:
        prime_second(i)