#diaxeirisi post/get request apo ta diafora url paths.
import csv, json, requests
from project.utils.translator import translate
from transformers import pipeline
import project.utils.erm as erm

def answer_question(context, question, model):
    print('in answer question: ', context, question)
    question_answerer = pipeline(task="question-answering", model = model)
    return translate(question_answerer(question = question, context = context)['answer'], 'helsinki', 'en', 'el')

def translate_questions(questions):
    translated_questions = []
    for q in questions:
        translated_questions.append(translate(q, 'helsinki', 'el', 'en'))
    return translated_questions

def translate_context(context):
    return translate(context, 'helsinki', 'el', 'en')

def questions_to_contexts(questions):
    tmp = []
    for q in questions:
        print('in questions_to_contexts current question: ', q)
        gr_context = erm.get_context(q, 'el')
        en_context = erm.get_context(q, 'en')
        if gr_context != '':
            gr_context = translate(gr_context, 'helsinki', 'el', 'en')
            gr_context = '' if gr_context == None else gr_context
        tmp.append(gr_context + '\n' + en_context)
        print('In questions_to_contexts for ', q, ':\n', tmp[-1])
        if en_context == '' and gr_context == '':
            return None
    return tmp

# with open(output_file, 'a', encoding='UTF16') as file:
#     writer = csv.writer(file)
#     writer.writerow(headers)

# for subject in data:
#     paragraphs = subject["paragraphs"]
#     print('\n-------------------------\n')
#     for QnA in paragraphs:        
#         en_context = translate(QnA['context'], 'google', 'el', 'en') #TODO: translate with helsinki (care for length limit)
#         print('Context:', en_context)
#         for qna in QnA["qas"]:
#             en_question = translate(qna["question"], 'google', 'el', 'en')
            
#             results = []
#             question = en_question
#             for i in range(len(models)):
#                 result = answer_question(en_context, en_question, models[i])
#                 results.append([question, models[i], result['score'], result['start'], result['end'], translate(result['answer'], 'helsinki', src='en', dest='el'), qna['answers'][0]['text']])
#                 question = ""

#             with open(output_file, 'a', encoding='UTF16') as file:
#                 writer = csv.writer(file)
#                 for i in range(len(results)):
#                     writer.writerow(results[i])