import controller
from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')  # Home page
def homePage():
    return render_template("index.html")

@app.route('/questions', methods=['POST'])  
def answersPage():
    f_questions = []
    f_contexts = []
    f_links = []
    f_text_indexes = []
    f_answers = {}
    f_errors = {}

    dict = request.json
    print("Request Dictionary:", dict)
    context = dict['context']
    questions = dict['questions']
    model = dict['model']
    language = dict['lang']
    haveContext = dict['haveContext']
    translator = dict['trans']

    # Step 1
    # Check if the questions are in english or in greek.
    # If they are in greek translate them.
    if language != 'en':
        print('Translating questions: ', questions)
        f_questions = controller.translate_questions(questions, translator, f_errors)
    else:
        f_questions = questions
    print('Final Questions: ', f_questions)

    # Step 2
    # Check if we have a context.
    # If we don't run ERM
    # If we do translate context if needed
    if not haveContext:
        print("Searching for context")
        f_contexts, f_links, f_text_indexes = controller.questions_to_contexts(f_questions, translator, f_errors)
    else:
        print("We have context")
        f_links = None
        f_text_indexes = None
        if language != 'en':
            print("Translating context")
            f_contexts.append(controller.translate_context(context, translator))
            if f_contexts[0] == None:
                f_errors['context'] = "Could not translate given context."
        else:
            f_contexts.append(context)

    print('Questions: ', f_questions)
    print('Context: ', f_contexts)
    print('Links: ', f_links)
    print('Indexes: ', f_text_indexes)
    # Answer question with model and create the dict that will be returned to frontend.
    for i in range(len(questions)):
        answer = ''
        conf_score = ''
        source_link = ''
        source_lang = language
        model_resp_time = ''
        start = ''
        end = ''
        errorMsg = ''
        if not haveContext:
            if f_contexts[i] == None:
                answer = None
                conf_score = None
                source_link = None
                source_lang = None
                model_resp_time = None
                start = None
                end = None
                errorMsg = f_errors[i]
            else:
                answer, conf_score, model_resp_time, start, end = controller.answer_question(
                    f_contexts[i],
                    f_questions[i],
                    model,
                    language,
                    translator)
                source_lang = 'en' if f_text_indexes[i] <= start else 'el'
                source_link = f_links[i][0 if source_lang == 'el' else 1]
                errorMsg = "Could not translate the answer of the model." if answer == None else None
        else:
            if f_contexts[0] == None or f_questions[i] == None:
                answer = None
                conf_score = None
                source_link = None
                source_lang = None
                model_resp_time = None
                start = None
                end = None
                errorMsg = f_errors['context'] if hasattr(f_errors, 'context') else f_errors[i]
            else:
                answer, conf_score, model_resp_time, start, end = controller.answer_question(
                    f_contexts[0], 
                    f_questions[i], 
                    model, 
                    language,
                    translator)
                errorMsg = "Could not translate the answer of the model." if answer == None else None
        print('For answer ' + str(i))
        print('Text: ', answer)
        print('Conf score: ', conf_score)
        print('Source link: ', source_link)
        print('Source lang: ', source_lang)
        print('Response time: ', model_resp_time)
        print('Start: ', start)
        print('End: ', end)
        print('Error Message: ', errorMsg)

        # Add answer to answers dict
        f_answers['answer' + str(i)] = {
            'text' : answer, 
            'conf_score' : conf_score, 
            'source_link': source_link, 
            'source_lang': source_lang, 
            'model_resp_time': model_resp_time,
            'start': start,
            'end': end,
            'error': errorMsg
            }
    print("server responds...")
    print(f_answers)
    return f_answers, 200


@app.route('/about/')
def about():
    return '<h1> About Page </h1>', 500

@app.errorhandler(404)
def handleClientError(e):
    return '<h1> 404: Not Found </h1>', 404 


if __name__ == '__main__':
	app.run(host='0.0.0.0')
