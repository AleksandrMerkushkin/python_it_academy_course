#First solution
L = input(u"Please enter an array(list[]) of integer: ")
N = input(u"Enter a number N: ")
if N <= (len(L)-1): #Index counter
    print (u"N degrees in the array element with index N is: {}".format(L[N] ** N))
elif N > (len(L)-1):  #Index counter
    print (u"Ranged exceeded. N beyond the boundaries of the array: {}".format(-1))
else:
     print'Invalid value. Please try again.'

#Second solution
def fun_array(array, N):
    if N <= (len(array)-1):
        return array[N]**N
    elif N > (len(array)-1):
        return -1
    else:
        print'Invalid value. Please try again.'

#l = [1,2,3,4,5,6]
#print fun_array(l,100)