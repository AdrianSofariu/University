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

try {
    // Fetch unique genres from the database
    $stmt = $conn->query("SELECT DISTINCT genre FROM multimedia_files");

    if ($stmt) {
        // Fetch results
        $genres = $stmt->fetchAll(PDO::FETCH_ASSOC);
        
        // Return genres as JSON with success status
        echo json_encode([
            'success' => true,
            'data' => $genres
        ]);
    } else {
        // Handle query failure
        http_response_code(500);
        echo json_encode([
            'success' => false,
            'error' => 'Failed to retrieve genres.'
        ]);
    }
} catch (Exception $e) {
    // Handle exceptions such as connection issues
    http_response_code(500);
    echo json_encode([
        'success' => false,
        'error' => 'Server error: ' . $e->getMessage()
    ]);
}
?>

