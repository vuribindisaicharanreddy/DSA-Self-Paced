# Rest of the code is already given

class Solution:
    def convertToWave(self,A,N):
        temp=0
        for i in range(N-1):
            if i%2 == 0:
                if A[i] < A[i+1]:
                    temp=A[i]
                    A[i]=A[i+1]
                    A[i+1]=temp
                else:
                    continue
            else:
                if A[i] > A[i+1]:
                    temp=A[i]
                    A[i]=A[i+1]
                    A[i+1]=temp
                else:
                    continue
