#diaxeirisi post/get request apo ta diafora url paths.
import csv, json, requests
from project.utils.translator import translate
from transformers import pipeline


def answer_question(context, question, model):
    context = translate(context, 'google', 'el', 'en')
    question = translate(question, 'google', 'el', 'en')
    question_answerer = pipeline(task="question-answering", model = model)
    return translate(question_answerer(question = question, context = context)['answer'], 'google', 'en', 'el')

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