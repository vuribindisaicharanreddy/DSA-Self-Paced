# Rest of the code is already given in driver code

class Solution:
    def areRotations(self, s1,s2):
        if (len(s1) == 1 or len(s2) == 1) & (s1 != s2):
            return False
        if (len(s1) == len(s2)) & (set(s1)==set(s2)) & (s2 in s1+s2) & (s1 in s1+s2):
            return True
        else:
            return False