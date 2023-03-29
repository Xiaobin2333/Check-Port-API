<?php


$server = $_GET['server'] ?? null;
$port = $_GET['port'] ?? null;


if (!$server || !$port) {
  http_response_code(400);
  die('server or port is None');
}


$fp = @fsockopen($server, $port, $errno, $errstr, 5);
if ($fp) {
  http_response_code(200);
  echo 'True';
  fclose($fp);
} 
else {
  http_response_code(200);
  echo 'False';
}


if ($errno) {
  http_response_code(500);
  die('Error');
}


?>
