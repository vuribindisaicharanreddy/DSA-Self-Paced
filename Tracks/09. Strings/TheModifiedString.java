// Rest of the code is already given in driver code

class Solution
{
    public static long modified(String a)
    {
        int start = 0;
        int end = 0;
        int count = 0;
        long result = 0;
        
        while(start<=end && end<a.length())
        {
            if(a.charAt(start)==a.charAt(end))
            {
                end++;
                count++;
            }
            else
            {
                count = 0;
                start = end;
            }
            
            if(count == 3)
            {
                result++;
                end--;
                start = end;
                count = 0;
            }
        } 
        return result;
    }
}