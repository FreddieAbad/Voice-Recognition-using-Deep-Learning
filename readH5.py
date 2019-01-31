import numpy as np
import h5py
filename = 'mfcc_cnn_model_voice_recognition.h5'
f = h5py.File(filename, 'r')
np.savetxt('datafile.txt', f['dataset'][...])
f.close()
