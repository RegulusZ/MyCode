package com.zhangchen;

import java.util.Date;

public class FormatTest {
    public static void main(String[] args) {
        Date date = new Date();
        String s = String.format("%te", date);

        System.out.println(date);
        System.out.println(s);
        System.out.println(String.format("%tb", date));
        System.out.println(String.format("%tB", date));
        System.out.println(String.format("%tA", date));
        System.out.println(String.format("%ta", date));
        System.out.println(String.format("%tc", date));
        System.out.println(String.format("%tY", date));
        System.out.println(String.format("%tj", date));
        System.out.println(String.format("%tm", date));
        System.out.println(String.format("%ty", date));

    }
}
