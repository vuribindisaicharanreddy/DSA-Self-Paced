# Rest of the code is already given in driver code

class Solution:
    def repeatingCharacter(self,s):
        import collections
        freqs = collections.Counter(s)
        if len(set(freqs.values())) == 1 and 1 in set(freqs.values()):
            return -1
        else:
            inds = []
            for k,v in freqs.items():
                if v > 1:
                    inds.append(s.index(k))
            return min(inds)