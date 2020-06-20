package com.zhangchen;

public class WhileLoop {
    public static void main(String[] args) {
        int n = 1;
        float sum = 0;
        while (n <= 30) {
            int i = 1;
            int s = 1;
            while (i <= n) {
                s = s * i;
                i++;
            }
            sum += 1.0/s;
            n++;
        }
        System.out.println(sum);
    }
}

