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
    $genre = $_GET['genre'] ?? '';

    $query = $genre
        ? "SELECT * FROM multimedia_files WHERE genre = ?"
        : "SELECT * FROM multimedia_files";

    $stmt = $conn->prepare($query);

    $stmt->execute($genre ? [$genre] : []);
    $files = $stmt->fetchAll(PDO::FETCH_ASSOC);

    echo json_encode([
        'success' => true,
        'data' => $files
    ]);
} catch (Exception $e) {
    http_response_code(500);
    echo json_encode([
        'success' => false,
        'error' => 'Server error: ' . $e->getMessage()
    ]);
}
?>

