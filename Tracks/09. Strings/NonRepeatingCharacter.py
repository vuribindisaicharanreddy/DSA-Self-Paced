# Rest of the code is already given in driver code

import collections
class Solution:
    
    def nonrepeatingCharacter(self,s):
        freqs = collections.Counter(s)
        if 1 not in freqs.values():
            return -1
        else:
            for c in s:
                if freqs[c]==1:
                    return c