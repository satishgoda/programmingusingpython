# https://github.com/lxyu/pinyin
# https://github.com/staff0rd/mandarin

import pinyin

##

print pinyin.get('你好')

print pinyin.get('你好', format='numerical')

print pinyin.get('你好', format='diacritical')

print pinyin.get('你好', format='strip')

##

for tonemark in pinyin.pinyin.tonemarks:
    if tonemark:
        print tonemark
##

"""

nǐhǎo
ni3hao3
nǐhǎo
nihao
̄
́
̌
̀

"""
