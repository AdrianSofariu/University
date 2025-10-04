package filters;

import javax.servlet.*;
import javax.servlet.annotation.WebFilter;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import java.io.IOException;

@WebFilter(urlPatterns = {"/dashboard", "/game/*", "/ships/*", "/profile/*"}) // Apply to all protected paths
public class AuthFilter implements Filter {

    @Override
    public void init(FilterConfig filterConfig) throws ServletException {
    }

    @Override
    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain)
            throws IOException, ServletException {
        HttpServletRequest req = (HttpServletRequest) request;
        HttpServletResponse res = (HttpServletResponse) response;

        HttpSession session = req.getSession(false); // Don't create a new session

        boolean loggedIn = (session != null && session.getAttribute("loggedInUser") != null);
        String loginURI = req.getContextPath() + "/login";
        String registerURI = req.getContextPath() + "/register";

        boolean isLoginRequest = req.getRequestURI().equals(loginURI);
        boolean isRegisterRequest = req.getRequestURI().equals(registerURI);
        boolean isLoginPage = req.getRequestURI().endsWith("login.jsp");
        boolean isRegisterPage = req.getRequestURI().endsWith("register.jsp");

        if (loggedIn || isLoginRequest || isRegisterRequest || isLoginPage || isRegisterPage) {
            chain.doFilter(request, response); // User is logged in or requesting login/registration
        } else {
            res.sendRedirect(loginURI); // Redirect to login page
        }
    }

    @Override
    public void destroy() {
        // Cleanup code if needed
    }
}