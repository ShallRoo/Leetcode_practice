"""
author：ShallRoo
Created on 2021/10/7 19:23
"""
if __name__ == "__main__":
    class Solution:
        def isValid(self, s: str) -> bool:
            stack = []
            mapping = {
                '(': ')',
                '[': ']',
                '{': '}'
            }#创建字典
            for item in s:
                if item in mapping.keys():
                    stack.append(mapping[item])
                elif not stack or stack[-1] != item:
                    return False
                else:
                    stack.pop()
            return True if not stack else False

if __name__ == "__main__": #debug代码

    s="(([]))[]{}"

    stack = [] #采用栈的数据结构，先进后出，先出现的左半边括号要后删除，后加的先删
    mapping = {
        '(': ')',
        '[': ']',
        '{': '}'
    } #创建字典
    for item in s:
        if item in mapping.keys(): #先匹配的对象先进栈
            stack.append(mapping[item])
        elif not stack or stack[-1] != item:
            print(False)
        else:
            stack.pop()
    if stack:
        print(False)
    else:
        print(True)