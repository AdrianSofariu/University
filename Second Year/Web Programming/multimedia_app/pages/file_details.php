<!DOCTYPE html>
<html lang="en">
<head>
    <title>File Details</title>
    <link rel="stylesheet" href="../styles.css">
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>
    <h1>File Details</h1>

    <div class="file-details">
        <!-- These elements will be dynamically populated -->
        <p><strong>Title:</strong> <span id="fileTitle"></span></p>
        <p><strong>Format:</strong> <span id="fileFormat"></span></p>
        <p><strong>Genre:</strong> <span id="fileGenre"></span></p>
        <p><strong>Path:</strong> <span id="filePath"></span></p>
    </div>

    <a href="../index.php">Back to the list</a>

    <script>
        $(document).ready(function() {
            // Get the file ID from the URL
            var fileId = new URLSearchParams(window.location.search).get('id');
            
            // Check if the file ID exists in the URL
            if (!fileId) {
                alert('File ID is missing.');
                return;
            }

            // AJAX call to fetch the file details by ID
            $.ajax({
                url: '../api/get_file.php',  // Endpoint to get file details
                type: 'GET',
                data: { id: fileId },
                dataType: 'json',
                success: function(response) {
                    if (response.success) {
                        // Populate the file details into the HTML elements
                        $('#fileTitle').text(response.file.title);
                        $('#fileFormat').text(response.file.format);
                        $('#fileGenre').text(response.file.genre);
                        $('#filePath').text(response.file.path);
                    } else {
                        alert('Error: ' + response.error);  // Error handling
                    }
                },
                error: function(xhr, status, error) {
                    alert('Error: ' + error);  // Handle AJAX errors
                }
            });
        });
    </script>

</body>
</html>
