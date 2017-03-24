import datetime
import random
import argparse


parser = argparse.ArgumentParser(description='Sort some integers in ascending by bubble and Python sort method .'
                                             '\nTime tests are compared and displayed at the end of script')
parser.add_argument('-int', metavar='integer', type=int, action='store',
                   help='input integer for the sort')
parser.add_argument('-numb',  metavar='number', type=int, action='store',
                   help='enter the number of tests')
args = parser.parse_args()


def func_random_list(amount_of_numbers):
    mylist = random.sample(xrange(1,50001), amount_of_numbers)
    return mylist

#print random_list(10000)

def Bubble_Sort(list_of_int):
    #print(u"initial sample: {}").format(sample)
    length = len(list_of_int)
    for i in range(length-1):
        for j in range(length-1-i):
            if (list_of_int[j] > list_of_int[j+1]):
                list_of_int[j], list_of_int[j+1] = list_of_int[j+1], list_of_int[j]
    return list_of_int
                #print ('Processes: {}'.format(sample))
    #print (u"sorted list: {}").format(sample)


def test_time(input_numbers, number_of_tests):
    count = 1
    Bubble_timeList = []
    Python_timeList = []
    while count <= number_of_tests:

        int_list = func_random_list(input_numbers)
        start = datetime.datetime.now()
        print u'\nTest:{}\n'.format(count)
        Bubble_Sort(int_list)
        #print (u'Sorted list: {}').format(int_list)
        finish = datetime.datetime.now()
        print u'The test time of Bubble sort is: {0}'.format(finish-start)
        Bubble_timeList.append(finish-start)

        int_list = func_random_list(input_numbers)
        start = datetime.datetime.now()
        int_list.sort()
        finish = datetime.datetime.now()
        print u'The test time of Python sort is: {0}\n'.format(finish-start)
        Python_timeList.append(finish-start)

        count += 1
    
    print u'Total time of Bubble sort     : {}'.format(sum(Bubble_timeList, datetime.timedelta()))
    print u'Max time of Bubble sort       : {}'.format(max(Bubble_timeList))
    print u'Min time of Bubble sort       : {}'.format(min(Bubble_timeList))
    print u'An average time of Bubble sort: {}\n'.format((sum(Bubble_timeList, datetime.timedelta()) -
                                            (max(Bubble_timeList) + (min(Bubble_timeList)))) / (number_of_tests - 2))

    print u'Total time of Python sort     : {}'.format(sum(Python_timeList, datetime.timedelta()))
    print u'Max time of Python sort       : {}'.format(max(Python_timeList))
    print u'Min time of Python sort       : {}'.format(min(Python_timeList))
    print u'An average time of Python sort: {}\n'.format((sum(Python_timeList, datetime.timedelta()) -
                                            (max(Python_timeList) + (min(Python_timeList)))) / (number_of_tests - 2))

if __name__ == "__main__":
    test_time(args.int, args.numb)




