import sparknlp
from pyspark.ml import PipelineModel
from sparknlp.annotator import *
from sparknlp.base import *

spark = sparknlp.start(spark32 = True)
documenter = DocumentAssembler().setInputCol("text").setOutputCol("document")
sentencerDL = SentenceDetectorDLModel.pretrained("sentence_detector_dl", "xx").setInputCols(["document"]).setOutputCol("sentences")
sd_model = LightPipeline(PipelineModel(stages=[documenter, sentencerDL]))


def split_to_sentences(text):
    sentences=[]
    for anno in sd_model.fullAnnotate(text)[0]["sentences"]:
        sentences.append(anno.result)
    return sentences


def split_text(text, length_limit):
    sentences = split_to_sentences(text)
    texts = []
    char_counter = 0
    cur_text = ''
    for sentence in sentences:
        if char_counter + len(sentence) > length_limit:
            texts.append(cur_text)
            cur_text = ''
            char_counter = 0
        cur_text += sentence
        char_counter += len(sentence)
    texts.append(cur_text)
    return texts