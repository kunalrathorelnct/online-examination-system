
function changeQuestion(questionid){
    iframe.contentWindow.document.getElementById('question_text').innerHTML = questions[questionid-1]['question_text'];
    iframe.contentWindow.document.getElementById('ques').innerHTML = "Question No. " + questionid;
    document.getElementById('quesType').innerHTML = questions[questionid-1]['type'];
    document.getElementById('quesMarks').innerHTML = questions[questionid-1]['marks'];
    if (questions[questionid-1]['img']){
        iframe.contentWindow.document.getElementById('quesImg').src = '/media/'+questions[questionid-1]['img'];
    }
    
}