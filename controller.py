#diaxeirisi post/get request apo ta diafora url paths.
import csv, json, requests
from utils.translator import translate
from transformers import pipeline
import utils.erm as erm
import time


def answer_question(context, question, model, lang, translator):
    print('Model Input:')
    print('Context: ', context)
    print('Question: ', question)
    
    start = time.time()
    question_answerer = pipeline(task="question-answering", model = model)
    qa = question_answerer(question = question, context = context)
    end = time.time()
    print('Model Answered: ', qa)

    if lang == 'el':
        return translate(qa['answer'], translator, 'en', 'el'), qa['score'], (end - start), qa['start'], qa['end']
    else:
        return qa['answer'], qa['score'], (end - start), qa['start'], qa['end']

def translate_questions(questions, translator, f_errors):
    translated_questions = []
    for q in questions:
        translated_questions.append(translate(q, translator, 'el', 'en'))
        if translated_questions[-1] == None:
            f_errors[questions.index(q)] = "Could not translate question."
    return translated_questions

def translate_context(context, translator):
    return translate(context, translator, 'el', 'en')

def questions_to_contexts(questions, translator, f_errors):
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

        # Translate the greek context
        if gr_context != '':
            gr_context = translate(gr_context, translator, 'el', 'en')
            gr_context = '' if gr_context == None else gr_context
        # If we didn't find any context
        if en_context == '' and gr_context == '':
            f_errors[questions.index(q)] = "Could not detect an entity in the question."
            contexts.append(None);
            text_indexes.append(None)
            links.append(None)
        else:
            contexts.append(gr_context + '\n' + en_context)
            text_indexes.append(len(gr_context) - 1)
            links.append([gr_link, en_link])
        print('Got context:', contexts[-1], '\n\nLinks:', links[-1][0], '\n      ', links[-1][1], '\nText Indice: ', str(text_indexes[-1])) if text_indexes[-1] != None else None
    return contexts, links, text_indexes