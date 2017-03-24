Input_list = input('Enter an array of integers: ')
List_of_integer = [x   for x in Input_list if x % 2 != 0] #The generator list, which finds odd elements in "Input" list and mapping them in a new list
if  not List_of_integer:
    print ('Your array is empty.\nTry again')
else:
    Summ_list_of_integer = sum(List_of_integer) * Input_list[-1]           #Calculations elements

print (u"Result is: {}".format(Summ_list_of_integer))