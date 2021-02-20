function insertAnswers() {
var express = require("express");
var mysql = require('mysql');
var app = express();
var connection = mysql.createConnection({
    //properties
    host: "localhost",
    user: "root",
    password: "password",
    database: "matching",
});

connection.connect(function (error) {
    if(!!error) {
        console.log(error);
    }
    else
    console.log("connected");});
    connection
    connection.query('INSERT INTO candidate (fname, lname, email) VALUES("john", "doe",  "john@gmail.com");', (err, rows) => {
        if(err) {
            throw err;
        }
        else
        {console.log("received");
        console.log(rows);}
    });
    connection.end((err) => {
        // The connection is terminated gracefully
        // Ensures all remaining queries are executed
        // Then sends a quit packet to the MySQL server.
        console.log("connection end");
      });

    }
