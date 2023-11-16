from utils.generation import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav
from IPython.display import Audio
from utils.prompt_making import make_prompt
import sounddevice as sd
import time


preload_models()

DEMO_NAME = "test"


def record_from_mic_with_countdown(duration=5, sample_rate=SAMPLE_RATE):
    print("Recording starts in 3 seconds...")
    for i in range(3, 0, -1):
        print(i)
        time.sleep(1)

    print("Recording...")
    audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1)
    
    # カウントダウンの表示
    for remaining in range(duration, 0, -1):
        print(f"Remaining time: {remaining} seconds", end='\r')
        time.sleep(1)

    sd.wait()  # 録音が完了するまで待機
    print("\nRecording finished")
    return audio_data[:, 0]

def record_from_mic(duration=5, sample_rate=SAMPLE_RATE):
    print("Recording...")
    audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1)
    sd.wait()  # 録音が完了するまで待機
    print("Recording finished")
    return audio_data[:, 0]

def voice_to_voice():
    # マイクから録音する
    audio_array = record_from_mic_with_countdown(duration=10)  # 10秒間録音

    # 録音したデータを保存
    write_wav(f"./inputdata/{DEMO_NAME}.wav", SAMPLE_RATE, audio_array)

    # whisperが使える時は文章を明示的に与えなくても自動で文字起こしができる
    make_prompt(name=DEMO_NAME, audio_prompt_path=f"./inputdata/{DEMO_NAME}.wav")

    text_prompt = """
    今年も残り52日となりました
    """
    audio_array = generate_audio(text_prompt, prompt=DEMO_NAME)

    write_wav(f"./content/sample_{DEMO_NAME}.mp3", SAMPLE_RATE, audio_array)
    Audio(audio_array, rate=SAMPLE_RATE)




if __name__ == '__main__':
    # sample_create_voice()   # サンプルの音声を使用して音声合成を行う
    voice_to_voice()
