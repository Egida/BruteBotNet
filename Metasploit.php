<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $mac = $_POST['MAC'];
    $option = $_POST['Option'];
    $target = $_POST['Target'];

    // Build a data string with the received values
    $data = "$mac::$option::$target";

    // Store the data in a file (you can use a database as well)
    file_put_contents('Meta.io', $data);

    // Respond with a success message
    echo "Data received and stored successfully.";
} elseif ($_SERVER['REQUEST_METHOD'] === 'GET') {
    // Serve the stored data when requested
    if (file_exists('Meta.io')) {
        echo file_get_contents('Meta.io');
    } else {
        echo "No data available.";
    }
}
?>
