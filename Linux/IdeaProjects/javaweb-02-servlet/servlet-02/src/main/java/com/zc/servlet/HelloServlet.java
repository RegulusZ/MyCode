package com.zc.servlet;

import javax.servlet.ServletContext;
import javax.servlet.ServletException;
import javax.servlet.http.*;
import java.io.IOException;
import java.io.PrintWriter;

public class HelloServlet extends HttpServlet {

    //  由于get或者post只是请求实现的不同方式，可以相互调用，业务逻辑都一样
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
//        super.doGet(req, resp);

        //this.getInitParameter()    初始化参数
//        this.getServletConfig()  servlet配置
        //this.getServletContext()   获取servlet上下文
        ServletContext context = this.getServletContext();

        String username = "zhangchen";
        context.setAttribute("username", username);

        System.out.println("hello");
    }



}
