import sys,json,numpy as np,librosa,subprocess
src,wj=sys.argv[1],sys.argv[2]
y,sr=librosa.load(src.replace('.mp4','.wav'),sr=22050,mono=True)
tempo,beats=librosa.beat.beat_track(y=y,sr=sr)
print('tempo',np.round(tempo,1),'beats',np.round(librosa.frames_to_time(beats,sr=sr),2)[:12])
# voice word times, to separate SFX from speech
words=[w for s in json.load(open(wj))['segments'] for w in s.get('words',[])]
S=np.abs(librosa.stft(y,n_fft=2048,hop_length=256))
f=librosa.fft_frequencies(sr=sr,n_fft=2048)
hi=S[f>6000].sum(0); lo=S[f<150].sum(0); full=S.sum(0)
cent=librosa.feature.spectral_centroid(S=S,sr=sr)[0]
t=librosa.frames_to_time(np.arange(S.shape[1]),sr=sr,hop_length=256)
on=librosa.onset.onset_detect(y=y,sr=sr,hop_length=256,backtrack=False,delta=0.25,units='frames')
# visual cuts
vid=subprocess.run(['ffmpeg','-v','error','-i',src,'-vf','scale=96:54,format=gray','-f','rawvideo','-'],capture_output=True).stdout
a=np.frombuffer(vid,np.uint8).reshape(-1,54,96).astype(float); d=np.abs(np.diff(a,axis=0)).mean((1,2))
cuts=[(i+1)/30 for i in range(len(d)) if d[i]>18]
print('visual cuts',np.round(cuts,2))
hn=hi/ (np.percentile(hi,95)+1e-9)
for o in on:
    seg=slice(max(o-20,0),min(o+60,len(t)))
    pre=hn[max(o-40,0):o].mean(); post=hn[o:o+8].mean()
    # length of the high-band event above half its peak
    pk=hn[o:o+40].max(); L=np.argmax(hn[o:o+80]<pk*0.3) if (hn[o:o+80]<pk*0.3).any() else 80
    slope=np.polyfit(np.arange(20),cent[max(o-20,0):max(o-20,0)+20],1)[0] if o>20 else 0
    inword=any(w['start']-0.02<=t[o]<=w['end'] for w in words)
    nearcut=min([abs(c-t[o]) for c in cuts],default=9)
    print(f"{t[o]:6.2f}s hi={post:4.2f} pre={pre:4.2f} len={L*256/sr*1000:4.0f}ms cent={cent[o]:5.0f} riseSlope={slope:6.1f} bass={lo[o]/(np.percentile(lo,95)+1e-9):4.2f} {'VOICE' if inword else '     '} {'CUT' if nearcut<0.07 else ''}")
