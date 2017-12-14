mylist=[1,2,4,5,6,7,9,32,54,-88,-7]
mylist2=["frank","newbe","conming","xbnhk"]
def count_odd(mylist):
    odd=0
    for i in mylist:
        if i%2 == 1:
            odd += 1
    print(odd)
            
            


def sum_even(mylist):
    sumeven=0
    for i in mylist:
        if i%2==0:
            sumeven += i
    print(sumeven)
            
    
def sum_negative(mylist):
    negasum=0
    for i in mylist:
        if i < 0:
            negasum += i
    print(negasum)
    
def countword5(mylist2):
    numword5=0
    for i in mylist2:
        if len(i)==5:
            numword5 += 1
    print(numword5)


            
 
    

count_odd(mylist)
sum_even(mylist)
sum_negative(mylist)
countword5(mylist2)
sne(mylist)
