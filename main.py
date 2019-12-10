import os
import sys
import re
import math
import random
import date
import time
import statistics
from urllib.request import urlopen
from datetime import date
import zlib
import numpy as np
import speech_recognition as sr
import shutil
import argparse
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import gzip
import pickle
import konlpy

r = sr.Recognizer()
mic = sr.Microphone()

with mic as source:
  audio = r.listen(source)
print(r.recognize_google(audio.language='ko-KR'))

x = np.arange(0,6,0.1)
y = np.sin(x)

plt.plot(x,y)
plt.show()


