import translators as ts
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM,pipeline

class Translators:

    translate_dict = {
        "helsinki": {"init": init_helsinki, "translate":translate_helsinki},
        "bing": {"init": init_bing, "translate":translate_bing}
    }

    def __init__(self, translator, source):
        self.translator = translator
        self.src = source

        translate_dict[translator].init(source)
    
    def init_helsinki(self, source):
        if source == 'el':
            self.tokenizer_to_en = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-grk-en")
            self.model_to_en = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-grk-en")

            self.tokenizer_to_src = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-el")
            self.model_to_src = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-el")
        elif source == 'zh':
            self.tokenizer_to_en = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-zh-en")
            self.model_to_en = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-zh-en")

            self.tokenizer_to_src = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-zh")
            self.model_to_src = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-zh")
        elif source == 'de':
            self.tokenizer_to_en = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-de")
            self.model_to_en = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-de")

            self.tokenizer_to_src = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-de-en")
            self.model_to_src = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-de-en")
        elif source == 'fr':
            self.tokenizer_to_en = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-fr")
            self.model_to_en = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-fr")

            self.tokenizer_to_src = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-fr-en")
            self.model_to_src = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-fr-en")
        elif source == 'es':
            self.tokenizer_to_en = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-es")
            self.model_to_en = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-es")

            self.tokenizer_to_src = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-es-en")
            self.model_to_src = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-es-en")
        elif source == 'fi':
            self.tokenizer_to_en = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-fi")
            self.model_to_en = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-fi")

            self.tokenizer_to_src = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-fi-en")
            self.model_to_src = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-fi-en")
        elif source == 'ru':
            self.tokenizer_to_en = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-ru")
            self.model_to_en = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-ru")

            self.tokenizer_to_src = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-ru-en")
            self.model_to_src = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-ru-en")
        elif source == 'it':
            self.tokenizer_to_en = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-it")
            self.model_to_en = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-it")

            self.tokenizer_to_src = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-it-en")
            self.model_to_src = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-it-en")
        elif source == 'nl':
            self.tokenizer_to_en = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-nl")
            self.model_to_en = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-nl")

            self.tokenizer_to_src = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-nl-en")
            self.model_to_src = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-nl-en")
        elif source == 'et':
            self.tokenizer_to_en = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-et")
            self.model_to_en = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-et")

            self.tokenizer_to_src = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-et-en")
            self.model_to_src = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-et-en")
        elif source == 'sv':
            self.tokenizer_to_en = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-sv")
            self.model_to_en = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-sv")

            self.tokenizer_to_src = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-sv-en")
            self.model_to_src = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-sv-en")
        elif source == 'tr':
            self.tokenizer_to_en = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-tr")
            self.model_to_en = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-tr")

            self.tokenizer_to_src = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-tr-en")
            self.model_to_src = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-tr-en")
        elif source == 'pt':
            self.tokenizer_to_en = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-pt")
            self.model_to_en = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-pt")

            self.tokenizer_to_src = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-pt-en")
            self.model_to_src = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-pt-en")
        elif source == 'hi':
            self.tokenizer_to_en = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-hi")
            self.model_to_en = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-hi")

            self.tokenizer_to_src = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-hi-en")
            self.model_to_src = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-hi-en")
        elif source == 'cs':
            self.tokenizer_to_en = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-cs")
            self.model_to_en = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-cs")

            self.tokenizer_to_src = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-cs-en")
            self.model_to_src = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-cs-en")
        elif source == 'hu':
            self.tokenizer_to_en = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-hu")
            self.model_to_en = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-hu")

            self.tokenizer_to_src = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-hu-en")
            self.model_to_src = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-hu-en")
        elif source == 'lv':
            self.tokenizer_to_en = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-lv")
            self.model_to_en = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-lv")

            self.tokenizer_to_src = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-lv-en")
            self.model_to_src = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-lv-en")
        elif source == 'lt':
            self.tokenizer_to_en = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-lt")
            self.model_to_en = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-lt")

            self.tokenizer_to_src = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-lt-en")
            self.model_to_src = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-lt-en")
        elif source == 'mt':
            self.tokenizer_to_en = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-mt")
            self.model_to_en = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-mt")

            self.tokenizer_to_src = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-mt-en")
            self.model_to_src = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-mt-en")
        elif source == 'pl':
            self.tokenizer_to_en = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-pl")
            self.model_to_en = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-pl")

            self.tokenizer_to_src = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-pl-en")
            self.model_to_src = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-pl-en")
        elif source == 'sk':
            self.tokenizer_to_en = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-sk")
            self.model_to_en = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-sk")

            self.tokenizer_to_src = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-sk-en")
            self.model_to_src = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-sk-en")
        elif source == 'bg':
            self.tokenizer_to_en = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-bg")
            self.model_to_en = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-bg")

            self.tokenizer_to_src = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-bg-en")
            self.model_to_src = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-bg-en")
        elif source == 'sl':
            self.tokenizer_to_en = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-sl")
            self.model_to_en = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-sl")

            self.tokenizer_to_src = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-sl-en")
            self.model_to_src = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-sl-en")
        elif source == 'ga':
            self.tokenizer_to_en = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-ga")
            self.model_to_en = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-ga")

            self.tokenizer_to_src = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-ga-en")
            self.model_to_src = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-ga-en")
        elif source == 'ro':
            self.tokenizer_to_en = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-ro")
            self.model_to_en = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-ro")

            self.tokenizer_to_src = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-ro-en")
            self.model_to_src = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-ro-en")
        elif source == 'hr':
            self.tokenizer_to_en = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-hr")
            self.model_to_en = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-hr")

            self.tokenizer_to_src = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-hr-en")
            self.model_to_src = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-hr-en")
        else:
            # TODO: multilingual

            
    
    def init_bing(self):
        pass