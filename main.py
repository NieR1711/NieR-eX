import os
import sys
import re
import math
import random
import statistics
from urllib.request import urlopen
from datetime import date
import zlib
import numpy as np
import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone()

with mic as source:
  audio = r.listen(source)
print(r.recognize_google(audio.language='ko-KR'))

