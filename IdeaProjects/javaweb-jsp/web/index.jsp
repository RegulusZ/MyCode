<%--
  Created by IntelliJ IDEA.
  User: chen
  Date: 2020/7/10
  Time: 21:43
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
  <head>
    <title>$Title$</title>
  </head>
  <body>

<%--  jsp表达式
<%= 变量或表达式=%>
作用：将程序的结果输出到客户端--%>
<%= new java.util.Date()%>

  <hr>
  <%--jsp 脚本片段--%>
  <%
    int sum = 0;
    for (int i=1; i <= 100; i++){
      sum += i;
    }
    out.println("<h1>Sum=" + sum + "<h1>");
  %>

  <%
    int x = 10;
    out.println(x);
  %>

  <p>这是一个jsp文档</p>

  <%
    out.println(x);
  %>

  <hr>

<%--在代码中嵌入html元素--%>
<%--el表达式--%>
  <%
    for (int i = 0; i < 5; i++){
  %>
    <h1>hello,world   ${i} </h1>
  <%
    }
  %>

<%!
  static {
    System.out.println("Loading Servlet!");
  }

  private int globalVal = 0;

  public void zc(){
    System.out.println("进入方法zc");
  }
%>

<!--我是html的注释-->
<%--我是jsp的注释--%>

  $END$
  </body>
</html>
