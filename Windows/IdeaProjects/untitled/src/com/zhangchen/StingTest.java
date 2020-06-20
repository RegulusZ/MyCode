package com.zhangchen;

public class StingTest {
    public static void main(String[] args) {
        String str1 = "Hello World";
        String str2 = "Hello Zhangchen";
        String substr1 = str1.substring(0,5);
        String substr2 = str2.substring(0,5);

        if (substr1.equalsIgnoreCase(substr2)) {
            System.out.println("两个子串相同");
        }
        else {
            System.out.println("两个子串不同");
        }
    }
}
