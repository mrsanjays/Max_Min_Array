"""
Given an array A of size N. You need to find the sum of Maximum and Minimum element in the given array.
"""
class Solution:
    @staticmethod
    def Max_Min_Array(array):

        maximum=float('-inf')
        minimum=float('inf')
        for i in array:
            if i>maximum:
                maximum=i
            elif i<minimum:
                minimum=i
        return maximum+minimum

if __name__ == "__main__":
    ob=Solution()
    array=list(map(int,input().split()))
    print(ob.Max_Min_Array(array))



