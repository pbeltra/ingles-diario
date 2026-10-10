import asyncio, json, os, subprocess, sys
import edge_tts
OUT="/workspace/ingles-app/audio"; TMP="/tmp/ingles_raw"; os.makedirs(TMP,exist_ok=True)
W=json.load(open("/workspace/ingles-app/words.json"))["words"]
jobs=[]
for w in W:
    jobs.append(("w_"+w["audio"], w["en"])); jobs.append(("e_"+w["audio"], w["ex"]))
sem=asyncio.Semaphore(int(os.environ.get("PAR","10"))); fails=[]
FORCE=os.environ.get("FORCE")=="1"
async def one(name,text):
    dst=f"{OUT}/{name}.mp3"
    if not FORCE and os.path.exists(dst) and os.path.getsize(dst)>1000 and os.path.exists(f"{TMP}/{name}.ok"): return
    async with sem:
        for a in range(4):
            try:
                raw=f"{TMP}/{name}.mp3"
                await edge_tts.Communicate(text,"en-US-AndrewNeural",rate="-15%").save(raw)
                p=await asyncio.create_subprocess_exec("ffmpeg","-y","-loglevel","error","-i",raw,
                    "-af","silenceremove=start_periods=1:start_threshold=-50dB,areverse,silenceremove=start_periods=1:start_threshold=-50dB,areverse,apad=pad_dur=0.15",
                    "-ac","1","-ar","22050","-b:a","32k",dst)
                await p.wait()
                if p.returncode==0 and os.path.getsize(dst)>500:
                    open(f"{TMP}/{name}.ok","w").close(); return
            except Exception as e:
                await asyncio.sleep(2*(a+1))
        fails.append(name)
async def main():
    await asyncio.gather(*(one(n,t) for n,t in jobs))
    print("done", len(jobs), "fails", fails)
asyncio.run(main())
