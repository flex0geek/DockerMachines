<?php

session_start();
if( $_SESSION['loggedin'] != 1){
	header("Location: index.php");
}

include 'database.php';
$uname = $_SESSION['username'];
$email = $_SESSION['email'];

$sql = "SELECT * FROM users where username='$uname'";
// echo $sql;
if( $result = $mysqli->query($sql) ){
	$data = mysqli_fetch_array($result);
	// print_r($data);
	$fullname= $data[0];
	$username = $data[1];
	$email = $data[3];
}
	// echo "test";

?>

<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="stylesheet" type="text/css" href="./css/style.css">
	<title>Profile</title>
</head>
<body>
	<center>
		<h1><?php echo "Welcome ".$username; ?></h1>
		<h1><?php echo "Fullname: ".$fullname; ?></h1>
		<h1><?php echo "E-Mail: ".$email; ?></h1>

		<a id=logout href="/logout.php">Logout</a>
	</center>
</body>
</html>