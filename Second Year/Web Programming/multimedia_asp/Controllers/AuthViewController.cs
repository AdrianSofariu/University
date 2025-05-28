using Microsoft.AspNetCore.Mvc;

namespace multimedia_app_asp.Controllers
{
    public class AuthViewController : Controller
    {
        // GET: /Auth/Login
        public IActionResult Login()
        {
            return View();
        }

        // GET: /Auth/Register
        public IActionResult Register()
        {
            return View();
        }
    }
}
