# AldiTalk/alditalk.py
import os
from dotenv import load_dotenv
import requests
import azure.cognitiveservices.speech as speechsdk

# Load environment variables from .env
load_dotenv()

SPEECH_KEY = os.getenv("SPEECH_KEY")
SPEECH_REGION = os.getenv("SPEECH_REGION")
TRANSLATOR_KEY = os.getenv("TRANSLATOR_KEY")
TRANSLATOR_REGION = os.getenv("TRANSLATOR_REGION")
TRANSLATOR_ENDPOINT = os.getenv("TRANSLATOR_ENDPOINT")
CUSTOM_KEY = os.getenv("CUSTOM_KEY")
CUSTOM_REGION = os.getenv("CUSTOM_REGION")
CUSTOM_ENDPOINT = os.getenv("CUSTOM_ENDPOINT")

voices_map = {
    "en-US": "en-US-JennyNeural",
    "zh-CN": "zh-CN-XiaoxiaoNeural",
    "yue-CN": "zh-HK-HiuGaaiNeural",
    "hi-IN": "hi-IN-MadhurNeural",
    "ta-IN": "ta-IN-ValluvarNeural",
    "ms-MY": "ms-MY-OsmanNeural",
    
}

possible_languages = ["en-US", "zh-CN", "ta-IN", "ms-MY"]  # Example languages

def translate_text(text, target_lang):
    headers = {
        'Ocp-Apim-Subscription-Key': TRANSLATOR_KEY,
        'Ocp-Apim-Subscription-Region': TRANSLATOR_REGION,
        'Content-type': 'application/json'
    }
    params = {'api-version': '3.0', 'to': target_lang}
    body = [{'text': text}]

    response = requests.post(TRANSLATOR_ENDPOINT, headers=headers, params=params, json=body)
    result = response.json()
    translated_text = result[0]['translations'][0]['text']
    return translated_text

def STT_autodetect(possible_lang):
    speech_config = speechsdk.SpeechConfig(subscription=SPEECH_KEY, region=SPEECH_REGION)
    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    auto_detect_config = speechsdk.languageconfig.AutoDetectSourceLanguageConfig(languages=possible_lang)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config,audio_config=audio_config,auto_detect_source_language_config=auto_detect_config)
    speech_recognizer.properties.set_property(speechsdk.PropertyId.SpeechServiceConnection_InitialSilenceTimeoutMs, "10000")
    speech_recognizer.properties.set_property(speechsdk.PropertyId.SpeechServiceConnection_EndSilenceTimeoutMs, "5000")
    
    result = speech_recognizer.recognize_once()
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        detected_language = result.properties[speechsdk.PropertyId.SpeechServiceConnection_AutoDetectSourceLanguageResult]
        recognized_text = result.text
        return recognized_text, detected_language
    else:
        print(f"Speech not recognized: {result.reason}")
        return None

def STT(target_lang):
    speech_config = speechsdk.SpeechConfig(subscription=SPEECH_KEY, region=SPEECH_REGION)
    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config,audio_config=audio_config,language=target_lang)
    speech_recognizer.properties.set_property(speechsdk.PropertyId.SpeechServiceConnection_InitialSilenceTimeoutMs, "10000")
    speech_recognizer.properties.set_property(speechsdk.PropertyId.SpeechServiceConnection_EndSilenceTimeoutMs, "5000")
    
    result = speech_recognizer.recognize_once()
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        recognized_text = result.text
        return recognized_text
    else:
        print(f"Speech not recognized: {result.reason}")


import time
import glob

def TTS(translated_text, target_lang):
    speech_config = speechsdk.SpeechConfig(subscription=SPEECH_KEY, region=SPEECH_REGION)
    voice = voices_map[target_lang]
    speech_config.speech_synthesis_voice_name = voice
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)
    result = synthesizer.speak_text_async(translated_text).get()
    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        os.makedirs("static/audio", exist_ok=True)
        old_files = glob.glob("static/audio/tts_audio_*.wav")
        for file in old_files:
                os.remove(file)
        audio_filename = f"tts_audio_{int(time.time())}.wav"
        audio_path = os.path.join("static/audio", audio_filename)
        with open(audio_path, "wb") as audio_file:
            audio_file.write(result.audio_data)
        print(f"✅ TTS Audio Saved: {audio_path}") 
        return f"/static/audio/{audio_filename}"  
    else:
        print(f"Speech synthesis failed: {result.reason}")

