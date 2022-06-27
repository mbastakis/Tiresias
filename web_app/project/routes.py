from project import app
from project import controller
from flask import render_template, request

@app.route('/')  # Home page
def homePage():
    return render_template("index.html")

@app.route('/questions', methods=['POST'])  
def answersPage():
    questions = []
    contexts = []
    dict = request.json
    print(dict)
    answers = {}
    language = dict['lang']
    if language == 'el':
        questions = controller.translate_questions(dict['questions'])
    else:
        questions = dict['questions']

    if dict['context'] == '':
        contexts = controller.questions_to_contexts(questions)
    else:
        if language == 'el':
            contexts.append(controller.translate_context(dict['context']))
        else:
            contexts.append(dict['context'])

    for i in range(len(questions)):
        print('test')
        if dict['context'] == '':
            if contexts[i] == None:
                answer = None
                conf_score = None
            else:
                answer, conf_score = controller.answer_question(contexts[i], questions[i], dict["model"], language)
        else:
            answer, conf_score = controller.answer_question(contexts[0], questions[i], dict["model"], language)
        answers['answer' + str(i)] = {'text' : answer, 'conf_score' : conf_score}
    print("server responds...")
    print(answers)
    return answers, 200


@app.route('/about/')
def about():
    return '<h1> About Page </h1>', 500

# @app.errorhandler(500)
# def handleServerError(e):
#     return '<h1> 500:Internal server error </h1>', 500

@app.errorhandler(404)
def handleClientError(e):
    return '<h1> 404: Not Found </h1>', 404 

# @app.route('/allTests')
# def allTests():
#     try:
#         grpcClient.sendAllTests()
#     except Exception as error:
#         print(f'Exception: {str(error)}')
#         abort(500)
#     return '<h1> All tests sent successfully </h1> '
#     #return redirect('http://127.0.0.1:8080/home')

# #Eg: http://127.0.0.1:8080/5555/1/Pass
# @app.route('/test/<int:testId>/<expectedResult>')  # PoC
# def forwardTestPlanToTestRunner(testId, expectedResult):
#     try:
#         grpcClient.sendTest(testId, expectedResult)
#     except Exception as error:
#         print(f'Exception: {str(error)}')
#         abort(500)
#     return '<h1> Test sent successfully </h1> '
#     #return redirect('http://127.0.0.1:8080/home')


# @app.route('/tests')
# def index():
#     if(not db.execute('SELECT * FROM tests;')):
#         print('Can not execute query')
#         abort(500)
#     tests = db.fetchAll()
#     print('Priting test results')
#     print(tests)
#     return render_template('tests.html', tests=tests)