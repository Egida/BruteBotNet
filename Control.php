<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Handle data received from the Python script
    $data = $_POST['data'];
    file_put_contents('Data.io', $data); // Save the data to a file
    echo "[+] executed successfully.\n";
} else if ($_SERVER['REQUEST_METHOD'] === 'GET') {
    // Handle requests from the target Python script
    $data = file_get_contents('Data.io');
    if (!empty($data)) {
        // Data is available; send it to the target script
        echo $data;
    } else {
        // No data available
        echo "No data available.\n";
    }
}
?>
