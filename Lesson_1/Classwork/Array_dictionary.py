#First solution
l = input('Enter your list: ')
L = list(set(l)) #Filtering duplicates in collections
print (u"List without duplicates: {}".format(L))

#Second solution
def filter_duplicates(l):
     F = list(set(l)) #Filtering duplicates in collections
     print (u"List without duplicates: {}".format(L))

#D = [123, 123, 222, 333, 444, 'asd', 'asd']
#print filter_duplicates(D)