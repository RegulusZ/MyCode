package com.zhangchen;


import com.sun.nio.sctp.PeerAddressChangeNotification;

import java.math.BigInteger;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.Objects;

import static java.lang.System.out;


 class Node {
      int val;
      Node next;
      Node random;
     public Node(int val) {
         this.val = val;
         this.next = null;
         this.random = null;
     }
  }
class Solution {

    public static void main(String[] args) {
//        ListNode l1 = new ListNode(9);
//        l1.next = new ListNode(4);
//        l1.next.next = new ListNode(3);
        Node l0 = new Node(0);
        Node l1 = new Node(1);
        Node l2 = new Node(2);
        l0.next = l1;
        l1.next = l2;
        l0.random = l2;
        l1.random = null;
        l2.random = l1;
//        l2.next = new ListNode(2);
//        l2.next.next = new ListNode(3);
//        l2.next.next.next = new ListNode(4);
//        l2.next.next.next.next = new ListNode(5);
////        l2.next.next.next.next.next = new ListNode(9);
////        l2.next.next.next.next.next.next = new ListNode(9);
////        l2.next.next.next.next.next.next.next = new ListNode(9);
////        l2.next.next.next.next.next.next.next.next = new ListNode(9);
////        l2.next.next.next.next.next.next.next.next.next = new ListNode(9);

        Node ans = copyRandomList(l0);
        out.println(ans);
    }


    public static Node copyRandomList(Node head) {
        if(head == null) {
            return head;
        }

        Map hashmap<Node, Node> = new HashMap<>();

        Node p = head;
        while (p != null) {
            hashmap.put(p, new Node(p.val));
        }

        Node q = hashmap.get(head);

        for (Node p : hashmap.keySet()) {
            hashmap.get(p).next = hashmap.get(p.next);
            hashmap.get(p).random = hashmap.get(p.random);
        }

        return hashmap.get(head);
    }
    }




