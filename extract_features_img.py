'''
Created on 2017.12.9

@author: Richard
'''

import os
import librosa.display
import librosa.feature
import numpy as np
import matplotlib.pyplot as plt

number = 'MauricioPesantez'

def extract_mfcc(in_path, file, fmax, nMel):
    y, sr = librosa.load(in_path + file)
    if(y.size !=0):
        S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=nMel, fmax=fmax)
        
        plt.figure(figsize=(3, 3), dpi=100)
        librosa.display.specshow(librosa.amplitude_to_db(S, ref=np.max), fmax=fmax)

        plt.xticks([])
        plt.yticks([])
        plt.tight_layout()
        plt.savefig('./spoken_numbers_wav/mfcc_image_ts/' + number + '/' + file[:-3] + 'png', bbox_inches='tight', pad_inches=-0.1)
        print('./spoken_numbers_wav/mfcc_image_ts/' + number + '/' + file[:-3] + 'png')
        plt.close()   
        return


count = 0       # number of files processed
i=0
#in_path = 'myRecording/audio_ts/' + number + '/'       # input directory
in_path = 'recordings/'

#y, sr = librosa.load(in_path + 'Pesantez308.m4a')
#print(y)
#print(sr)
for wavfile in os.listdir(in_path):
    S = extract_mfcc(in_path, wavfile, 8000, 256)
    count += 1
    i+=1
    if count % 20 == 0:
        print ('%d files processed.' % count)
        #print (in_path, wavfile)

print ('Done!\t%d files processed.' % count)
