<html>
<head>
<meta name="viewport" content="width=device-width" />
<title>Motor Control</title>
</head>
        <body>
        DC Motor Direction Control:
        <form method="get" action="gpio_test.php">
                <input type="submit" value="FORWARDS" name="forwards">
                <input type="submit" value="BACKWARDS" name="backwards">
		<input type="submit" value="OFF" name="off">
        </form>
        <?php
        $setmode17 = shell_exec("/usr/local/bin/gpio -g mode 17 out");
	$setmode18 = shell_exec("/usr/local/bin/gpio -g mode 18 out");
        if(isset($_GET['forwards'])){
                shell_exec("/usr/local/bin/gpio -g write 17 1");
                shell_exec("/usr/local/bin/gpio -g write 18 0");
        }
        else if(isset($_GET['backwards'])){
                shell_exec("/usr/local/bin/gpio -g write 17 0");
                shell_exec("/usr/local/bin/gpio -g write 18 1");
        }
	else if(isset($_GET['off'])){
                shell_exec("/usr/local/bin/gpio -g write 17 0");
                shell_exec("/usr/local/bin/gpio -g write 18 0");

        }
        ?>
        </body>
</html>
