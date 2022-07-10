import time
import translators as ts
# from transformers import AutoTokenizer, AutoModelForSeq2SeqLM,pipeline
from project.utils.text_splitter import split_to_sentences, split_text

# tokenizer_gr_to_en = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-grk-en")
# model_gr_to_en = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-grk-en")

# tokenizer_en_to_gr = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-el")
# model_en_to_gr = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-el")

# Map greek and english words.
greek_to_english = {}

# def translate_sentence_with_helsinki(input, src='el', dest='en'):
#     if ( (src == 'el') and (dest == 'en') ):
#         translation=pipeline("translation",model=model_gr_to_en,tokenizer=tokenizer_gr_to_en)
#     elif ( (src == 'en') and (dest == 'el') ):
#         translation=pipeline("translation",model=model_en_to_gr,tokenizer=tokenizer_en_to_gr)
#     else:
#         raise Exception("Invalid language selection.")
#     return translation(input)[0]['translation_text']


# def helsinki_translate(text, input_lang, output_lang):
#     sentences = split_to_sentences(text)
#     translated_text = ''
#     for sentence in sentences:
#         if(sentence == '..'):
#             translated_text += '..'
#         else:
#             if sentence not in greek_to_english.keys():
#                 greek_to_english[sentence] = translate_sentence_with_helsinki(sentence, input_lang, output_lang)
#             translated_text += greek_to_english[sentence]
#     return translated_text.replace('City name (optional, probably does not need a translation)', '')


def request_bing_translation(input, src, dest):
    nap_time = 3
    exception_counter = 0
    exception_total_counter = 0
    while(True):
        try:
            if exception_total_counter > 100:
                print("Reached 100 exceptions sleeping for 2 minutes...")
                time.sleep(120)
                exception_total_counter = 0
            response = ts.bing(input, from_language=src, to_language=dest)
            return response
        except Exception as e:
            if(exception_counter > 3):
                nap_time += nap_time
            exception_counter += 1
            exception_total_counter += 1
            print("An exception occured: ", e)
            print("Sleeping for ", nap_time, ", exceptions happend: ", exception_counter)
            time.sleep(nap_time)


def bing_translate(input, src='auto', dest='en'):
    result = ''
    if len(input) > 999:
        texts = split_text(input, 999)
        for text in texts:
            translated_text = request_bing_translation(text, src, dest)
            result += translated_text
    else:
        if input not in greek_to_english.keys():
            translated_text = request_bing_translation(input, src, dest)
            result = translated_text
            greek_to_english[input] = translated_text
        else:
            result += greek_to_english[input]
        if len(greek_to_english) > 100:
            greek_to_english.clear()
    return result

# Dictionary of functions
translate_dict = {
    # "helsinki": helsinki_translate,
    "bing": bing_translate
}

def translate(input, translator, src='el', dest='en'):
    try:
        return translate_dict[translator](input, src, dest)
    except Exception as e:
        print("Exception while translating: ",input, ", with translator: ", translator, " : ",e)
        return None