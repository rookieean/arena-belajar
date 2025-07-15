<?php include 'db.php'; ?>

<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>Daftar Pengunjung</title>
    <style>
        body { font-family: Arial; margin: 40px; }
        form { margin-bottom: 20px; }
        input, button { padding: 10px; margin: 5px; }
        table { width: 100%; border-collapse: collapse; margin-top: 20px; }
        th, td { padding: 10px; border: 1px solid #ddd; text-align: left; }
    </style>
</head>
<body>
    <h1>Daftar Pengunjung</h1>

    <form action="simpan.php" method="POST">
        <input type="text" name="nama" placeholder="Nama" required>
        <input type="email" name="email" placeholder="Email" required>
        <button type="submit">Simpan</button>
    </form>

    <h2>Data Pengunjung:</h2>
    <table>
        <tr>
            <th>No</th>
            <th>Nama</th>
            <th>Email</th>
        </tr>
        <?php
        $query = mysqli_query($conn, "SELECT * FROM pengunjung");
        $no = 1;
        while ($row = mysqli_fetch_assoc($query)) {
            echo "<tr>
                    <td>{$no}</td>
                    <td>{$row['nama']}</td>
                    <td>{$row['email']}</td>
                  </tr>";
            $no++;
        }
        ?>
    </table>
</body>
</html>
