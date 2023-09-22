<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $data = $_POST;

    $timestamp = time();
    $file_path = "data_$timestamp.txt";

    $file = fopen($file_path, "w");

    if ($file) {
        fwrite($file, json_encode($data, JSON_PRETTY_PRINT));

        fclose($file);

        echo "Data received and saved successfully in $file_path";
    } else {
        echo "Failed to open the file for writing.";
    }
} else {
    echo "No POST Requests Found.";
}
?>
