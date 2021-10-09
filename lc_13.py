"""
author：ShallRoo
Created on 2021/9/27 20:55
"""


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        characters = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        n = list(s[::])
        k = len(n) #=4
        r = 0
        for i in range(k): #0,1,2,3
            if i == k-1:
                r = r + characters[n[i]]
            elif characters[n[i]] >= characters[n[i + 1]]:
                r = r + characters[n[i]]
            else:
                r = r - characters[n[i]]
        return r


class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I':1, 'IV':3, 'V':5, 'IX':8, 'X':10, 'XL':30, 'L':50, 'XC':80, 'C':100, 'CD':300, 'D':500, 'CM':800, 'M':1000}
        return sum(d.get(s[max(i-1, 0):i+1], d[n]) for i, n in enumerate(s))

#作者：QQqun902025048
#链接：https://leetcode-cn.com/problems/roman-to-integer/solution/2-xing-python-on-by-knifezhu/
#来源：力扣（LeetCode）
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。