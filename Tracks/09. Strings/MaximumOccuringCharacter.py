# Rest of the code is already given in driver code

class Solution:
    
    def getMaxOccurringChar(self,s):
        import collections
        freqs = collections.Counter(s)
        maxO = max(freqs.values())
        chars = []
        for c in s:
            if freqs[c] == maxO:
                chars.append(c)
        if len(chars) == 1:
            return chars[0]
        else:
            return min(chars)