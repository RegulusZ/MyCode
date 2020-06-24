package com.zc;

import javax.servlet.ServletException;
import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Date;

//中文数据传递
public class CookieDemo03 extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {

        //解决中文乱码
        req.setCharacterEncoding("utf-8");
        resp.setCharacterEncoding("utf-8");
        resp.setContentType("text/html");
        //Cookie, 服务器从客户端获取
        Cookie[] cookies = req.getCookies();   //返回数组，说明cookie可能存在多个
        PrintWriter out = resp.getWriter();

        //判断cookie是否存在
        if(cookies != null){
            //如果存在
            out.write("你上一次访问的时间是:");

            for (Cookie cookie : cookies) {
                if (cookie.getName().equals("name")) {
                    //获取cookie的值
                    out.write(cookie.getValue());
                }
            }
        }
        else {
            out.write("这是您第一次访问本站");
        }

        Cookie cookie = new Cookie("name", "张晨");
        resp.addCookie(cookie);
    }

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        super.doPost(req, resp);
    }
}

