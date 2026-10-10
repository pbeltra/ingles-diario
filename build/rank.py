# Construye la lista de lemas más frecuentes desde SUBTLEX-US (Brysbaert & New 2009)
import csv, json, re, sys
from collections import defaultdict
from lemminflect import getAllLemmas
SRC="/workspace/ingles-app/data-src/SUBTLEXus74286wordstextversion.tsv"
DROP=set("""t s m re ll ve d don didn doesn isn wasn aren weren couldn wouldn shouldn haven hasn hadn ain won
gonna wanna gotta ya uh um huh ah hmm mm mmm whoa ha eh ooh aw la oh-oh yo na da em o ooh hm uh-huh uh-oh y c b e g n p r u x
ok mhm ahh hah heh shh ma'am th yea""".split())
KEEP_FORM=set("""left better best bit lying people glasses clothes news means used saw rest ones mind might would could should
lot data guys""".split()) - set(["saw","used","guys","ones"])
FORCE={"ok":"okay","guys":"guy","ones":"one","saw":"see","used":"use","men":"man","women":"woman","children":"child","an":"a","me":"me",
"him":"him","us":"us","them":"them","her":"her","my":"my","his":"his","their":"their","our":"our","your":"your","its":"its",
"is":"be","am":"be","are":"be","was":"be","were":"be","been":"be","being":"be","has":"have","had":"have","having":"have",
"does":"do","did":"do","done":"do","doing":"do","got":"get","gotten":"get"}
CAPS_OK=set("i mr mrs dr tv christmas english god ok oh hey hi french".split())
NAMES=set("mike nick ed ray jack max frank al bob jerry john il yo bill mark brown pop".split())
PROFANITY=set("""shit fuck fucking fucked fuckin bitch goddamn bastard bullshit asshole motherfucker dick piss ass crap damn hell
screw suck sucks bitches whore pussy cock sexy jesus christ freaking freakin""".split())
MERGE={"things":"thing","cops":"cop","feelings":"feeling","movies":"movie","found":"find","fell":"fall","pant":"pants","pants":"pants",
"fellas":"fella","cannot":"can","bigger":"big","biggest":"big","greatest":"great","closer":"close","faster":"fast","easier":"easy",
"earlier":"early","older":"old","sooner":"soon","longer":"long","means":"mean","lying":"lie","tire":"tired","tired":"tired",
"amaze":"amazing","amazing":"amazing","excite":"excited","excited":"excited","bore":"bored","bored":"bored","interest":"interest",
"alright":"all right","okay":"okay","ok":"okay","mommy":"mom","mama":"mom","daddy":"dad","folks":"folks","glasses":"glasses",
"thanks":"thanks","wed":"wedding","wedding":"wedding","clothes":"clothes","news":"news","people":"people","police":"police"}
for x in "ls ln ma de ho outta kinda mm lt il ofthe ifyou cause st".split(): DROP.add(x)
lem=defaultdict(float); forms=defaultdict(list)
for row in csv.DictReader(open(SRC,encoding="utf-8",errors="replace"),delimiter="\t"):
    w=row["Word"].strip(); fc=float(row["FREQcount"]); fl=float(row["FREQlow"])
    if fc<200: continue
    lw=w.lower()
    if fl/fc<0.1 and lw not in CAPS_OK: continue   # nombres propios (casi siempre en mayúscula)
    if lw in NAMES or lw in PROFANITY: continue
    if lw in DROP or "'" in lw or not re.fullmatch(r"[a-z]+",lw): continue
    if len(lw)==1 and lw not in ("a","i"): continue
    if lw in MERGE: L=MERGE[lw]
    elif lw in FORCE: L=FORCE[lw]
    elif lw in KEEP_FORM: L=lw
    else:
        al=getAllLemmas(lw); L=lw
        for pos in ("AUX","VERB","NOUN"):
            if pos in al and lw not in al[pos]:
                L=al[pos][0]; break
            if pos in al and lw in al[pos]: break
    L=MERGE.get(L,L)
    lem[L]+=fc; forms[L].append(lw)
ranked=sorted(lem.items(),key=lambda x:-x[1])
out=[{"rank":i+1,"en":("I" if w=="i" else w),"freq":int(f),"forms":forms[w][:6]} for i,(w,f) in enumerate(ranked[:1300])]
json.dump(out,open("/workspace/ingles-app/build/ranked.json","w"),ensure_ascii=False,indent=0)
for o in out[:1300]: print(o["rank"],o["en"],"/".join(o["forms"][:4]))
