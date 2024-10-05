import sounddevice as sd
import wave
import time

# print(sd.query_devices())

# Function to capture audio in real-time
device_id=14
def record_audio(duration,delay, filename="output.wav", sample_rate=44100,device=None):

    time.sleep(delay)  # will start the recording from x1 time
    print(f"Recording for {duration} seconds...")

    # Capture audio stream
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=2, dtype='int16',device=device)

    sd.wait()  # Wait for the recording to finish
    print(f"Recording complete, saved as {filename}")

    # Save the recording as a WAV file
    with wave.open(filename, 'w') as wf:
        wf.setnchannels(2)  # Stereo
        wf.setsampwidth(2)  # Sample width in bytes
        wf.setframerate(sample_rate)
        wf.writeframes(recording.tobytes())


if __name__ == "__main__":
    x1 = 0  # Start time in seconds
    x2 = 10  # End time in seconds 
    filename = "output.wav"
    
    record_audio(x2-x1,x1, filename,device=device_id)