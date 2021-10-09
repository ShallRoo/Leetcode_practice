"""
author：ShallRoo
Created on 2021/10/9 21:33
"""

if __name__ == "__main__":
    class Solution(object):
        def lengthOfLongestSubstring(self, s):
            """
            :type s: str
            :rtype: int
            """

            def get_long(s, i):
                k = []
                for item in s[i:]:
                    if item in k:
                        return k
                    else:
                        k.append(item)
                return k

            if not s:
                return 0
            else:
                a = 0
                l = 0
                ans = []
                for i in range(len(s)):
                    l = len(get_long(s, i))
                    if l > a:
                        ans = get_long(s, i)
                        a = l
            return len(ans)

#我自己的答案：通过时间1340ms,内存消耗14.3MB

'''
标签：滑动窗口
暴力解法时间复杂度较高，会达到 O(n^2)，故而采取滑动窗口的方法降低时间复杂度
定义一个 map 数据结构存储 (k, v)，其中 key 值为字符，value 值为字符位置 +1，加 1 表示从字符位置后一个才开始不重复
我们定义不重复子串的开始位置为 start，结束位置为 end
随着 end 不断遍历向后，会遇到与 [start, end] 区间内字符相同的情况，此时将字符作为 key 值，获取其 value 值，并更新 start，此时 [start, end] 区间内不存在重复字符
无论是否更新 start，都会更新其 map 数据结构和结果 ans。
时间复杂度：O(n)

作者：guanpengchn
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/solution/hua-jie-suan-fa-3-wu-zhong-fu-zi-fu-de-zui-chang-z/
来源：力扣（LeetCode）
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        left = 0
        lookup = set()
        n = len(s)
        max_len = 0
        cur_len = 0
        for i in range(n):
            cur_len += 1
            while s[i] in lookup:
                lookup.remove(s[left])
                left += 1
                cur_len -= 1
            if cur_len > max_len:
                max_len = cur_len
            lookup.add(s[i])
        return max_len

#作者：powcai
#链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/solution/hua-dong-chuang-kou-by-powcai/
#来源：力扣（LeetCode）
