### YOUR CODE FOR openLocks() FUNCTION GOES HERE ###
def openLocks(number_of_lockers,number_of_students):
    if number_of_lockers < 0 or number_of_students < 0 :
        return None
    if number_of_lockers == 0 or number_of_students == 0 :
        return 0
   
    else:
        return h(number_of_lockers,number_of_students)
    
def h(number_of_lockers,number_of_students):
    if number_of_lockers<=number_of_students:
        return c(a,number_of_lockers)
    else:
        return d

a=1
def c(a,number_of_lockers): 
    
    b=number_of_lockers
    cnt = 0 
    
    for i in range (a, b + 1): 
        j = 1; 
        while j * j <= i: 
            if j * j == i: 
                 cnt = cnt + 1
            j = j + 1
        i = i + 1
    return cnt 
   

def d(number_of_lockers,number_of_students):
    return loo
#### End OF MARKER





### YOUR CODE FOR mostTouchableLocker() FUNCTION GOES HERE ###
def mostTouchableLocker(number_of_lockers,number_of_students):
    if number_of_lockers < 0 or number_of_students < 0 :
        return None
    if number_of_lockers == 0 or number_of_students == 0 :
        return 0
    else:
        return coo(number_of_lockers,number_of_students)
        
def coo(number_of_lockers,number_of_students):
    a=[]
    for i in range(1,number_of_lockers+1):
        z=0
        for j in range(1,number_of_students+1):
            if i%j==0:
                z=z+1
        a.append(z)
    c=a
    x=0
    
    for i in c:
        if x<=i:
            x=i
    return c.index(x)+1

#### End OF MARKER


