package com.ming.likou.leetcode955;

class Solution {
    public int minDeletionSize(String[] strs) {
        int m = strs.length;
        int n = strs[0].length();
        boolean[] sorted = new boolean[m - 1];
        int ans = 0;
        for(int j = 0;j < n;j ++){
            boolean deleted = false;
            for(int i = 0;i < m - 1;i ++){
                if(sorted[i]){
                    continue;
                }
                if(strs[i].charAt(j) > strs[i + 1].charAt(j)){
                    deleted = true;
                    break;
                }
            }
            if(deleted){
                ans ++;
                continue;
            }
            for(int i = 0; i < m - 1;i ++){
                if(strs[i].charAt(j) < strs[i + 1].charAt(j)){
                    sorted[i] = true;
                    continue;
                }
            }
        }
        return ans;
    }
}