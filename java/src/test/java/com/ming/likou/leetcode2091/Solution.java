package com.ming.likou.leetcode2091;

class Solution {
    public int minimumDeletions(int[] nums) {
        if(nums.length <= 2){
            return nums.length;
        }
        int mi = nums[0];
        int ma = nums[0];
        int miind = 0,maind = 0;
        for(int i = 0;i < nums.length;i++){
            if(nums[i] < mi){
                mi = nums[i];
                miind = i;
            }
            if(nums[i] > ma){
                ma = nums[i];
                maind = i;
            }
        }
        int left = Math.min(miind,maind);
        int right = Math.max(miind,maind);
        return Math.min(Math.min(right + 1,nums.length - left + 1),left + 1 + nums.length - right + 1);
    }
}