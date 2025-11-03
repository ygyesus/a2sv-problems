# Problem: Sort the People - https://leetcode.com/problems/sort-the-people/

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # BUBBLE SORT

        arr = heights
        for i in range(len(arr)):
            for j in range(1, len(arr)-i):
                if arr[j-1] < arr[j]:
                    arr[j-1], arr[j] = arr[j], arr[j-1]
                    names[j-1], names[j] = names[j], names[j-1]
                    
                    
                                    
        print("BUBBLE SORT:")
                    
        print(heights)
        print(names)
        
        return names
                
