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

$id = $_GET['id'] ?? '';

if (!$id) {
    http_response_code(400);
    echo json_encode(['success' => false, 'error' => 'Missing ID']);
    exit;
}

try {
    // Prepare the SELECT query
    $stmt = $conn->prepare("SELECT * FROM multimedia_files WHERE id = ?");
    $stmt->execute([$id]);
    $file = $stmt->fetch(PDO::FETCH_ASSOC);

    // Check if the file exists in the database
    if ($file) {
        echo json_encode(['success' => true, 'file' => $file]);  // Return the file data as JSON with success status
    } else {
        http_response_code(404);  // File not found
        echo json_encode(['success' => false, 'error' => 'File not found']);
    }
} catch (Exception $e) {
    // Catch any general exceptions and return a JSON error message
    http_response_code(500);
    echo json_encode(['success' => false, 'error' => 'An unexpected error occurred: ' . $e->getMessage()]);
}
?>
