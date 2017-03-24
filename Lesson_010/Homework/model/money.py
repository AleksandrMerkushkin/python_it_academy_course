# -*- coding: utf-8 -*-

import json

GOLD = 1
SILVER = 2
COPPER = 3



class Money():
    def __init__(self,code, amount):
        self.code = code
        self.amount = amount

    def as_dict(self):
        d = {
            "code":self.code,
            "amount":self.amount
        }
        return d

    def save(self, file_object):
        json.dump(self.as_dict(), file_object)

    def load(self, file_object):
        object_as_dict = json.load(file_object)
        self.code = object_as_dict["code"]
        self.amount = object_as_dict["amount"]
        return object_as_dict

    def __str__(self):
        return u'currency_code:{}, amount:{}'.format(self.code, self.amount)



class Wallet():
    def __init__(self, gold, silver, copper):

        if gold.code != GOLD:
            raise Exception("gold.code != GOLD")
        if silver.code != SILVER:
            raise Exception("silver.code != SILVER")
        if copper.code != COPPER:
            raise Exception("copper.code != COPPER")

        self.gold   = gold
        self.silver = silver
        self.copper = copper
        self.money = {
        GOLD:   gold,
        SILVER: silver,
        COPPER: copper
        }

    def as_dict(self):
        d = {
            "gold":self.gold.as_dict(),
            "silver":self.silver.as_dict(),
            "copper":self.copper.as_dict()
            }
        return d

    def save(self, file_object):
        json.dump(self.as_dict(), file_object)

    def load(self, file_object):
        object_as_dict = json.load(file_object)
        self.gold =   object_as_dict["gold"]
        self.silver = object_as_dict["silver"]
        self.copper = object_as_dict["copper"]
        return object_as_dict

    def __str__(self):
        return u'Gold   - {};' \
               u'\n           Silver - {};' \
               u'\n           Copper - {};'.format(self.gold, self.silver, self.copper)