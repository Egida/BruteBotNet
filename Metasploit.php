<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Store the received data in a file or database
    $mac = $_POST['MAC'];
    $option = $_POST['Option'];
    
    // Store the data in a file (you can use a database as well)
    $data = "$mac::$option";
    file_put_contents('Meta.io', $data);
} elseif ($_SERVER['REQUEST_METHOD'] === 'GET') {
    // Serve the stored data when requested
    if (file_exists('Meta.io')) {
        echo file_get_contents('Meta.io');
    } else {
        echo "No data available.";
    }
}
?>
