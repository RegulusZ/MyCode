package com.zhangchen;

public class BubbleSort {
    public static void main(String[] args) {
        int[] array = {2,3,1,7,2,8,3,6,0};
        array = sort(array);
        for (int a : array) {
            System.out.println(a);
        }

    }
    static private int[] sort(int[] array) {
        for (int i=0; i < array.length-1; i++) {
            for (int j=0; j < array.length-1; j++) {
                if (array[j] > array [j+1]) {
                    int temp = array[j];
                    array[j] = array[j+1];
                    array[j+1] = temp;
                }
            }
        }
        return array;
    }
}
