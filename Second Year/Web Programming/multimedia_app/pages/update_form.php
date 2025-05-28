<!DOCTYPE html>
<html>
<head>
    <title>Edit File</title>
    <link rel="stylesheet" href="../styles.css">
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>
<h2>Edit Multimedia File</h2>

<!-- Form for editing file -->
<form id="editForm">
    <input type="hidden" name="id" id="fileId">

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
        <button type="submit">Update</button>
    </div>
</form>

<a href="../index.php">Back</a>

<script>
    $(document).ready(function() {
        // Fetch file data by ID from the URL
        var fileId = new URLSearchParams(window.location.search).get('id');
        
        // Make an AJAX call to fetch the file data
        $.ajax({
            url: '../api/get_file.php',  // Endpoint to fetch the file by ID
            type: 'GET',
            data: { id: fileId },
            dataType: 'json',
            success: function(response) {
                if (response.success) {
                    // Populate the form fields with the data
                    $('#fileId').val(response.file.id);
                    $('#title').val(response.file.title);
                    $('#format').val(response.file.format);
                    $('#genre').val(response.file.genre);
                    $('#path').val(response.file.path);
                } else {
                    alert('Error: ' + response.error);
                }
            },
            error: function(xhr, status, error) {
                alert('Error: ' + error);
            }
        });

        // Handle form submission via AJAX
        $('#editForm').on('submit', function(e) {
            e.preventDefault();  // Prevent the default form submission

            var formData = {
                id: $('#fileId').val(),
                title: $('#title').val(),
                format: $('#format').val(),
                genre: $('#genre').val(),
                path: $('#path').val()
            };

            // Send data as JSON
            $.ajax({
                url: '../api/update_file.php',  // Endpoint to update the file
                type: 'POST',
                contentType: 'application/json',  // Sending data as JSON
                data: JSON.stringify(formData),  // Convert the form data to JSON
                dataType: 'json',
                success: function(response) {
                    if (response.success) {
                        alert(response.message);  // Success message
                        window.location.href = '../index.php';  // Redirect after success
                    } else {
                        alert('Error: ' + response.errors.join('\n'));  // Show error messages
                    }
                },
                error: function(xhr, status, error) {
                    alert('Error: ' + error);  // Handle errors
                }
            });
        });
    });
</script>

</body>
</html>
