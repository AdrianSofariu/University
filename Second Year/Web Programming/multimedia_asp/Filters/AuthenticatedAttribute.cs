using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Filters;

namespace multimedia_app_asp.Filters
{
    public class AuthenticatedAttribute : ActionFilterAttribute
    {
        public override void OnActionExecuting(ActionExecutingContext context)
        {
            var userId = context.HttpContext.Session.GetString("UserId");
            if (string.IsNullOrEmpty(userId))
            {
                context.Result = new UnauthorizedResult();
            }
            base.OnActionExecuting(context);
        }
    }
}
