// Rest of the code is already given as Driver Code

class GfG
{
    public static Node createTree(int arr[], int n)
    {
        if(n==0)
            return null;
            
        Node relation[] = new Node[n];
        for(int i=0;i<n;i++)
            relation[i] = (new Node(i));
        Node root = null;
        
        Node child = null;
        Node parent = null;
        for(int i=0;i<n;i++){
            child = relation[i];
            if(arr[i]==-1)
                root = relation[i];
            else{
                parent = relation[arr[i]];
                if(parent.left == null)
                    parent.left = child;
                else
                    parent.right = child;
            }  
        }
        return root;
    }  
}