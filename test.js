//const { request } = require("express");

// if answers are not fully filled, alert, or else record
function check() {
    var reqLength = 1;
    allArrayElements = Array.from(document.querySelector("#email-form").elements);
    first = document.getElementById("fname").value;
    last = document.getElementById("lname").value; 
    email = document.getElementById("email").value;
    var len = allArrayElements.filter(element => element.checked).length;

    if (len == reqLength && first != null && last != null && email != null)
    {
    var userAnswer = record(allArrayElements, [first, last, email]);
    


    // give the result to database
    const emailurl = new URL("http://localhost:5500/email");
    const emailoption = {
        method: 'POST',
        headers: {
            'Content-Type' : 'application/json'
        },
        body: userAnswer
    }
    console.log(userAnswer);
    fetch(emailurl, emailoption);
    

    // check if the result already exists
    var emailRepeat = null;
    const checkurl = new URL("http://localhost:5500/check"); 
    console.log("reached");
    const request = () => {
    const Eresponse = fetch(checkurl)
    .then(response => {return response.text();})
    .then(data => {
        emailStatus = data;
        /* for (var key in data) {
            if (data.hasOwnProperty(key))
            {emailStatus = data[key];}
        } */
         console.log("22 ", emailStatus);
         emailRepeat = emailStatus[emailStatus.length - 3];
         console.log("happened");
        console.log("the status is " + emailRepeat);
    });

    console.log("reached 2nd point");

 


    const url = new URL("http://localhost:5500/candidateData");
    const option = {
        method: 'POST',
        headers: {
            'Content-Type' : 'application/json'
        },
        body: userAnswer
    }
    function executeEmail() {
        console.log("current email repeat is ", emailRepeat);
        fetch(url, option)
        .then(response => response.text())
        .then(data => {
            console.log("return value ", data.split(", "));
            output =data.split(", ") 
            alert(`A match for you! \n email: ${output[0]}, first name: ${output[1]}, last name: ${output[2]}`);
        });
    }
    while(emailRepeat == null)
    {setTimeout(() => {  console.log("sleep for email check to get back"); }, 2000);

    }
    if(emailRepeat == 0)
    {executeEmail();
    
    }
    
    else
    alert("the email already exists!");
    console.log(userAnswer);
    
    // do something here to query userdata
}


request();


}

    
    else
    alert("fill out all the questions!");

}
// record the answers
function record(ar, names) {
 
    var q1; 
    var answer = [];

    answer.push(names[0]);
    answer.push(names[1]);
    answer.push(names[2]);
    ar.forEach(element => {
        if (element.type == "radio" && element.checked)
        {answer.push(element.value);
        //console.log(element);
        }
    });
    return arrayToJson(answer);
    console.log(answer);
}

function arrayToJson(ar) {
    return JSON.stringify({firstName: ar[0],
            lastName: ar[1],
            email: ar[2],
            answers: ar.splice(3, ar.length)});
}
