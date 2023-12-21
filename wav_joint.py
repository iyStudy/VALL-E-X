# -*- coding: utf-8 -*-
from pydub import AudioSegment

# 音声ファイルの読み込み
sound1 = AudioSegment.from_file("./jointSound/input/wakamoto_syaruru_01.wav", "wav")
sound2 = AudioSegment.from_file("./jointSound/input/wakamoto_syaruru_02.wav", "wav")
sound3 = AudioSegment.from_file("./jointSound/input/wakamoto_syaruru_03.wav","wav")

# 連結
sound = sound1 + sound2 + sound3

# 保存
sound.export("./jointSound/output/output.mp4", format="mp4")
