########################################################################################################################
#
# a = 2
# b = 2
# c = 1
#
# if (a+b) > (a+c) and (a+b) > (b+c):
#     print u'Max summ is: a + b =', (a+b)
# elif (a+c) > (a+b) and (a+c) > (b+c):
#     print u'Max summ is: a + b =', (a+c)
# elif (b+c) > (a+b) and (b+c) > (a+c):
#     print u'Max summ is: a + c =', (b+c)
# else:
#     print 'Error, integers have the same value!\nChange the input data and try again.'
#
# print max(a+b,a+c,b+c)
#
########################################################################################################################
#
# price_for_1kg_of_sweets = 100000
# for elem in range(1,11):
#     print u'The price for {0} kg is:{1} BYR'.format(elem, elem * price_for_1kg_of_sweets)
#
########################################################################################################################
#
# price_for_1kg_of_sweets = 100000
# finish = 2
# step = 0.2
# current = 1.2
#
# while current <= finish:
#     print u'The price for {0} kg is: {1} BYR'.format((current), (current * price_for_1kg_of_sweets))
#     current += step
#
########################################################################################################################
#
# l = [1,2,55,102,-4,42]
#
# for x in l:
#     if len((str(x))) < 3:
#         if x == 42:
#             print (u'The Answer to the Ultimate Question of Life, the Universe, and Everything')
#             break
#         else:
#             print x
#
########################################################################################################################
#
# Input_list = range(1000)
# List_of_integer = [x   for x in Input_list if x % 13 != 0]
# for x in Input_list:
#     if x % 13 != 0:
#         continue
#     print x
#
########################################################################################################################
#
# import sys
#
# if __name__ == "__main__":
#      numerals = sys.argv[1:] # first arg is numbers
#      l = []
#      for s in numerals:
#          number = int(s)
#          l.append(number)
# print u'The sum of the integers is:',sum(l)
#
########################################################################################################################
#
# def summ_of_sweets(weight_in_kg, cost_1kg):
#     price = weight_in_kg * cost_1kg
#     return round(price,1)
#
#
# print summ_of_sweets(2, 123500.000)
#
########################################################################################################################
#
# import sys
#
# # def sum_of_int(*args):
# #     return sum(args)
# #
# # print sum_of_int(1,2,3,5)
#
# def my_func(*args):
#     my_sum = 0
#     for i in args:
#         my_sum += i
#     return my_sum
#
# print my_func(1,2,3,4,5,6,7)
#
########################################################################################################################
#
# def sort_numbers(input_list):
#     for elem in input_list:
#         if elem % 2 == 0:
#             print u'An even number: {}'.format(elem)
#         else:
#             print u'An odd number: {}'.format(elem)
#
# l = range(100)
# print sort_numbers(l)
#
########################################################################################################################
#
# def list_of_string(sentence):
#     return sentence.split()
#
# sentence = "What art thou that usurp'st this time of night \
# Together with that fair and warlike form \
# In which the majesty of buried Denmark \
# Did sometimes march? By heaven I charge thee speak!"
#
# print list_of_string(sentence)
#
########################################################################################################################











########################################################################################################################
#
# def to_str(integers):
#     list_1 = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eighth", 9: "nine", 0: "zero"}
#     list_new = []
#
#     for elem in str(integers):
#         list_new.append(list_1.get(int(elem)))
#     return ' '.join(list_new)
#
#
# print to_str(5906)


