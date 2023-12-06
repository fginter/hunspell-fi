import sys
import re
from libvoikko import Voikko

V=Voikko("fi")

w_re=re.compile("^[a-zA-ZöäåÖÄÅ][a-zA-ZöäåÖÄÅ-]*$")

for line in sys.stdin:
    line=line.strip()
    count,form,lemma,upos,utags=line.split("\t")
    lemma=lemma.replace("#","")
    count=int(count)
    if not w_re.match(form) or form[-1]=="-":
        continue
    if not w_re.match(lemma) or lemma[-1]=="-":
        continue
    print(count,form,lemma,upos,utags,V.spell(form),V.spell(lemma),sep="\t")
    
