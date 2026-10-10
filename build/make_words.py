import json, re, glob
ranked=json.load(open("ranked.json"))[:1000]
rows=[]
for f in sorted(glob.glob("tr/*.txt")):
    for ln in open(f,encoding="utf-8"):
        ln=ln.rstrip("\n")
        if not ln.strip(): continue
        p=ln.split("|"); assert len(p)==5,(f,ln); rows.append(p)
assert len(rows)==1000,len(rows)
DISP={"mr":"Mr.","mrs":"Mrs.","dr":"Dr.","tv":"TV","christmas":"Christmas","english":"English","french":"French","god":"God"}
POS={"verbo":"verbo","sust":"sustantivo","adj":"adjetivo","adv":"adverbio","pron":"pronombre","prep":"preposición","conj":"conjunción",
     "art":"artículo","det":"determinante","interj":"expresión","num":"número"}
out=[]; seen=set()
for r,(en,pos,es,ex,exes) in zip(ranked,rows):
    assert r["en"].lower()==en.lower(),(r["rank"],r["en"],en)
    d=DISP.get(en,en); assert d not in seen; seen.add(d)
    out.append({"rank":r["rank"],"en":d,"pos":POS[pos],"es":es.strip(),"ex":ex.strip(),"exEs":exes.strip(),
                "audio":re.sub(r"[^a-z0-9]+","_",d.lower()).strip("_"),"forms":r["forms"],"subtlexCount":r["freq"]})
meta={"source":"SUBTLEX-US (Brysbaert & New, 2009), frecuencias de subtítulos de películas y series de EE. UU. (51 millones de palabras)",
      "sourceUrl":"https://www.ugent.be/pp/experimentele-psychologie/en/research/documents/subtlexus",
      "file":"https://www.lexique.org/databases/SUBTLEX-US/SUBTLEXus74286wordstextversion.tsv",
      "license":"CC-BY-SA","method":"Lemas: formas sumadas por lema (lemminflect), sin contracciones, nombres propios, muletillas ni groserías; orden por frecuencia total del lema.",
      "count":len(out)}
json.dump({"meta":meta,"words":out},open("../words.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print(len(out))
for k in (1,50,200,500,999): print(json.dumps(out[k-1],ensure_ascii=False))
