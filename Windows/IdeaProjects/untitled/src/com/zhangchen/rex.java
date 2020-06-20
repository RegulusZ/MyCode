package com.zhangchen;
import java.util.HashMap;
import java.util.Map;
import java.util.regex.*;

public class rex {
    public static void main(String args[]) {
        String strTest = "15:51:59";
        Pattern pattern = Pattern.compile("(2[0-3]|[0-1][0-9]):([0-5][0-9]):([0-5][0-9])");
        Matcher matcher = pattern.matcher(strTest);
        if (matcher.matches()) {
            String hour = matcher.group(1);
            String minute = matcher.group(2);
            String second = matcher.group(3);

            System.out.println(hour);
            System.out.println(minute);
            System.out.println(second);
        }
        else {
            System.out.println("输入不匹配");
        }
    }
}

