#! /usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import urllib2
import xml.etree.ElementTree as ET
from datetime import datetime


def get_exchange(preferred_currency):
    URL = urllib2.urlopen('http://www.nbrb.by/Services/XmlExRates.aspx?ondate=12/20/2014')
    URL_string = URL.read()
    root = ET.fromstring(URL_string)
    for currency in root.findall('Currency'):
        Rate = currency.find('Rate').text
        CharCode = currency.find('CharCode').text
        for key_currency in {CharCode:Rate}:
            if key_currency == preferred_currency:
                return Rate


#print get_exchange('RUB')

def open_csv(csv_file):
    file_csv = open(csv_file)
    csv_reader = csv.reader(file_csv)
    new_csv = list(csv_reader)
    return new_csv

#print open_csv('car_stats.csv')

def fuel_total_cost(csv_file):
    Exchange_summ = 0
    Total_summ = 0
    for row, j in enumerate(csv_file):
        if row != 0 and j[0] != '':
            if j[5] != 'BYR':
                Exchange_summ += (int(j[3])) * int(get_exchange('RUB'))
            if (j[5]) == 'BYR':
                Total_summ += (int(j[3]))
    return int(Total_summ + Exchange_summ)


#print fuel_total_cost('car_stats.csv')


def number_of_days(csv_file):
    date_format = "%m/%d/%Y"
    date_list = []
    for row, j in enumerate(csv_file):
        if row != 0 and j[0] != '':
            date_list.append(j[0])
    a = datetime.strptime(date_list[0], date_format)
    b = datetime.strptime(date_list[-1], date_format)
    delta = b - a
    return int(delta.days)

#print number_of_days()


def mileage(csv_file):
    mileage_list = []
    for row, j in enumerate(csv_file):
        if row != 0 and j[0] != '':
            mileage_list.append(j[1])
    return int(mileage_list[-1])

#print mileage()


def amount_of_liters(csv_file):
    Total_summ = []
    for row, j in enumerate(csv_file):
        if row != 0 and j[0] != '':
            Total_summ.append(float(j[2]))
    return sum(Total_summ) - (50 - Total_summ[-1])


#print amount_of_liters()


def func_result(csv_file):
    print u'Money spent on fuel:                                {} BYR'.format(fuel_total_cost(csv_file))
    print u'An average amount of money on fuel per month:       {} BYR'.format(fuel_total_cost(csv_file) /  number_of_days(csv_file) * 30)
    print u'An average fuel consumption in liters per 100 km:   {} liters'.format(round(amount_of_liters(csv_file) * 100 / mileage(csv_file),2))



if __name__ == "__main__":
    csv_file = open_csv('car_stats.csv')
    func_result(csv_file)





