<?php
require("connection.php");
$compname = $_POST["compname"];
$email = $_POST["email"];
$password = $_POST["password"];

$preparedStatement = $conn->prepare("INSERT into user(compName, userEmail, userPassword) VALUES(?,?,?);");
$preparedStatement->bind_param("sss", $compname, $email, $password);
$preparedStatement->execute();

$preparedStatement = $conn->prepare("SELECT * FROM user;");
$preparedStatement->execute();
$result = $preparedStatement->get_result();
if ($result->num_rows > 0) {
    while ($row = $result->fetch_assoc()) {
        $data[] = $row;
    }
    echo json_encode($data);
} else {
    echo 0;
}
$conn->close();