#! /usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ == "tyomcat"

import operator

str=''  #词频分析的字符串
payloads = 'ujcvtkgekcgcxqeayuhge'
payloads = payloads.upper()
# print payloads
dists = {}
for x in payloads:
    dists[x] = 0
    # print x,dists[x]
for s in str:
    dists[s] += 1

ans = ''
res = sorted(dists.iteritems(), key=operator.itemgetter(1), reverse=True)
for r in res:
    ans += r[0]
    print r
print ans