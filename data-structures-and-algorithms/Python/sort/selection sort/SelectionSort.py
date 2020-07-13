'''
@Author: Goog Tech
@Date: 2020-07-13 15:35:00
@Description: selection sort
@FilePath: algorithm.show\leetcode-googtech\data-structures-and-algorithms\Python\sort\selection sort\SelectSort.py
'''
class SelectionSort:
    
    '''
    @description: 选择排序
    @param {alist} 
    @return: 
    '''
    def selectionSort(self,alist):
        for fillslot in range(len(alist)-1,0,-1): # range(start, stop[, step])
            positionOfMax = 0
            # 寻找最大值
            for location in range(1,fillslot+1):
                if alist[location] > alist[positionOfMax]:
                    positionOfMax = location
            # 交互数据
            temp = alist[fillslot]
            alist[fillslot] = alist[positionOfMax]
            alist[positionOfMax] = temp
        print(alist)

s = SelectionSort()
s.selectionSort([6,5,4,3,2,1]) # [1, 2, 3, 4, 5, 6]
