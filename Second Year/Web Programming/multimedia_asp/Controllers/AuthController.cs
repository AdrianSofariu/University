using Microsoft.AspNetCore.Mvc;
using multimedia_app_asp.Models;
using multimedia_app_asp.Services.DAL;
using multimedia_app_asp.Services;
using System;

namespace multimedia_app_asp.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class AuthController : ControllerBase
    {
        private readonly UserRepository _userRepository;

        public AuthController(UserRepository userRepository)
        {
            _userRepository = userRepository;
        }

        [HttpPost("register")]
        public IActionResult Register([FromBody] User user)
        {
            if (string.IsNullOrWhiteSpace(user.Username) || string.IsNullOrWhiteSpace(user.PasswordHash))
                return BadRequest(new { message = "Username and password required" });

            try
            {
                var existingUser = _userRepository.GetByUsername(user.Username);
                if (existingUser != null)
                    return Conflict(new { message = "Username already exists" });

                user.PasswordHash = PasswordHelper.HashPassword(user.PasswordHash);
                _userRepository.AddUser(user);

                return Ok(new { message = "User registered successfully" });
            }
            catch (Exception ex)
            {
                return StatusCode(500, new { message = "An error occurred during registration.", detail = ex.Message });
            }
        }

        [HttpPost("login")]
        public IActionResult Login([FromBody] User user)
        {
            if (string.IsNullOrWhiteSpace(user.Username) || string.IsNullOrWhiteSpace(user.PasswordHash))
                return BadRequest(new { message = "Username and password required" });

            try
            {
                var existingUser = _userRepository.GetByUsername(user.Username);
                if (existingUser == null || !PasswordHelper.VerifyPassword(user.PasswordHash, existingUser.PasswordHash))
                {
                    return Unauthorized(new { message = "Invalid username or password" });
                }

                // Create a session
                HttpContext.Session.SetString("UserId", existingUser.Id.ToString());
                HttpContext.Session.SetString("Username", existingUser.Username);

                return Ok(new { message = "Login successful" });
            }
            catch (Exception ex)
            {
                return StatusCode(500, new { message = "An error occurred during login.", detail = ex.Message });
            }
        }

        [HttpPost("logout")]
        public IActionResult Logout()
        {
            try
            {
                HttpContext.Session.Clear();
                return Ok(new { message = "Logged out" });
            }
            catch (Exception ex)
            {
                return StatusCode(500, new { message = "An error occurred during logout.", detail = ex.Message });
            }
        }
    }
}
