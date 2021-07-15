// Rest of the code is already given as Driver Code

int recur_sum(Node*root,int prev_chosen)
{
    int d,res1=0,res2=0,res3=0,res4=0,res5=0,left=0,right=0;
    
    if(root==NULL)
    return 0;
    d = root->data;
    if(prev_chosen){
        res1 = recur_sum(root->left,0)+recur_sum(root->right,0);
        return res1;
    }
    else{
        res2 = recur_sum(root->left,1);
        res3 = recur_sum(root->right,1);
        res4 = recur_sum(root->left,0);
        res5 = recur_sum(root->right,0);
        return max(d+res2+res3,res4+res5);
    }
    
   
}
int getMaxSum(Node *root) 
{
    return recur_sum(root,0);
}