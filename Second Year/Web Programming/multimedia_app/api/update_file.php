<?php
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Headers: Content-Type');
header('Access-Control-Allow-Methods: GET, PATCH, OPTIONS');
header('Content-Type: application/json');

if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(200);
    exit();
}


require 'db_connection.php';

// Read the raw POST data
$data = json_decode(file_get_contents('php://input'), true);  // Parsing JSON data

$id     = $data['id']     ?? '';
$title  = $data['title']  ?? '';
$format = $data['format'] ?? '';
$genre  = $data['genre']  ?? '';
$path   = $data['path']   ?? '';

$errors = [];

if (empty($id)) $errors[] = "ID is required.";
if (empty($title)) $errors[] = "Title is required.";
if (empty($format)) $errors[] = "Format is required.";
if (empty($genre)) $errors[] = "Genre is required.";
if (empty($path)) $errors[] = "Path is required.";
if (!preg_match("/^[\w\s\-',.?!]+$/", $title)) $errors[] = "Title contains invalid characters.";

// If errors are found, send them as a response
if ($errors) {
    echo json_encode(['success' => false, 'errors' => $errors]);
    exit();
}

try {
    // Prepare the SQL query to update only the provided fields
    $sql = "UPDATE multimedia_files SET ";
    $params = [];

    // Conditionally add fields to update
    if ($title) {
        $sql .= "title = ?, ";
        $params[] = $title;
    }
    if ($format) {
        $sql .= "format = ?, ";
        $params[] = $format;
    }
    if ($genre) {
        $sql .= "genre = ?, ";
        $params[] = $genre;
    }
    if ($path) {
        $sql .= "path = ?, ";
        $params[] = $path;
    }

    // Remove the trailing comma and add the WHERE clause
    $sql = rtrim($sql, ', ') . " WHERE id = ?";

    // Add the ID to the parameters
    $params[] = $id;

    // Execute the query
    $stmt = $conn->prepare($sql);
    $success = $stmt->execute($params);

    echo json_encode([
        'success' => $success,
        'message' => $success ? 'File updated successfully.' : 'Update failed.'
    ]);
} catch (Exception $e) {
    http_response_code(500); // Internal Server Error
    echo json_encode([
        'success' => false,
        'error' => 'An error occurred while updating the file.',
        'message' => $e->getMessage()
    ]);
}
?>
