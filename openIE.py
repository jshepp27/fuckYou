import nltk
from pycorenlp import *
import collections
nlp=StanfordCoreNLP("http://localhost:9000/")
s="Twenty percent electric motors are pulled from an assembly line"
output = nlp.annotate(s, properties={
    "annotators": "tokenize, ssplit, pos, depparse, natlog,openie",
    "outputFormat": "json",
    "openie.triple.strict":"true"
})

# result = [output["sentences"][0]["openie"] for item in output]
print(output)
# for i in result:
#     for rel in i:
#         relationSent=rel['relation'], rel['subject'], rel['object']
#         print(relationSent)