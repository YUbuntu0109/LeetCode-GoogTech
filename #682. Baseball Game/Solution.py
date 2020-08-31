'''
Author: Goog Tech
Date: 2020-08-31 17:36:50
LastEditTime: 2020-08-31 17:37:13
Description: https://leetcode-cn.com/problems/baseball-game/
FilePath: \leetcode-googtech\#682. Baseball Game\Solution.py
WebSite: https://algorithm.show/
'''

class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        # 初始化辅助栈
        stack = []
        # 逐个遍历字符串数组中的符号
        for op in ops:
            # 轮获得的得分是前两轮有效回合得分的总和,即获取栈顶及栈顶第二个元素,并将其相加后压入栈中
            if op == '+':
                stack.append(stack[-1] + stack[-2])
            # 获得的最后一个有效回合的分数是无效的,即删除栈顶元素
            elif op == 'C':
                stack.pop()
            # 本轮获得的得分是前一轮有效回合得分的两倍,即获取栈顶元素并将其乘以二后压入栈中
            elif op == 'D':
                stack.append(2 * stack[-1])
            # 表示本轮中获得的积分数,即直接将其压入栈中
            else:
                stack.append(int(op))
        # 返回总分数值
        return sum(stack)
