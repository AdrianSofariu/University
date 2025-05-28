<?php
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Headers: Content-Type');
header('Access-Control-Allow-Methods: GET, POST, OPTIONS');
header('Content-Type: application/json');

if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(200);
    exit();
}

require 'db_connection.php';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Get POST data
    $data = json_decode(file_get_contents('php://input'), true);

    $title  = $data['title']  ?? '';
    $format = $data['format'] ?? '';
    $genre  = $data['genre']  ?? '';
    $path   = $data['path']   ?? '';

    // Validate inputs
    $errors = [];
    if (empty($title)) $errors[] = "Title is required.";
    if (empty($format)) $errors[] = "Format is required.";
    if (empty($genre)) $errors[] = "Genre is required.";
    if (empty($path)) $errors[] = "Path is required.";
    if (!preg_match("/^[\w\s\-',.!?]+$/", $title)) $errors[] = "Title contains invalid characters.";

    if (!empty($errors)) {
        echo json_encode(['success' => false, 'errors' => $errors]);
        exit();
    }

    try {
        // Prepare the INSERT query
        $stmt = $conn->prepare("INSERT INTO multimedia_files (title, format, genre, path) VALUES (?, ?, ?, ?)");
        $stmt->execute([$title, $format, $genre, $path]);

        echo json_encode(['success' => true, 'message' => 'File added successfully.']);
    } catch (Exception $e) {
        echo json_encode(['success' => false, 'error' => 'An unexpected error occurred: ' . $e->getMessage()]);
    }
}
?>
