class Solution:

    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        numSet = set()
        myList = set(arr)

        for num in myList:
            count = arr.count(num)
            if count in numSet:
                return False
            else:
                numSet.add(count)
        
        return True