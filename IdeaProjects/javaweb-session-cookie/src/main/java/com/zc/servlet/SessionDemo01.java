package com.zc.servlet;

import com.zc.pojo.Person;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import java.io.IOException;

//获取并输出session的id
public class SessionDemo01 extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        //解决乱码问题
        resp.setContentType("text/html;charset=utf-8");
        resp.setCharacterEncoding("utf-8");
        req.setCharacterEncoding("utf-8");

        //得到session
        HttpSession session = req.getSession();

        //给session存东西
        session.setAttribute("name", new Person("张晨", 25));

        //获取session的id
        String id = session.getId();

        //判断是不是新的session
        if (session.isNew()) {
            resp.getWriter().write("session创建成功，ID:" + id);
        }
        else{
            resp.getWriter().write("session已存在，ID:" + id);
        }
    }

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        super.doPost(req, resp);
    }
}
