import sys

final=set()

for line in sys.stdin:
    line=line.strip()
    count,form,lemma,upos,utags,form_ok,lemma_ok=line.split("\t")
    if form_ok!="True" or lemma_ok!="True":
        continue
    if form[0].isupper() and not lemma[0].isupper():
        form=form.lower()
    final.add((lemma,form,upos+"_"+utags))
for l,f,t in sorted(final):
    print(l,f,t,sep="\t")

        
