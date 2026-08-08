package com.ming.likou.leetcode944;

class Solution {
    public int minDeletionSize(String[] strs) {
        int ans = 0;
        int m = strs.length,n = strs[0].length();
        for(int i = 0;i < n;i ++){
            char ma = strs[0].charAt(i);
            for(int j = 1;j < m;j ++){
                if(strs[j].charAt(i) < ma){
                    ans ++;
                    break;
                }
                ma = strs[j].charAt(i);
            }
        }
        return ans;
    }
}
