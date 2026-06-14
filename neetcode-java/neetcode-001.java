class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> se = new HashSet<>();
        for(int i : nums){
            if(se.contains(i)){
                return true;
            }
            se.add(i);
        }
        return false;
    }
}