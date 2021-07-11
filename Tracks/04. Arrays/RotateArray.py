# Rest of the code is already given

class Solution:
    def rotateArr(self,A,D,N):
        A[:D] = A[:D][::-1]
        A[D:] = A[D:][::-1]
        f = A[:D] + A[D:]
        A[:] = f[::-1]
