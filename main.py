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
from konlpy.tag import Okt

r = sr.Recognizer()
mic = sr.Microphone()

with mic as source:
  audio = r.listen(source)
print(r.recognize_google(audio.language='ko-KR'))

okt = Okt()

text = "이 프로젝트를 시작해볼까"

print(okt.morphs(text))
print(okt.morphs(text, stem=True))

