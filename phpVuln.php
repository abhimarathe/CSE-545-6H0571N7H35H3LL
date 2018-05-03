
<?php

$name = $_GET['name']
echo $name

$offset = $_GET['offset']; 
$query  = "SELECT id, name FROM products ORDER BY name LIMIT 20 OFFSET $offset;";
$result = pg_query($conn, $query);

?>
