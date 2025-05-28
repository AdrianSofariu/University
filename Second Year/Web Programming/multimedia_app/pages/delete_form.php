<!DOCTYPE html>
<html>
<head>
    <title>Delete File</title>
    <link rel="stylesheet" href="../styles.css">
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>
<div id="centerDiv">
    <h2>Are you sure you want to delete this file?</h2>
    <form id="deleteForm">
        <button type="submit">Yes, Delete</button>
    </form>
    <a id="backHref" href="../index.php">Cancel</a>
</div>

<script>
    // Event handler for form submission
    $('#deleteForm').on('submit', function(e) {
        e.preventDefault(); // Prevent the default form submission

        var fileId = new URLSearchParams(window.location.search).get('id'); // Get the 'id' from the URL
        
        $.ajax({
            url: '../api/delete_file.php?id=' + fileId, // Send the ID via GET parameter
            type: 'POST',
            success: function(response) {
                if (response.success) {
                    alert(response.message);  // Success message
                    window.location.href = '../index.php';  // Redirect after deletion
                } else {
                    alert(response.message);  // Error message
                }
            },
            error: function(xhr, status, error) {
                alert('Error: ' + error);  // Handle any errors from the request
            }
        });
    });
</script>

</body>
</html>