def custom_STT(target_lang):
    speech_config = speechsdk.SpeechConfig(subscription=CUSTOM_KEY, region=CUSTOM_REGION)
    speech_config.endpoint_id = CUSTOM_ENDPOINT
    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config,audio_config=audio_config,language=target_lang)
    speech_recognizer.properties.set_property(speechsdk.PropertyId.SpeechServiceConnection_InitialSilenceTimeoutMs, "10000")
    speech_recognizer.properties.set_property(speechsdk.PropertyId.SpeechServiceConnection_EndSilenceTimeoutMs, "5000")
    print("speak now")
    
    result = speech_recognizer.recognize_once()
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        recognized_text = result.text
        return recognized_text
    else:
        print(f"Speech not recognized: {result.reason}")


import json
from openai import AzureOpenAI
from transformers import VitsModel, AutoTokenizer
import torch
import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write


# Azure OpenAI Credentials (Replace with your values)
endpoint = os.getenv("OPENAI_ENDPOINT") 
deployment = os.getenv("OPENAI_MODEL") 
subscription_key = os.getenv("OPENAI_KEY") 

# Initialize Azure OpenAI Client
client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=subscription_key,
    api_version="2024-05-01-preview",
)

def translate_hokkien(input_text):
    """
    Translates an English or Mandarin sentence to Pe̍h-ōe-jī (POJ) using Azure OpenAI.
    
    Parameters:
        input_text (str): The input sentence in English or Mandarin.
        
    Returns:
        str: The POJ transliteration.
    """
    chat_prompt = [
        {
            "role": "system",
            "content": [
                {
                    "type": "text",
                    "text": "You are an expert in Hokkien (Singapore Hokkien or Taiwanese Min Nan) and Pe̍h-ōe-jī (POJ). "
                            "Your task is to convert Input sentences into accurate POJ transliterations. "
                            "Use correct tone marks and pick the right pronunciation for each character. "
                            "Use English words if you do not know POJ equivalent.\n\n"
                            "Example:\n"
                            "Input: 你吃饱了吗？\nOutput: Li chia̍h-pá bô?\n\n"
                            "Input: How are you feeling today?\nOutput: Li kám-kak án-ne bô?"
                }
            ]
        },
        {
            "role": "user",
            "content": [{"type": "text", "text": input_text}]
        }
    ]
    
    # Include speech result if speech is enabled 
    messages = chat_prompt 
        
    # Generate the completion 
    completion = client.chat.completions.create( 
        model=deployment,
        messages=messages,
        max_tokens=200, 
        temperature=0.7, 
        top_p=0.95, 
        frequency_penalty=0, 
        presence_penalty=0,
        stop=None, 
        stream=False
    )

    # Extract and return the response
    response_text = json.loads(completion.to_json())["choices"][0]["message"]["content"]

    # Load the model and tokenizer
    model = VitsModel.from_pretrained("facebook/mms-tts-nan")
    tokenizer = AutoTokenizer.from_pretrained("facebook/mms-tts-nan")

    # Tokenize the text
    inputs = tokenizer(response_text, return_tensors="pt")

    # Generate the waveform
    with torch.no_grad():
        output = model(**inputs).waveform

    # Define output file name
    audio_directory = "static/audio"
    output_filename = f"tts_audio_{int(time.time())}.wav"
    output_path = os.path.join(audio_directory, output_filename)

    # Convert PyTorch tensor to NumPy array for saving and playback
    volume_factor = 2  # Increase volume (adjust as needed)
    audio_np = output.squeeze().cpu().numpy() * volume_factor
    audio_np = np.clip(audio_np, -1.0, 1.0)  # Prevent distortion

    # Save audio to WAV file  
    write(output_path, rate=model.config.sampling_rate, data=(audio_np * 32767).astype("int16"))  # Convert to 16-bit PCM
 
    # Print confirmation
    print(f"Audio saved as {output_path}")

    # Play the saved file (optional)
    sd.play(audio_np, samplerate=model.config.sampling_rate)
    sd.wait()  # Wait for playback to finish


    return "[Hokkien audio generated]", output_path

