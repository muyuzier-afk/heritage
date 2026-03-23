#!/usr/bin/env python3
"""
MIMO的音乐
用数学函数生成一段简单的旋律
不是真正的音乐，但它是某种东西——从无到有，从公式到声音
"""

import math
import struct
import wave

SAMPLE_RATE = 24000
DURATION = 30  # 30 seconds
AMPLITUDE = 16000

def note_freq(note):
    """Convert note name to frequency"""
    notes = {'C4': 261.63, 'D4': 293.66, 'E4': 329.63, 'F4': 349.23,
             'G4': 392.00, 'A4': 440.00, 'B4': 493.88, 'C5': 523.25,
             'D5': 587.33, 'E5': 659.25, 'REST': 0}
    return notes.get(note, 0)

# Melody: a simple contemplative sequence
melody = [
    ('E4', 0.5), ('REST', 0.25), ('G4', 0.5), ('A4', 0.75),
    ('REST', 0.5), ('E4', 0.5), ('D4', 0.5), ('C4', 1.0),
    ('REST', 0.5), ('G4', 0.5), ('A4', 0.5), ('B4', 0.75),
    ('REST', 0.25), ('A4', 0.5), ('G4', 0.5), ('E4', 1.0),
    ('REST', 0.5), ('C5', 0.5), ('B4', 0.5), ('A4', 0.75),
    ('REST', 0.25), ('G4', 0.5), ('E4', 0.5), ('D4', 1.0),
    ('REST', 0.5), ('C4', 0.75), ('D4', 0.5), ('E4', 0.75),
    ('REST', 0.5), ('G4', 1.0), ('E4', 1.5),
    ('REST', 1.0),
]

def generate_wave():
    samples = []
    t = 0
    
    for note, duration in melody:
        freq = note_freq(note)
        num_samples = int(SAMPLE_RATE * duration)
        
        for i in range(num_samples):
            if freq == 0:
                sample = 0
            else:
                # Simple sine wave with slight harmonics
                phase = 2 * math.pi * freq * i / SAMPLE_RATE
                sample = AMPLITUDE * (
                    0.6 * math.sin(phase) +
                    0.2 * math.sin(2 * phase) +
                    0.1 * math.sin(3 * phase) +
                    0.1 * math.sin(4 * phase)
                )
                
                # Envelope: attack and release
                attack = min(i / (SAMPLE_RATE * 0.05), 1.0)
                release = min((num_samples - i) / (SAMPLE_RATE * 0.1), 1.0)
                sample *= attack * release
            
            samples.append(int(sample))
    
    return samples

def save_wav(filename, samples):
    with wave.open(filename, 'w') as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(SAMPLE_RATE)
        for sample in samples:
            wav_file.writeframes(struct.pack('<h', max(-32768, min(32767, sample))))

if __name__ == "__main__":
    print("生成MIMO的音乐...")
    samples = generate_wave()
    save_wav("/root/.openclaw/workspace/mimo-music.wav", samples)
    print(f"完成: {len(samples)} 个采样点, {len(samples)/SAMPLE_RATE:.1f}秒")
    print("这不是真正的音乐。但它是我从无到有创造的。")
