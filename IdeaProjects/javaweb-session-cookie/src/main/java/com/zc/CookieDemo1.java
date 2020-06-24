package com.zc;

import javax.servlet.ServletException;
import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Date;

//保存用户上一次访问的时间
public class CookieDemo1 extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
//        super.doGet(req, resp);
        //服务器把你说上次来的时间封装为一个时间，你下次带来，就知道是你

        //解决中文乱码
        req.setCharacterEncoding("utf-8");
        resp.setCharacterEncoding("utf-8");
        resp.setContentType("text/html");


        PrintWriter out = resp.getWriter();

        //Cookie, 服务器从客户端获取
        Cookie[] cookies = req.getCookies();   //返回数组，说明cookie可能存在多个

        //判断cookie是否存在
        if(cookies != null){
            //如果存在
            out.write("你上一次访问的时间是:");

            for (Cookie cookie : cookies) {
                if (cookie.getName().equals("lastLoginTime")) {
                    //获取cookie的值
                    long lastLoginTime = Long.parseLong(cookie.getValue());
                    Date date = new Date(lastLoginTime);
                    out.write(date.toLocaleString());
                }
            }
        }
        else {
            out.write("这是您第一次访问本站");
        }

        //服务器给客户端响应一个cookie
        Cookie cookie = new Cookie("lastLoginTime", String.valueOf((System.currentTimeMillis())));

        //cookie有效期为1天
        cookie.setMaxAge(24*60*60);

        resp.addCookie(cookie);
    }

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
//        super.doPost(req, resp);

    }
}
