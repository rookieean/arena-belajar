<?php
include 'db.php';

$nama  = $_POST['nama'];
$email = $_POST['email'];

$query = "INSERT INTO pengunjung (nama, email) VALUES ('$nama', '$email')";

if (mysqli_query($conn, $query)) {
    header("Location: index.php");
} else {
    echo "Gagal menyimpan data: " . mysqli_error($conn);
}
?>
