"""
author：ShallRoo
Created on 2021/9/28 17:43
"""

"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。
"""
from collections import Counter
strs = ["flower","flow","flight"]


dict={}
s=10000
a=[]
for index,value in enumerate(strs):
    dict[index] = list(str(value))
    k=len(dict[index])
    if s>k:
        s=k
    else:
        continue

for i in range(s):
    for index in dict:
        if dict.get(index)[i] == dict.get(index+1)[i] and dict.get(index)[i] not in a:
            a.append(dict.get(index)[i])
        else:
            break

print(a)

#以下为调试段

res = ""
for tmp in zip(*strs):
#逐个读取strs中元素的第一个字符
    tmp_set = set(tmp)
#set主要用于寻找列表中的不同元素
    if len(tmp_set) == 1:
        res += tmp_set.pop()
    else:
        break
print(res)

#这样得出的结果只是前两个元素进行比较，并没有所有元素一起比较

"""
class Solution:
    def longestCommonPrefix(self, strs):
        
        :type strs: List[str]
        :rtype: str
        
        res = ""
        for tmp in zip(*strs):
            
            tmp_set = set(tmp)
            if len(tmp_set) == 1:
                res += tmp[0]
            else:
                break
        return res

#作者：powcai
#链接：https://leetcode-cn.com/problems/longest-common-prefix/solution/duo-chong-si-lu-qiu-jie-by-powcai-2/
#来源：力扣（LeetCode）
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
