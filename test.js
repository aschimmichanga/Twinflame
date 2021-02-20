// if answers are not fully filled, alert, or else record
function check() {
    var reqLength = 6;
    allArrayElements = Array.from(document.querySelector("#quiz_id").elements);
    first = document.getElementById("fname").value;
    last = document.getElementById("lname").value; 
    email = document.getElementById("email").value;
    var len = allArrayElements.filter(element => element.checked).length;

    if (len == reqLength && first != null && last != null && email != null)
    {
    var userAnswer = record(allArrayElements, [first, last, email]);
    //insertAnswers();
    const url = new URL("http://localhost:5500/candidateData");
    const option = {
        method: 'POST',
        headers: {
            'Content-Type' : 'application/json'
        },
        body: userAnswer
    }
    fetch(url, option);
    console.log(userAnswer);

    // do something here to query userdata
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