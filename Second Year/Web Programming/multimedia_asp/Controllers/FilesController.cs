using Microsoft.AspNetCore.Mvc;
using multimedia_app_asp.Models;
using multimedia_app_asp.Services.DAL;
using multimedia_app_asp.Filters;
using System;

namespace multimedia_app_asp.Controllers
{
    [Authenticated]  // Protect all actions here
    public class FilesController : Controller
    {
        private readonly FileRepository _fileRepository;

        public FilesController(FileRepository fileRepository)
        {
            _fileRepository = fileRepository;
        }

        // GET: /Files/Index
        public IActionResult Index(string? genreFilter)
        {
            try
            {
                int userId = Convert.ToInt32(HttpContext.Session.GetString("UserId"));
                var files = _fileRepository.GetAll(userId);

                if (!string.IsNullOrEmpty(genreFilter))
                {
                    files = files.FindAll(f => f.Genre == genreFilter);
                }

                ViewBag.Genres = _fileRepository.GetGenres();
                ViewBag.PreviousFilter = TempData["CurrentFilter"] as string ?? "--";
                ViewBag.CurrentFilter = genreFilter ?? "All Genres";
                TempData["CurrentFilter"] = ViewBag.CurrentFilter;

                return View(files);
            }
            catch (Exception ex)
            {
                return StatusCode(500, "An error occurred while loading files.");
            }
        }

        // GET: /Files/Details/{id}
        public IActionResult Details(int id)
        {
            try
            {
                var file = _fileRepository.GetById(id);
                if (file == null) return NotFound();

                return View(file);
            }
            catch (Exception ex)
            {
                return StatusCode(500, "An error occurred while loading file details.");
            }
        }

        // GET: /Files/Create
        public IActionResult Create()
        {
            return View();
        }

        // POST: /Files/Create
        [HttpPost]
        [ValidateAntiForgeryToken]
        public IActionResult Create(MultimediaFile file)
        {
            if (!ModelState.IsValid)
                return View(file);

            try
            {
                int userId = Convert.ToInt32(HttpContext.Session.GetString("UserId"));
                _fileRepository.Insert(file, userId);
                return RedirectToAction(nameof(Index));
            }
            catch (Exception ex)
            {
                ModelState.AddModelError("", "Failed to create file.");
                return View(file);
            }
        }

        // GET: /Files/Edit/{id}
        public IActionResult Edit(int id)
        {
            try
            {
                var file = _fileRepository.GetById(id);
                if (file == null) return NotFound();

                return View(file);
            }
            catch (Exception ex)
            {
                return StatusCode(500, "An error occurred while loading the edit page.");
            }
        }

        // POST: /Files/Edit/{id}
        [HttpPost]
        [ValidateAntiForgeryToken]
        public IActionResult Edit(MultimediaFile file)
        {
            if (!ModelState.IsValid)
                return View(file);

            try
            {
                _fileRepository.Update(file);
                return RedirectToAction(nameof(Index));
            }
            catch (Exception ex)
            {
                ModelState.AddModelError("", "Failed to update file.");
                return View(file);
            }
        }

        // GET: /Files/Delete/{id}
        public IActionResult Delete(int id)
        {
            try
            {
                var file = _fileRepository.GetById(id);
                if (file == null) return NotFound();

                return View(file);
            }
            catch (Exception ex)
            {
                return StatusCode(500, "An error occurred while loading the delete page.");
            }
        }

        // POST: /Files/Delete/{id}
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public IActionResult DeleteConfirmed(int id)
        {
            try
            {
                _fileRepository.Delete(id);
                return RedirectToAction(nameof(Index));
            }
            catch (Exception ex)
            {
                return StatusCode(500, "Failed to delete file.");
            }
        }
    }
}
