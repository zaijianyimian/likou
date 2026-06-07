class Solution001 {
    public int divide(int a, int b) {
        if (a == Integer.MIN_VALUE && b == -1) {
            return Integer.MAX_VALUE;
        }
        int flag = 0;
        if(a > 0){
            a = -a;
            flag += 1;
        }
        if(b > 0){
            b = -b;
            flag += 1;
        }

        int ans = 0;
        while(a <= b){
            int tmp = b;
            int count = 1;
            while(tmp > Integer.MIN_VALUE >>1   && a <= tmp + tmp){
                tmp += tmp;
                count += count;
            }
            a -= tmp;
            ans += count;
        }
        if(flag == 1){
            ans = -ans;
        }
        return ans;
    }
}