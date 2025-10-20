<?php
$servername = "db";
$username = "sgssi_user";
$password = "sgssi_password";
$dbname = "sgssi_db";

// Crear conexión
$conn = new mysqli($servername, $username, $password, $dbname);

// Verificar conexión
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $nombre = $_POST['nombre'];
    $apellidos = $_POST['apellidos'];
    $dni = $_POST['dni'];
    $telefono = $_POST['telefono'];
    $fecha_nacimiento = $_POST['fecha_nacimiento'];
    $email = $_POST['email'];
    $username = $_POST['username'];
    $password_hash = password_hash($_POST['password'], PASSWORD_DEFAULT);
    
    $sql = "INSERT INTO usuarios (nombre, apellidos, dni, telefono, fecha_nacimiento, email, username, password) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)";
    
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("ssssssss", $nombre, $apellidos, $dni, $telefono, $fecha_nacimiento, $email, $username, $password_hash);
    
    if ($stmt->execute()) {
        header("Location: login.html?registro=exitoso");
    } else {
        echo "Error: " . $stmt->error;
    }
    
    $stmt->close();
}

$conn->close();
?>