from project import app
from project import controller
from flask import render_template, request, Blueprint


main = Blueprint('main', __name__)

@main.route('/')  # Home page
def homePage():
    print('test2')
    return render_template("index.html")

@main.route('/questions', methods=['POST'])  
def answersPage():
    f_questions = []
    f_contexts = []
    f_links = []
    f_text_indexes = []
    f_answers = {}

    dict = request.json
    print("Request Dictionary:", dict)
    context = dict['context']
    questions = dict['questions']
    model = dict['model']
    language = dict['lang']
    haveContext = dict['haveContext']
    
    # Step 1
    # Check if the questions are in english or in greek.
    # If they are in greek translate them.
    if language != 'en':
        print('Translating questions: ', questions)
        f_questions = controller.translate_questions(questions)
    else:
        f_questions = questions
    print('Final Questions: ', f_questions)

    # Step 2
    # Check if we have a context.
    # If we don't run ERM
    # If we do translate context if needed
    if not haveContext:
        print("Searching for context")
        f_contexts, f_links, f_text_indexes = controller.questions_to_contexts(f_questions)
    else:
        print("We have context")
        f_links = None
        f_text_indexes = None
        if language != 'en':
            print("Translating context")
            f_contexts.append(controller.translate_context(context))
        else:
            f_contexts.append(context)

    # Answer question with model and create the dict that will be returned to frontend.
    for i in range(len(questions)):
        answer = ''
        conf_score = ''
        source_link = ''
        source_lang = language
        model_resp_time = ''
        start = ''
        end = ''
        if not haveContext:
            if f_contexts[i] == None:
                answer = None
                conf_score = None
                source_link = None
                source_lang = None
                model_resp_time = None
                start = None
                end = None
            else:
                answer, conf_score, model_resp_time, start, end = controller.answer_question(f_contexts[i], f_questions[i], model, language)
                source_lang = 'en' if f_text_indexes[i] <= start else 'el'
                source_link = f_links[i][0 if source_lang == 'el' else 1]
        else:
            if f_contexts[0] == None or f_questions[i] == None:
                answer = None
                conf_score = None
                source_link = None
                source_lang = None
                model_resp_time = None
                start = None
                end = None
            else:
                answer, conf_score, model_resp_time, start, end = controller.answer_question(f_contexts[0], f_questions[i], model, language)
        # Add answer to answers dict
        f_answers['answer' + str(i)] = {
            'text' : answer, 
            'conf_score' : conf_score, 
            'source_link': source_link, 
            'source_lang': source_lang, 
            'model_resp_time': model_resp_time,
            'start': start,
            'end': end
            }
    print("server responds...")
    print(f_answers)
    return f_answers, 200
