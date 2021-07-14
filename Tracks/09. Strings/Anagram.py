# Rest of the code is already given in driver code

class Solution:
    def isAnagram(self,a,b):
        import collections
        freqs_a = collections.Counter(a)
        freqs_b = collections.Counter(b)
        if (set(a) == set(b)) and (sorted(freqs_a.values()) == sorted(freqs_b.values())):
            return True
        else:
            return False