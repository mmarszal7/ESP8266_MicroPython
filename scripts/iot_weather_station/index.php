<?php

    $host = 'localhost';
	$login = '';
	$password = '';
	$db = 'grafana';
	$connection = new mysqli($host, $login, $password, $db);
    
    $method = $_SERVER['REQUEST_METHOD'];
    switch ($method) 
    {
        case 'GET':
        {
            try
            {
                $temperature = $_GET['temperature'];
                $humidity = $_GET['humidity'];
            
                $connection->query("INSERT INTO data (temperature, humidity) VALUES ('$temperature', '$humidity')");
                echo '200';
            }
            catch (Exception $e)
            {
                echo $e;
            }
            
            break;
        }
    }
