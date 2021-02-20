// if answers are not fully filled, alert, or else record
function check() {
    var reqLength = 6;
    allArrayElements = Array.from(document.querySelector("#quiz_id").elements);
    first = document.getElementById("fname").value;
    last = document.getElementById("lname").value; 
    var len = allArrayElements.filter(element => element.checked).length;

    if (len == reqLength && first != null && last != null)
    {
    var userAnswer = record(allArrayElements, [first, last]);
    insertAnswers();
    console.log(userAnswer);
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
            answers: ar.splice(2, ar.length)});
}