
var express = require("express");
var mysql = require('mysql');
var app = express();

const cors = require("cors")
app.use(cors());
app.use(express.json());
app.listen(5500, () => {
    console.log("server started at", 5500);
});

app.post('/candidateData', (req, res) => {
    const userData = req.body;
    console.log(`recieved data: ${typeof(userData.firstName)}\n`);

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
    connection.query(`INSERT INTO candidate (fname, lname, email) VALUES("${userData.firstName}", "${userData.lastName}",  "${userData.email}");`, (err, rows) => {
        if(err) {
            throw err;
        }
        else
        {console.log(`inserted user with email ${userData.email}`);
        console.log(rows);}
    });
    connection.end((err) => {
        // The connection is terminated gracefully
        // Ensures all remaining queries are executed
        // Then sends a quit packet to the MySQL server.
        console.log("connection end");
      });

    
    });