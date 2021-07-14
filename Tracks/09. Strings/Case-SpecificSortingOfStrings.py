# Rest of the code is already given in driver code

class Solution:
    def caseSort(self,s,n):
        upper_chars = sorted([i for i in s if i.isupper()])
        lower_chars = sorted([i for i in s if i.islower()])
        sorted_string = []
        for c in s:
            if c.islower():
                sorted_string.append(lower_chars[0])
                x = lower_chars.pop(0)
            elif c.isupper():
                sorted_string.append(upper_chars[0])
                x = upper_chars.pop(0)
        return ''.join(sorted_string)