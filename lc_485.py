"""
author：ShallRoo
Created on 2021/10/1 10:12
"""
"""
nums = [0,0]
s=set(nums)
if 1 not in s:
    l=0
else:
    k=1
    l=1
    for i in range(1,len(nums)):
        if nums[i]-nums[i-1]==1:
            k = 1
        elif nums[i]==nums[i-1]==1:
            k+=1
        if k>l:
            l=k
print(l)
"""
"""
if nums is None or len(nums) == 0;
    return 0

c_o = 0 if nums[0] == 0 else 1
m_c_o = c_o

for i in range(1,len(nums)):
    if nums[i] == 1:
        c_o += 1
    else:
        c_o = 0
    m_c_o = max(m_c_o,c_o)
return m_c_o
"""

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #如果列表里没有1可以直接return 0
        while 1 not in set(nums):
            return 0
        l,k=1,1
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]==1:
                k=1
            elif nums[i]==nums[i-1]==1:
                k+=1
            l=max(l,k)
        return l


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res,tmp=0,0
        for i in nums:
            if i==0:tmp=0
            else:tmp+=1
            res = max(tmp,res)
        return res

#目前我只找到了比较垃圾的循环解决，时间复杂度都很高，不是很巧妙

#下面的解法是错误的
nums = [1,1,0,1]#或者[0,1],[1,1,0,1,1,1]都是错误答案
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        while 1 not in set(nums):
            return 0
        l,k=1,1
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]==1 or nums[i]==nums[i-1]==1:
                k+=1
            else:
                k=0
            l=max(l,k)
        return l