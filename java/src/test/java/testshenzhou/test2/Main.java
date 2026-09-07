package testshenzhou.test2;

import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for(int i = 0;i < n;i++){
            arr[i] = sc.nextInt();
        }
        Set<Integer> ji = new HashSet<>();
        Set<Integer> ou = new HashSet<>();
        for(int num: arr){
            if(num % 2 == 0){
                ou.add(num);
            }else{
                ji.add(num);
            }
        }
        List<Integer> ouList = new ArrayList<>(ou);
        List<Integer> jiList = new ArrayList<>(ji);
        if(jiList.isEmpty() || ouList.isEmpty()){
            System.out.println(1);
            return;
        }
        Collections.sort(jiList);
        Collections.sort(ouList);
        int i = 0,j = 0;
        List<Integer> res = new ArrayList<>();
        int flag = -1;
        while(i < jiList.size() && j < ouList.size()){
           if(flag == -1){
               if(jiList.get(i) < ouList.get(j)){
                   flag = 0;
                   res.add(jiList.get(i));
                   i ++;
               }else{
                   flag = 1;
                   res.add(ouList.get(j));
                   j ++;
               }
               continue;
           }
           if(flag == 1){
               int num = jiList.get(i);
               if(num < res.get(res.size() - 1)){
                   i ++;
                   continue;
               }
               res.add(num);
               i ++;
               flag = 0;
               continue;
           }
           if(flag == 0){
               int num = ouList.get(j);
               if(num < res.get(res.size() - 1)){
                   j ++;
                   continue;
               }
               res.add(num);
               j ++;
               flag = 1;
               continue;
           }
        }
        while(flag == 1 && i < jiList.size()){
            if(jiList.get(i) < res.get(res.size() - 1)){
                i ++;
                continue;
            }
            res.add(jiList.get(i));
            i ++;
            break;
        }
        while(flag == 0 && j < ouList.size()){
            if(ouList.get(j) < res.get(res.size() - 1)){
                j ++;
                continue;
            }
            res.add(ouList.get(j));
            j ++;
            break;
        }
        System.out.println(res.size());
    }
}
