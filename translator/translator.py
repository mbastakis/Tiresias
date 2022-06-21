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
        elif source == ''
    
    def init_bing(self):
        pass

    
