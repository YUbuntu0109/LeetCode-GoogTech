'''
Author: Goog Tech
Date: 2020-08-29 16:02:32
LastEditTime: 2020-08-29 16:02:44
Description: https://leetcode-cn.com/problems/generate-a-string-with-characters-that-have-odd-counts/
FilePath: \leetcode-googtech\#1374. Generate a String With Characters That Have Odd Counts\Solution.py
WebSite: https://algorithm.show/
'''

class Solution(object):
    def generateTheString(self, n):
        """
        :type n: int
        :rtype: str
        """
        return "a" * n if n % 2 != 0 else "a" * (n - 1) + "b";
