import numpy as np
import pandas as pd
from scipy.io.wavfile import write

input_filename=input("Input csvfile:")
soundlength_str=input("Sound length(sec):")
freq_str=input("Frequency:")
soundlength=int(soundlength_str)
freq=int(freq_str)

csvdata=pd.read_csv(input_filename, header=None,names=['ch1', 'ch2'])

ch_both=csvdata[['ch1','ch2']].values
ch_both_new=ch_both
for i in range(freq*soundlength-1):
    ch_both_new=np.concatenate([ch_both_new,ch_both])
    
write("output.wav", len(ch_both)*freq, ch_both_new.astype(np.float32))
print(f'Completed. Sampling rate:{len(ch_both)*freq}')
