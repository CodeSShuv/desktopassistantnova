import  numpy as np 

def noise_cancellation(audio):
    noise_threshold = 0.005
    audio[np.abs(audio) < noise_threshold] = 0
    cleaned_audio = np.copy(audio)
    cleaned_audio = cleaned_audio - np.mean(cleaned_audio)
    cleaned_audio[np.abs(cleaned_audio) < noise_threshold] = 0

    peak = np.max(np.abs(cleaned_audio))
    if peak > 0:
        cleaned_audio = cleaned_audio / peak
        
    return cleaned_audio