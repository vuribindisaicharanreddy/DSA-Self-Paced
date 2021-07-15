// Rest of the code is already given as Driver Code

class Solution {
    void mirror(Node node)
    {
        if(node == null)
            return;
        mirror(node.left);
        mirror(node.right);
        Node temp = node.right;
        node.right = node.left;
        node.left = temp;
    }
}