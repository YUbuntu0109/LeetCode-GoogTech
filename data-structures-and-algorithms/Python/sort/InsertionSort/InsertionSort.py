'''
@Author: Goog Tech
@Date: 2020-07-13 16:05:46
@Description: insertion sort
@FilePath: alogrithm.show\leetcode-googtech\data-structures-and-algorithms\Python\sort\InsertionSort\InsertionSort.py
'''
class InsertionSort:
    
    '''
    @description: 插入排序
    @param {alist} 
    @return: 
    '''
    def insertionSort(self,alist):
        for index in range(1,len(alist)):
            currentValue = alist[index]
            position = index
            while position > 0 and alist[position-1] > currentValue:
                alist[position] = alist[position-1]
                position = position - 1
            alist[position] = currentValue
        print(alist)
    

i = InsertionSort()
i.insertionSort([6,5,4,3,2,1]) # [1, 2, 3, 4, 5, 6]
