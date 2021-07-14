# Rest of the code is already given in driver code

class Solution:
    def isIsogram(self,s):
        import collections
        freqs = collections.Counter(s)
        if len(set(freqs.values())) == 1 and 1 in set(freqs.values()):
            return True
        else:
            return False