# -*- coding: utf-8 -*-
import datetime
import time


now = datetime.datetime.now()
firstday = datetime.datetime.strptime('2017-1-1', '%Y-%m-%d')
birthday = datetime.datetime.strptime('2018-5-21', '%Y-%m-%d')
d1 = now - firstday
d2 = now - birthday

print 'firstday'
print d1.days
print 'birthday'
print d2.days
