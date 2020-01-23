<?php
$distance = $_POST["distance"];
$price = $_POST["price"];
$quantity = $_POST["quantity"];
$con=mysqli_connect("localhost","root","");
if(!$con)
die("connection unsuccesful");
$dbstatus = mysqli_select_db($con,"project");
if(!$dbstatus)
die("database not found");
$sql = "insert into project1 
values('$distance','$price','$quantity')";
$status = mysqli_query($con,$sql);
if($status)
echo "Record inserted successfully";
else
echo "TRY AGAIN";
?>
