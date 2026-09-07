package testshenzhou.test1;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
//        int[] arr = new int[n];
        int count = 0;
        for(int i = 0;i < n;i ++) {
            int num = sc.nextInt();
            if(num % 2 == 1){
                count ++;
            }
        }
        if(count != 0)System.out.println(count);
        else System.out.println(-1);
    }
}
