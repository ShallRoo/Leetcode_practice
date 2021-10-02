"""
author：ShallRoo
Created on 2021/10/2 8:45
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        while 0 in nums:
            for i in nums:
                if i == 0:
                    nums.remove(i)
                    nums.append(0)
        return nums

        #加上了while条件是因为每次删除之后，列表会自动更新，而循环就会漏掉前面已有的元素
        #当列表存在相邻的0元素时，结果就会出错
        #这个方法虽然能解决问题，但是消耗的时间超过时间限制了


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        n = nums.count(0)
        if n != 0:
            nums_set = list(set(nums))
            nums_set.remove(0)
            for i in range(n):
                nums_set.append(0)
            return nums_set
        else:
            return nums

        #修改：
        #for i in range(n):
        #   nums.remove(0)
        #nums.extend([0]*n)
        #这个方法在pycharm上跑得出来，可是LeetCode上显示的是错误
        #错误原因是，LeetCode要求在原数组上进行修改，最后return不需要打出，默认直接return nums
        #因为return的不是原数组所以报错了


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1

        #别人的解答：冒泡，不断把非零元素往前提


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        n = nums.count(0)
        for i in range(n):
            nums.remove(0)
        nums.extend([0] * n)