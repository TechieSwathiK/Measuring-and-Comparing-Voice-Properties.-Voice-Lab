

"""
L2: Voice Analysis & Comparison
Record → Analyze Properties → Compare Two Recordings
Prepares students to CONTROL these properties in L3 (TTS)

============== DEPENDENCY SETUP ==============

CHECK IF INSTALLED (run in terminal):
    pip show SpeechRecognition pyaudio numpy matplotlib

INSTALL - WINDOWS:
    pip install SpeechRecognition pyaudio numpy matplotlib

INSTALL - macOS:
    brew install portaudio
    pip install SpeechRecognition pyaudio numpy matplotlib

NOTE: macOS requires portaudio BEFORE installing pyaudio
==============================================
"""

import threading
import sys

# Dependency check
try:
    import pyaudio
    import numpy as np
    import matplotlib.pyplot as plt
    import speech_recognition as sr
    from speech_recognition import AudioData
except ImportError as e:
    print(f"❌ Missing library: {e.name}")
    print("\n📦 Install commands:")
    print("   Windows: pip install SpeechRecognition pyaudio numpy matplotlib")
    print("   macOS:   brew install portaudio && pip install SpeechRecognition pyaudio numpy matplotlib")
    sys.exit(1)

stop_event = threading.Event()

def wait_for_enter():
    input()
    stop_event.set()

def record_audio(label):
    stop_event.clear()
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000,
                    input=True, frames_per_buffer=1024)
    frames = []
    
    print(f"\n🎤 {label}")
    print("   Press Enter to stop...")
    threading.Thread(target=wait_for_enter, daemon=True).start()
    
    print("🔴 Recording", end="", flush=True)
    while not stop_event.is_set():
        frames.append(stream.read(1024, exception_on_overflow=False))
        print(".", end="", flush=True)
    print(" ✅")
    
    stream.stop_stream()
    stream.close()
    width = p.get_sample_size(pyaudio.paInt16)
    p.terminate()
    return b''.join(frames), 16000, width

def analyze_audio(data, rate):









  

def transcribe(data, rate, width):
    recognizer = sr.Recognizer()
    try:
        return recognizer.recognize_google(AudioData(data, rate, width))
    except:
        return "[Could not transcribe]"

def display_stats(stats, text, label):
    print(f"\n{'─' * 35}")
    print(f"📊 {label}")
    print(f"{'─' * 35}")
    print(f"⏱️  Duration:   {stats['duration']:.2f} sec")
    print(f"📈 Avg Volume: {stats['avg_volume']:.0f}")
    print(f"🔊 Max Volume: {stats['max_volume']:.0f}")
    print(f"📝 Text: {text}")

def compare(s1, s2):










  

def plot_both(s1, s2, rate):














  

def main():










  

if __name__ == "__main__":
    main()
