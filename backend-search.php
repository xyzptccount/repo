<?php
header("Access-Control-Allow-Origin: *");
/* Attempt MySQL server connection. Assuming you are running MySQL

server with default setting (user 'root' with no password) */

$link = mysqli_connect("localhost", "dvitt90", "", "c9");
$returnArray = array();
$returnArraytwo = array();
$returnArraythree = array();
$returnArrayfour = array();
$mainReturn = array();

// Check connection

if($link === false){

    die("ERROR: Could not connect. " . mysqli_connect_error());

}

 
$de = json_decode($_GET['term']);
// Escape user inputs for security

$term = mysqli_real_escape_string($link, $de);

 

if(isset($term)){

    // Attempt select query execution

    $sql = "SELECT * FROM fabItems WHERE itemName LIKE '" . $term . "%'";
    $sqltwo = "SELECT * FROM fabItems WHERE itemNumber LIKE '" . $term . "%'";
    
    if($result = mysqli_query($link, $sql)){

        if(mysqli_num_rows($result) > 0){
            
            $i = 0;
            
            while($row = mysqli_fetch_array($result)){
                array_push($returnArray, array($row['itemLink'], $row['itemNumber'], $row['itemName'], $row['itemSupplier']));
                if($i == 2){
                    break;
                }
                $i = $i + 1;

            }
            // Close result set
            
            mysqli_free_result($result);

        } elseif($resulttwo = mysqli_query($link, $sqltwo)){
            $i = 0;
            
            while($row = mysqli_fetch_array($resulttwo)){
                array_push($returnArraytwo, array($row['itemLink'], $row['itemNumber'], $row['itemPrice'], $row['itemSupplier']));
                if($i == 2){
                    break;
                }
                $i = $i + 1;

            }
            // Close result set
            
            mysqli_free_result($resulttwo);

        }

    } else{

        echo "ERROR: Could not able to execute $sql. " . mysqli_error($link);

    }
    if(sizeof($returnArray) > 0){
        array_push($mainReturn, $returnArray);
    }elseif(sizeof($returnArraytwo) > 0){
        array_push($mainReturn, $returnArraytwo);
    }
}

if(isset($term)){

    // Attempt select query execution

    $sqlthree = "SELECT * FROM priceDB WHERE itemName LIKE '" . $term . "%'";
    $sqlfour = "SELECT * FROM priceDB WHERE itemNumber LIKE '" . $term . "%'";
    
    if($resultthree = mysqli_query($link, $sqlthree)){

        if(mysqli_num_rows($resultthree) > 0){
            
            $i = 0;
            
            while($row = mysqli_fetch_array($resultthree)){
                array_push($returnArraythree, array($row['itemLink'], $row['itemNumber'], $row['itemName'], $row['itemSupplier']));
                if($i == 2){
                    break;
                }
                $i = $i + 1;

            }
            // Close result set
            
            mysqli_free_result($resultthree);

        } elseif($resultfour = mysqli_query($link, $sqlfour)){
            $i = 0;
            
            while($row = mysqli_fetch_array($resultfour)){
                array_push($returnArrayfour, array($row['itemLink'], $row['itemNumber'], $row['itemPrice'], $row['itemSupplier']));
                if($i == 2){
                    break;
                }
                $i = $i + 1;

            }
            // Close result set
            
            mysqli_free_result($resultfour);

        }

    } else{

        echo "ERROR: Could not able to execute $sql. " . mysqli_error($link);

    }
    if(sizeof($returnArraythree) > 0){
        array_push($mainReturn, $returnArraythree);
    }elseif(sizeof($returnArrayfour) > 0){
        array_push($mainReturn, $returnArrayfour);
    }
}

if(sizeof($mainReturn) > 0){
    echo $_GET['callback'] . json_encode($mainReturn);
}else {
    echo $_GET['callback'] . json_encode('<p>No matches found</p>');
}


// close connection

mysqli_close($link);

 //echo $send; //"<li><p><a href='" . $row['itemLink'] . "'>" . $row['itemNumber'] .  "</a>" . " | " . $row['itemPrice'] . "</p></li>";
//else{
    //array_push($mainReturn, "<p>No matches found</p>");
//}
?>