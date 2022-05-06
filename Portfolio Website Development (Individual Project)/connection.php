<?php

$servername = "localhost";
$database = "id17271030_corpcontactformdb";
$username = "id17271030_contactformdb";
$password = "1T5h9n8v@@@@@";

// Create connection
$conn = new mysqli($servername, $username, $password, $database);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}


// Check connection
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}
//echo "Connected successfully";

?>
