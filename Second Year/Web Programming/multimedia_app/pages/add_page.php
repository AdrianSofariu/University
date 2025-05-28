<!DOCTYPE html>
<html lang="en">
<head>
    <title>Add File</title>
    <link rel="stylesheet" href="../styles.css">
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>
<h2>Add Multimedia File</h2>

<form id="addForm">
    <div class="form-row">
        <label for="title">Title:</label>
        <input type="text" id="title" name="title" required>
    </div>

    <div class="form-row">
        <label for="format">Format:</label>
        <input type="text" id="format" name="format" required>
    </div>

    <div class="form-row">
        <label for="genre">Genre:</label>
        <input type="text" id="genre" name="genre" required>
    </div>

    <div class="form-row">
        <label for="path">Path:</label>
        <input type="text" id="path" name="path" required>
    </div>

    <div class="form-actions">
        <button type="submit">Add</button>
    </div>
</form>

<a href="../index.php">Back</a>

<script>
    // Event listener for the form submission
    $('#addForm').on('submit', function(e) {
        e.preventDefault();  // Prevent the default form submission

        // Collect the form data
        const title = $('#title').val().trim();
        const format = $('#format').val().trim();
        const genre = $('#genre').val().trim();
        const path = $('#path').val().trim();

        // Validate inputs before sending
        let errorMsg = '';
        if (!title) errorMsg += 'Title is required.\n';
        if (!format) errorMsg += 'Format is required.\n';
        if (!genre) errorMsg += 'Genre is required.\n';
        if (!path) errorMsg += 'Path is required.\n';

        if (errorMsg) {
            alert(errorMsg);
            return;
        }

        // Send the form data via AJAX as a JSON object
        $.ajax({
            url: '../api/add_file.php',  // The backend PHP file to handle the form submission
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({
                title: title,
                format: format,
                genre: genre,
                path: path
            }),
            success: function(response) {
                if (response.success) {
                    alert(response.message);
                    window.location.href = '../index.php';  // Redirect after successful submission
                } else {
                    alert('Error: ' + response.errors.join('\n'));  // Show errors if any
                }
            },
            error: function(xhr, status, error) {
                alert('Error: ' + error);  // Handle AJAX request error
            }
        });
    });
</script>

</body>
</html>
