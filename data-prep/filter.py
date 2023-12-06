import sys
import re
from libvoikko import Voikko

V=Voikko("fi")

for line in sys.stdin:
    line=line.strip()
    count,form,lemma,upos,utags=line.split("\t")
    lemma=lemma.replace("#","")
    count=int(count)
    if not re.match("^[a-zA-ZöäåÖÄÅ][a-zA-ZöäåÖÄÅ-]*$",form) or form[-1]=="-":
        continue
    if not re.match("^[a-zA-ZöäåÖÄÅ][a-zA-ZöäåÖÄÅ-]*$",lemma) or lemma[-1]=="-":
        continue
    print(count,form,lemma,upos,utags,V.spell(form),V.spell(lemma),sep="\t")
    
