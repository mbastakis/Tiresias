#diaxeirisi post/get request apo ta diafora url paths.
import csv, json, requests
from project.utils.translator import translate
from transformers import pipeline
import project.utils.erm as erm
import time


def answer_question(context, question, model, lang):
    print('in answer question: ', context, question)
    start = time.time()
    question_answerer = pipeline(task="question-answering", model = model)
    qa = question_answerer(question = question, context = context)
    end = time.time()
    if lang == 'el':
        return translate(qa['answer'], 'bing', 'en', 'el'), qa['score'], (end - start), qa['start'], qa['end']
    else:
        return qa['answer'], qa['score'], (end - start), qa['start'], qa['end']

def translate_questions(questions):
    translated_questions = []
    for q in questions:
        translated_questions.append(translate(q, 'bing', 'el', 'en'))
    return translated_questions

def translate_context(context):
    return translate(context, 'bing', 'el', 'en')

def questions_to_contexts(questions):
    contexts = []
    links = []
    text_indexes = []
    for q in questions:
        print('Searhing context from question:', q)
        # Check if the question was translated correctly.
        if q == None:
            contexts.append(None)
            links.append(None)
            text_indexes.append(None)
            continue
        # Get context from the question, in English and in Greek.
        gr_context, gr_link = erm.get_context(q, 'el');
        en_context, en_link = erm.get_context(q, 'en');

        gr_context = '' #TODO: remove this line
        # Translate the greek context
        if gr_context != '':
            gr_context = translate(gr_context, 'bing', 'el', 'en')
            gr_context = '' if gr_context == None else gr_context
        # If we didn't find any context
        if en_context == '' and gr_context == '':
            contexts.append(None);
            text_indexes.append(None)
            links.append(None)
        else:
            contexts.append(gr_context + '\n' + en_context)
            text_indexes.append(len(gr_context) - 1)
            links.append([gr_link, en_link])
        print('Got context:', contexts[-1], '\n\nLinks:', links[-1][0], '\n      ', links[-1][1], '\nText Indice: ', str(text_indexes[-1])) if text_indexes[-1] != None else None
    return contexts, links, text_indexes

# with open(output_file, 'a', encoding='UTF16') as file:
#     writer = csv.writer(file)
#     writer.writerow(headers)

# for subject in data:
#     paragraphs = subject["paragraphs"]
#     print('\n-------------------------\n')
#     for QnA in paragraphs:        
#         en_context = translate(QnA['context'], 'google', 'el', 'en') #TODO: translate with bing (care for length limit)
#         print('Context:', en_context)
#         for qna in QnA["qas"]:
#             en_question = translate(qna["question"], 'google', 'el', 'en')
            
#             results = []
#             question = en_question
#             for i in range(len(models)):
#                 result = answer_question(en_context, en_question, models[i])
#                 results.append([question, models[i], result['score'], result['start'], result['end'], translate(result['answer'], 'bing', src='en', dest='el'), qna['answers'][0]['text']])
#                 question = ""

#             with open(output_file, 'a', encoding='UTF16') as file:
#                 writer = csv.writer(file)
#                 for i in range(len(results)):
#                     writer.writerow(results[i])