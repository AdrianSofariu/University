# Movie Management Application (C++ Qt)

## Overview

This **C++ Qt** application allows users to manage a list of movies. It features an **Admin Mode** where the administrator can perform CRUD operations (Create, Read, Update, Delete) on the movie list, with support for **Undo** and **Redo** actions. The **User Mode** allows users to browse and explore movies by genre, view movie trailers, access IMDb pages, and create a watchlist. The application supports reading movie data from both **CSV** and **HTML** formats and saves the movie list in memory for efficient usage.

## Features

### Admin Mode
- **CRUD Operations**: Add, update, delete, and view movies in the list.
- **Undo/Redo Support**: All changes made by the admin can be undone or redone.
- **Data Persistence**: Admin can save and load the movie list to/from memory.

### User Mode
- **Movie Browsing**: View all movies and browse them by genre.
- **IMDb Access**: Each movie’s IMDb page is opened for more detailed information.
- **Watchlist**: Users can add movies to their personal watchlist and save it in memory as a file.

### File Support
- **CSV File Import**: Load a list of movies from CSV files.
- **HTML File Import**: Load a list of movies from HTML files.
- **Memory Storage**: The movie list is stored in memory for the session and can be saved or loaded as required.

