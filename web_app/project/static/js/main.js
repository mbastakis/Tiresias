var questionCounter = 0;

$('#add-button').on('click', () => {
    $questions = $('.questions-section');
    questionCounter++;

    $questions.append('<div class="question" id="' + questionCounter + '">' +
        '<h3 class="question-counter">Question #' + (questionCounter + 1) + '</h3>' +
        '<div class="question-field">' +
        '<input class="input" type="text" value="">' +
        '<button class="remove-question" id="remove-' + questionCounter + '" name="' + questionCounter + '"> - </button>' +
        '</div>' +
        '<output></output>');

    $('#remove-' + questionCounter).on('click', (question) => {
        var removeId = question.currentTarget["name"];
        $('#' + removeId).remove();
        question_list = $('.question-counter');
        for (let i = 0; i < question_list.length; i++) {
            question_list.get(i).innerText = 'Question #' + (i + 2);
        }
    });

    question_list = $('.question-counter');
    for (let i = 0; i < question_list.length; i++) {
        question_list.get(i).innerText = 'Question #' + (i + 2);
    }
});

$('#answer-button').on('click', () => {
    outputList = $('output');
    inputList = $('.input');
    context = $('#context').val();
    $('load-bar').addClass("loader");

    model = $('#models').val();

    let request = {}
    request.context = context;
    request.questions = [];
    request.model = model;
    for (let i = 0; i < inputList.length; i++) {
        request.questions.push(inputList.get(i).value);
    }

    $.ajax({
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify(request),
        dataType: 'json',
        url: 'http://127.0.0.1:8080/questions',
        success: (answers) => {
            $('load-bar').removeClass("loader");
            i = 0;
            for (let index in answers) {
                outputList.get(i).innerText = answers[index];
                i++;
            }
        },
        error: (e) => {
            $('load-bar').removeClass("loader");
            console.log(e);
        }
    });
});