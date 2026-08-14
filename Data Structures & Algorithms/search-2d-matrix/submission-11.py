class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def find_position(n):
            return (int(n/len(matrix[0])),(n)%len(matrix[0]))

        l, r = 0, len(matrix)*len(matrix[0])-1

        while l<=r:
            mid = (r+l)//2
            x,y = find_position(mid)

            if target == matrix[x][y]:
                return True
            elif target < matrix[x][y]:
                r = mid - 1
            else:
                l = mid + 1

        return False



        