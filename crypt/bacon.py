#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = 'tyomcat'
# 培根解密代码
# 两种加密方式
import sys
def peig1(m):
    basic1 = {
    'AAAAA' : 'A',
    'AAAAB' : 'B',
    'AAABA' : 'C',
    'AAABB' : 'D',
    'AABAA' : 'E',
    'AABAB' : 'F',
    'AABBA' : 'G',
    'AABBB' : 'H',
    'ABAAA' : 'I',
    'ABAAB' : 'J',
    'ABABA' : 'K',
    'ABABB' : 'L',
    'ABBAB' : 'N',
    'ABBBA' : 'O',
    'ABBBB' : 'P',
    'BAAAA' : 'Q',
    'BAAAB' : 'R',
    'BAABA' : 'S',
    'BAABB' : 'T',
    'BABAA' : 'U',
    'BABAB' : 'V',
    'BABBA' : 'W',
    'BABBB' : 'X',
    'BBAAA' : 'Y',
    'BBAAB' : 'Z'
    }
    output = ''
    for i in range(0, len(m) - 4, 5):
        temp = m[i: i + 5]
        output += basic1[temp]
    return output

def peig2(m):

    basic2 = {
    'AAAAA' : 'A',
    'AAAAB' : 'B',
    'AAABA' : 'C',
    'AAABB' : 'D',
    'AABAA' : 'E',
    'AABAB' : 'F',
    'AABBA' : 'G',
    'AABBB' : 'H',
    'ABAAA' : 'I',
    'ABAAA' : 'J',
    'ABAAB' : 'K',
    'ABABA' : 'L',
    'ABABB' : 'M',
    'ABBAA' : 'N',
    'ABBAB' : 'O',
    'ABBBA' : 'P',
    'ABBBB' : 'Q',
    'BAAAA' : 'R',
    'BAAAB' : 'S',
    'BAABA' : 'T',
    'BAABB' : 'U',
    'BAABB' : 'V',
    'BABAA' : 'W',
    'BABAB' : 'X',
    'BABBA' : 'Y',
    'BABBB' : 'Z'
    }
    output = ''
    for i in range(0, len(m) - 4, 5):
        temp = m[i: i + 5]
        output += basic2[temp]
    return output

if __name__ == '__main__':
    
    m = raw_input("请输入密文:")
    mode = input("选择密文对应的方式 1 or 2：")
    if len(m)%5 == 0:
        l = []
        k = []
        for i in xrange(len(m)/5):
            l.append(m[:5])
            m = m[5:]
        if mode == 1:
            for i in l:
                if i.isupper():
                    k.append(peig1(i))
                else:
                    i = i.upper()
                    k.append(peig1(i))

        elif mode == 2:
            for i in l:
                if i.isupper():
                    k.append(peig2(i))
                else:
                    i = i.upper()
                    k.append(peig2(i))
        flag = ''
        for i in k:
            flag+=i[0]
        print flag