# Rest of the code is already given

class Solution:
    def insertAtIndex(self, arr, sizeOfArray, index, element):
        if len(arr) <= index:
            arr.append(element)
        else:
            arr.insert(index,element)
            arr.pop()
