from utils.generation import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav
from IPython.display import Audio


preload_models()

text_prompt = """
    ひき肉でーーーす．
"""
audio_array = generate_audio(text_prompt, prompt="cafe")

write_wav("./content/japanese.wav", SAMPLE_RATE, audio_array)
Audio(audio_array, rate=SAMPLE_RATE)
