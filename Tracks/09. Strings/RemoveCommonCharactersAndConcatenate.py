# Rest of the code is already given in driver code

class Solution:
    
    def concatenatedString(self,s1,s2):
        cms = set(s) & set(p)
        rst = []
        for i in s:
            if i not in cms:
                rst.append(i)
        for i in p:
            if i not in cms:
                rst.append(i)
        if len(rst) == 0:
            return -1
        else:
            return ''.join(rst)