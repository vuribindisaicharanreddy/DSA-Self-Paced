// Rest of the code is already given as Driver Code

class Tree 
{
    boolean IsFoldable(Node node) 
	{ 
	    if(node == null)
	        return true;
	    return findFoldable(node.left,node.right);
	} 
	
	boolean findFoldable(Node root1,Node root2){
	    if(root1==null && root2==null)
	        return true;
	       
	    return (root1 != null && root2 != null) 
	            && findFoldable(root1.left,root2.right) 
	            && findFoldable(root1.right,root2.left);
	}
}