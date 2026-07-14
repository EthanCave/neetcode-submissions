class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        ones = sum(students)
        zeros = len(students) - ones
        
        while (ones and sandwiches[0] == 1) or (zeros and sandwiches[0] == 0):
            if sandwiches[0] == 1:
                ones -= 1
                sandwiches.pop(0)
            elif sandwiches[0] == 0:
                zeros -= 1
                sandwiches.pop(0)
        return ones + zeros