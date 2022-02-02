<?php
session_start();
if( $_SERVER['REQUEST_METHOD'] != "POST" ){
	header("Location: /index.php");
}
include 'database.php';

$uname = mysqli_real_escape_string($mysqli, $_POST['uname']);
$paswd = $_POST['psw'];

#mysqli_real_escape_string($mysqli, 

$sql = "SELECT * FROM users where username='$uname' and password='$paswd'";
// echo $sql;
if( $result = $mysqli->query($sql) ){
	$data = mysqli_fetch_array($result);
	// print_r($data);
	if($data[2]){
		$_SESSION['username'] = $data[1];
		$_SESSION['email'] = $data[3];
		$_SESSION['loggedin'] = 1;
		header("Location: /profile.php");
	}else{
		header("Location: /index.php?msg=Username/Password is wrong");
	}
}