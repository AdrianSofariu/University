<?php
// CORS headers
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Headers: Content-Type');
header('Access-Control-Allow-Methods: GET, DELETE, OPTIONS');
header('Content-Type: application/json');

// Handle preflight request
if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(200);
    exit();
}

require 'db_connection.php';

$id = $_GET['id'] ?? '';

// Ensure the ID is valid
if (empty($id)) {
    echo json_encode(['success' => false, 'message' => 'Invalid file ID']);
    exit();
}

try {
    // Prepare and execute the DELETE query
    $stmt = $conn->prepare("DELETE FROM multimedia_files WHERE id = ?");
    $stmt->execute([$id]);

    // Check if any row was affected (i.e., file was deleted)
    if ($stmt->rowCount() > 0) {
        echo json_encode(['success' => true, 'message' => 'File deleted successfully']);
    } else {
        echo json_encode(['success' => false, 'message' => 'File not found']);
    }
} catch (Exception $e) {
    echo json_encode([
        'success' => false,
        'message' => 'Error: ' . $e->getMessage()
    ]);
}
?>
