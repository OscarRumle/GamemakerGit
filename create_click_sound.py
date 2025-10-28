import struct
import math

def create_click_sound(filename, duration=0.1, sample_rate=44100):
    """Create a simple click/beep sound"""

    # Calculate number of samples
    num_samples = int(duration * sample_rate)

    # Generate a short beep (sine wave with envelope)
    samples = []
    frequency = 1000  # Hz

    for i in range(num_samples):
        # Sine wave
        t = i / sample_rate
        amplitude = math.sin(2 * math.pi * frequency * t)

        # Apply envelope to avoid clicks (fade in/out)
        envelope = 1.0
        fade_samples = int(0.01 * sample_rate)  # 10ms fade
        if i < fade_samples:
            envelope = i / fade_samples
        elif i > num_samples - fade_samples:
            envelope = (num_samples - i) / fade_samples

        # Scale to 16-bit integer
        sample_value = int(amplitude * envelope * 32767 * 0.3)  # 30% volume
        samples.append(sample_value)

    # Write WAV file
    with open(filename, 'wb') as f:
        # WAV header
        f.write(b'RIFF')
        f.write(struct.pack('<I', 36 + num_samples * 2))  # File size - 8
        f.write(b'WAVE')

        # fmt chunk
        f.write(b'fmt ')
        f.write(struct.pack('<I', 16))  # Chunk size
        f.write(struct.pack('<H', 1))   # PCM format
        f.write(struct.pack('<H', 1))   # Mono
        f.write(struct.pack('<I', sample_rate))
        f.write(struct.pack('<I', sample_rate * 2))  # Byte rate
        f.write(struct.pack('<H', 2))   # Block align
        f.write(struct.pack('<H', 16))  # Bits per sample

        # data chunk
        f.write(b'data')
        f.write(struct.pack('<I', num_samples * 2))

        for sample in samples:
            f.write(struct.pack('<h', sample))

create_click_sound('Blank Pixel Game_1/sounds/snd_click/snd_click.wav')
print("Click sound created successfully!")
