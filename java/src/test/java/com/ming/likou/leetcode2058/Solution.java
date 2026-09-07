package com.ming.likou.leetcode2058;


import java.util.ArrayList;
import java.util.List;

//Definition for singly-linked list.
class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class Solution {
    public int[] nodesBetweenCriticalPoints(ListNode head) {
        ListNode dummy = new ListNode(0,head);
        ListNode cur = head;
        ListNode pre = dummy;
        int ind = 0;
        List<Integer> list = new ArrayList<>();
        while(cur != null && cur.next != null){
            if(pre == dummy){
                pre = cur;
                cur = cur.next;
                ind ++;
                continue;
            }
            if((pre.val > cur.val && cur.val < cur.next.val) || (pre.val < cur.val && cur.val > cur.next.val)){
                list.add(ind);

            }
            pre = cur;
            cur = cur.next;
            ind ++;
        }
        if(list.size() < 2){
            return new int[]{-1,-1};
        }
        int maxInd = list.get(list.size() - 1) - list.get(0);
        int minInd = list.get(1) - list.get(0);
        for(int i = 0;i < list.size() - 1;i++){
            minInd = Math.min(minInd,list.get(i + 1) - list.get(i));
        }
        return new int[]{minInd,maxInd};
    }
}