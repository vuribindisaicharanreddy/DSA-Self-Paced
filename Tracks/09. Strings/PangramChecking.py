# Rest of the code is already given in driver code

class Solution:
    def checkPangram(self,s):
        import string
        letters = set(string.ascii_lowercase)
        gletters = set(s)
        if gletters & letters == letters:
            return True
        else:
            return False