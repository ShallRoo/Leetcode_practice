"""
author：ShallRoo
Created on 2021/9/30 15:28
"""

s="ccdcc"

a=[]
s=list(s)
m=[]
if len(s)>2:
    for i in range(0, len(s) - 1):
        if len(m)<len(a):
            m = a
            a=[]
        else:
            for n in range(0, len(s) // 2):
                if s[i-n] == s[i+n]:
                    if i-n != i+n:
                        a.append(s[i+n])
                        a.insert(0,s[i-n])
                    else:
                        a.append(s[i])
                else:
                    continue
else:
    m = s[0]
print(m)

#只能跑出去三个回文数的结果，跑不出两个的。。。

#采用动态规划
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2: return s

        max_len = 1
        begin = 0
        dp = [[False] * n for _ in range(n)]
        for i in range(n): dp[i][i] = True

        for L in range(2, n + 1):
            for i in range(n):
                j = L + i - 1
                if j >= n: break
                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    begin = i
        return s[begin:begin + max_len]


#作者：caiji - ud
#链接：https: // leetcode - cn.com / problems / longest - palindromic - substring / solution / python3 - dong - tai - gui - hua - by - caiji - ud - 3yzx /
#来源：力扣（LeetCode）
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        palindrome = ''

        for i in range(len(s)):
            #回文字符中心对称
            len_1 = len(self.getlongestpalindrome(s, i, i))
            if len_1 > len(palindrome):
                palindrome = self.getlongestpalindrome(s, i, i)
            #回文字符轴对称
            len_2 = len(self.getlongestpalindrome(s, i, i + 1))
            if len_2 > len(palindrome):
                palindrome = self.getlongestpalindrome(s, i, i + 1)

        return palindrome

    def getlongestpalindrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r]

#以上是学习了b站上的解法