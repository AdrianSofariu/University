<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Multimedia Collection</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Multimedia Collection</h1>
    
    <div id="listControls">
        <div id="filterControls">
            <!-- Genre selection dropdown -->
            <label for="genre">Select Genre:</label>

            <select id="genre" name="genre" onchange="fetchByGenre()">
                <option value="">All Genres</option>
            </select>

            <!-- Display the previous genre -->
            <p>Previous genre: <span id="prevFilter">--</span></p>

            <!-- Display the selected genre -->
            <p>Last selected genre: <span id="currentFilter">All Genres</span></p>
        </div>
        <!-- Button to add new file -->
        <a href="pages/add_page.php">Add New File</a>
    </div>

    <!-- List of multimedia files -->
    <ul id="fileList"></ul>

    <!-- Link to External JS file -->
    <script src="index_script.js"></script>
</body>
</html>
