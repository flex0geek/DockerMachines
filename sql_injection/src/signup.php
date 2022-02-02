<?php
session_start();
if( $_SERVER['REQUEST_METHOD'] != "POST" ){
	header("Location: /index.php");
}
include 'database.php';

$fname = mysqli_real_escape_string($mysqli, $_POST['fname']);
$uname = mysqli_real_escape_string($mysqli, $_POST['uname']);
$email = mysqli_real_escape_string($mysqli, $_POST['email']);
$paswd = mysqli_real_escape_string($mysqli, $_POST['psw']);

$sql = "INSERT INTO users VALUES('$fname','$uname','$paswd','$email')";
// echo $uname;
if( $result = $mysqli->query($sql) ){
	header("Location: /index.php?msg=Account Created.");
}else{
	header("Location: /index.php?msg=Username Wrong");
}