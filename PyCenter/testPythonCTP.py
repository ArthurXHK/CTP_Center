#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
test ctp
'''

import os
import sys
import CTPPack
from CTPPack import *
from time import sleep


__author__ = 'jebin'




center = MarketDataCenter.MarketDataCenter()
center.run()

trader = Trader.Trader()
trader.Connect()
trader.SendOrder('IF1501', '0', '0', 2, 3350)
sleep(1)
#trader.CancelOrder(1)
trader.Release()
CTPPack.MainOverEvent.wait()

