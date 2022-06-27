var sideBar = document.getElementById("mobile-nav");
var openSidebar = document.getElementById("openSideBar");
var closeSidebar = document.getElementById("closeSideBar");
sideBar.style.transform = "translateX(-260px)";

var questionCounter = 1
var haveContext = true

function sidebarHandler(flag) {
    if (flag) {
        sideBar.style.transform = "translateX(0px)";
        openSidebar.classList.add("hidden");
        closeSidebar.classList.remove("hidden");
    } else {
        sideBar.style.transform = "translateX(-260px)";
        closeSidebar.classList.add("hidden");
        openSidebar.classList.remove("hidden");
    }
}

function applyChanges() {
    className = $(this).attr('id');
    if (className.includes('small')) {
        $('#' + className.substring(0, className.length - 6)).val($('#' + className).val());
    } else {
        $('#' + className + '-small').val($('#' + className).val());
    }
}

$('#model').on('change', applyChanges);
$('#model-small').on('change', applyChanges);
$('#lang').on('change', applyChanges);
$('#lang-small').on('change', applyChanges);
$('#trans').on('change', applyChanges);
$('#trans-small').on('change', applyChanges);
$('#erm').on('change', applyChanges);
$('#erm-small').on('change', applyChanges);

$('.context-toggle').on('click', function () {
    let isOn = !$(this).is(":checked");

    if (isOn) {
        $('#erm').hide();
        $('#erm-small').hide();
        $('.context-container').hide();
        $(this).prop('checked', false);
        haveContext = false;
    } else {
        $('#erm').show();
        $('#erm-small').show();
        $('.context-container').show();
        $(this).prop('checked', true);
        haveContext = true;
    }

    className = $(this).attr('id');
    if (className.includes('small')) {
        $('#' + className.substring(0, className.length - 6)).prop('checked', !isOn);
    } else {
        $('#' + className + '-small').prop('checked', !isOn);
    }
});

$('#add-button').on('click', () => {
    $questions = $('.questions-section');
    questionCounter++;

    $questions.append(
        '<div id = "' + questionCounter + '" class="flex flex-row items-center ">' +
        '<div class="form-control w-full max-w-xl mb-5" >' +
        '<label class="label question-label">' +
        '<span class="label-text text-lg">Question ' + (questionCounter) + '</span>' +
        '</label>' +
        '<div class="w-full flex flex-col">' +
        '<input type="text" placeholder="Write a question..." class="input input-bordered w-full input-question" />' +
        '<result class="bg-primary p-3 -mt-1 -z-10 rounded-t-none rounded-b-lg text-gray-200"></result>' +
        '</div>' +
        '</div>' +
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" id="remove-' + questionCounter + '" class="mt-5 h-5 ml-4 hover:cursor-pointer"><path d="M135.2 17.69C140.6 6.848 151.7 0 163.8 0H284.2C296.3 0 307.4 6.848 312.8 17.69L320 32H416C433.7 32 448 46.33 448 64C448 81.67 433.7 96 416 96H32C14.33 96 0 81.67 0 64C0 46.33 14.33 32 32 32H128L135.2 17.69zM394.8 466.1C393.2 492.3 372.3 512 346.9 512H101.1C75.75 512 54.77 492.3 53.19 466.1L31.1 128H416L394.8 466.1z" /></svg>' +
        '</div >'
    );

    question_list = $('.question-label');
    for (let i = 0; i < question_list.length; i++) {
        $(question_list.get(i))[0].innerHTML = '<span class="label-text text-lg">Question ' + (i + 1) + '</span>';
    }

    $('#remove-' + questionCounter).on('click', (question) => {
        let removeId = $($(question.currentTarget)[0]).attr('id').replace('remove-', '')
        $('#' + removeId).remove();
        question_list = $('.question-label');
        for (let i = 0; i < question_list.length; i++) {
            $(question_list.get(i))[0].innerHTML = '<span class="label-text text-lg">Question ' + (i + 1) + '</span>';
        }
    });
});

function clearPopup() {
    $('#popups').empty();
}

function addErrorPopup(errorMsg) {
    let popup = '<div class="absolute z-10 alert alert-error shadow-xl w-1/2 flex mt-8 justify-center">' +
        '<div>' +
        '<svg xmlns="http://www.w3.org/2000/svg" class="stroke-current flex-shrink-0 h-6 w-6" fill="none"' +
        'viewBox="0 0 24 24">' +
        '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"' +
        'd="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z" />' +
        '</svg>' +
        '<span>Error! ' + errorMsg + '</span>' +
        '</div>' +
        '</div>';

    $('#popups').append(popup);
    setTimeout(() => {
        clearPopup();
    }, 6000);
}

function addSucessPopup(successMsg) {
    let popup = '<div class="absolute z-10 alert alert-success shadow-xl w-1/2 flex mt-8 justify-center">' +
        '<div>' +
        '<svg xmlns="http://www.w3.org/2000/svg" class="stroke-current flex-shrink-0 h-6 w-6" fill="none" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" ' + 'stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>' +
        '<span>Sucess! ' + successMsg + '</span>' +
        '</div>' +
        '</div>';

    $('#popups').append(popup);
    setTimeout(() => {
        clearPopup();
    }, 6000);
}

$('#answer-button').on('click', () => {
    let outputList = $('result');
    let questionList = $('.input-question');
    let context = $('#context').val();
    let model = $('#model').val();
    let lang = $('#lang').val();
    let trans = $('#trans').val();
    let erm = $('#erm').val();

    // Error checking, prerequisite for the ajax request.
    if (haveContext && context === "") {
        addErrorPopup('Please add a context or turn off the \'give context\' option.');
        return;
    }
    if (model === null) {
        addErrorPopup('Please select a Model to answer your questions.');
        return;
    }
    if (lang === null) {
        addErrorPopup('Please select the language of the questions and the context.');
        return;
    }
    if (trans === null) {
        addErrorPopup('Please select the Translator to perform the necessary translations for the process.');
        return;
    }
    if (haveContext && erm === null) {
        addErrorPopup('Please select an Entity Recognition Model.');
        return;
    }

    for (let i = 0; i < questionList.length; i++) {
        if (questionList.get(i).value === "") {
            addErrorPopup('Question ' + (i + 1) + ' is empty, please remove this question or input a question');
            return;
        }
    }
    // $('load-bar').addClass("loader");

    let request = {};
    if(haveContext === false) context = "";
    request.context = context;
    request.questions = [];
    request.model = model;
    request.lang = lang;
    request.trans = trans;
    request.erm = erm;
    request.haveContext = haveContext;

    for (let i = 0; i < questionList.length; i++) {
        request.questions.push(questionList.get(i).value);
    }

    $.ajax({
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify(request),
        dataType: 'json',
        url: 'http://127.0.0.1:5000/questions',
        success: (answers) => {
            $('load-bar').removeClass("loader");
            i = 0;
            console.log(answers)
            for (let key in answers) {
                console.log(key);
                outputList.get(i).innerText = answers[key].text + " (Score: " + parseFloat(answers[key].conf_score).toFixed(2) + ')';
                i++;
            }
        },
        error: (e) => {
            $('load-bar').removeClass("loader");
            console.log(e);
        }
    });
});