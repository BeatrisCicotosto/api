<?php

    $db_host = "localhost";
    $db_user = "root";
    $db_password = "";
    $db_name = "formulario";

    $conexao = new mysqli($db_host,$db_user,$db_password,$db_name);

    if($conexao->connect_errno){
        echo "Erro" . $conexao->connect_error;
    } else {
        echo"Conexão efetuada com sucesso";
    }
?>