# Voice Recognition
### English Version
## File Architecture and Description
`. / spoken_numbers_wav / *` Dataset spectrograms (train & test)

`. / tmp / tmp / *` Temporary Folder

`. / cnn_model.py` Trained CNN models

`. / extract_features_img.py` Script to produce Spectrograms

`. / generate_tr.py` Script to record voice
 
  `. / trimmer.py` Script to get 1 sec files
 
  `. / recorder.py` Script for real-time voice recognition
 
  `. / Recorder_GUI.py` GUI for` recorder.py`

  `. / splitTestTranDirectories.py` Script to separate Spectrograms between Train-Test
  
  `. / Recorder_GUI.py` GUI for` recorder.py`

### Version en Español
## File Architecture and Description
`./spoken_numbers_wav/*`   Espectrogramas del dataset (train & test)

`./tmp/tmp/*`   Carpeta Temporal

`./cnn_model.py`   Modelos CNN entrenados

`./extract_features_img.py`   Script para producir Espectrogramas

`./generate_tr.py`   Script para grabar voz
 
 `./trimmer.py`   Script para obtener Archivos de 1 seg
 
 `./recorder.py`   Script para reconocimiento de voz en tiempo real
 
 `./Recorder_GUI.py`   GUI para `recorder.py` 

 `./splitTestTranDirectories.py`   Script para separar Espectrogramas entre Train-Test
  
 `./Recorder_GUI.py`   GUI para `recorder.py`
