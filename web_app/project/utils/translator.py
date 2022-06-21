from googletrans import Translator
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

google_translator = Translator()

# tokenizer_gr_to_en = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-grk-en")
# model_gr_to_en = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-grk-en")

# tokenizer_en_to_gr = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-el")
# model_en_to_gr = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-el")


def google_translate(input, src='auto', dest='en'):
    return google_translator.translate(input, src=src, dest=dest).text


# def helsinki_translate(input, src='el', dest='en'):
#     if ( (src == 'el') and (dest == 'en') ):
#         translation=pipeline("translation",model=model_gr_to_en,tokenizer=tokenizer_gr_to_en)
#     elif ( (src == 'en') and (dest == 'el') ):
#         translation=pipeline("translation",model=model_en_to_gr,tokenizer=tokenizer_en_to_gr)
#     else:
#         raise Exception("Invalid language selection.")
#     return translation(input)[0]['translation_text']

# Dictionary of functions
translate_dict = {
    "google": google_translate,
    # "helsinki": helsinki_translate
}

def translate(input, translator, src='el', dest='en'):
    return translate_dict[translator](input, src, dest)