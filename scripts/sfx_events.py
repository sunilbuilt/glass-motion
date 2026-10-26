import sys,numpy as np,librosa
y,sr=librosa.load(sys.argv[1],sr=22050,mono=True)
hop=256
rms=librosa.feature.rms(y=y,hop_length=hop)[0]; db=librosa.amplitude_to_db(rms,ref=1.0)
S=np.abs(librosa.stft(y,n_fft=2048,hop_length=hop)); cent=librosa.feature.spectral_centroid(S=S,sr=sr)[0]
f=librosa.fft_frequencies(sr=sr,n_fft=2048); lowr=S[f<200].sum(0)/(S.sum(0)+1e-9)
on=librosa.onset.onset_detect(y=y,sr=sr,hop_length=hop,backtrack=True,delta=0.12,units='frames')
t=lambda i:i*hop/sr
for k,o in enumerate(on):
    nxt=on[k+1] if k+1<len(on) else len(db)
    seg=slice(o,nxt); pk=o+np.argmax(db[seg]); 
    # end: falls 30 dB below peak or next onset
    e=pk
    while e<nxt-1 and db[e]>db[pk]-30: e+=1
    c=cent[o:e+1]; slope=(c[-1]-c[0])/max(t(e-o),1e-3) if e>o else 0
    print(f"{t(o):6.2f}  attack {1000*t(pk-o):4.0f}ms  len {1000*t(e-o):5.0f}ms  peak {db[pk]:5.1f}dB  cent {np.median(c):5.0f}Hz  slope {slope:7.0f}  bass {np.median(lowr[o:e+1]):.2f}")
