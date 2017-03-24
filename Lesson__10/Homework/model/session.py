# -*- coding: utf-8 -*-
import json
import datetime



class Session():
    def __init__(self):
        self.start_time = datetime.datetime.now()


    def start(self):
        self.start_time = datetime.datetime.now()
        return self.start_time

    def end(self):
        self.end_time = datetime.datetime.now()
        return self.end_time

    def get_elapse_time(self):
        elapsedTime = None
        if self.start_time is not None:
            if self.end_time is not None:
                elapsedTime = (self.end_time) -\
                              (self.start_time)
        else:
            # Timer hasn't started, error on the side of caution
            rightNow = datetime.datetime.now()
            elapsedTime = (rightNow - rightNow)
        return(elapsedTime)


    def as_dict(self):
        d = {
            "start_time":self.start_time,
            "end_time":self.end_time,
        }
        return d

    def save(self, file_object):
        json.dump(self.as_dict(), file_object)

    def load(self, file_object):
        object_as_dict = json.load(file_object)
        self.start_time = object_as_dict["start_time"]
        self.finish_time = object_as_dict["finish_time"]
        return object_as_dict

    def __str__(self):
        return u'Starting : {};\n' \
               u'Finished : {};'.format(self.start_time, self.finish_time)
