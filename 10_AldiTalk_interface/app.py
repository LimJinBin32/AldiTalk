# app.py
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from AldiTalk import alditalk

app = Flask(__name__)
CORS(app)  # Enable CORS if your front end is on a different origin

# Home page
@app.route('/')
def index():
    return render_template('index.html')

# About page (if needed)
@app.route('/about')
def about():
    return render_template('about.html')

# Endpoint for manual text translation
@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()
    text = data.get('text', '')
    target_lang = data.get('target_lang', 'en-US')  # Default language

    if not text:
        return jsonify({'error': 'No text provided'}), 400

    translation = alditalk.translate_text(text, target_lang)
    return jsonify({'translation': translation})

# Endpoint for speech-to-text auto-detection
@app.route('/stt_autodetect', methods=['POST'])
def stt_autodetect():
    result = alditalk.STT_autodetect(alditalk.possible_languages)
    if result:
        recognized_text, detected_language = result
        return jsonify({
            'recognized_text': recognized_text,
            'detected_language': detected_language
        })
    else:
        return jsonify({'error': 'Speech not recognized'}), 400

# Endpoint for speech-to-text Cantonese and other specific languages
@app.route("/stt_basic", methods=["POST"])
def handle_stt_basic():
    try:
        data = request.get_json()
        if not data or "target_lang" not in data:
            print("❌ [Error] Invalid STT request:", data)  # Debugging
            return jsonify({"error": "Invalid request data"}), 400

        target_lang = data["target_lang"]
        print(f"🎤 STT Request for {target_lang}")  # Debugging

        recognized_text = alditalk.STT(target_lang)

        if not recognized_text:
            return jsonify({"error": "Speech not recognized"}), 400

        return jsonify({"recognized_text": recognized_text})
    
    except Exception as e:
        print(f"❌ [Error] Exception in STT Basic: {e}")  # Debugging log
        return jsonify({"error": str(e)}), 500

    
# Endpoint for STT for Hokkien only
@app.route("/stt_hokkien", methods=["POST"])
def handle_stt_hokkien():
    try:
        data = request.get_json()
        target_lang = data.get("target_lang", "zh-CN")  # Default to Mandarin
        recognized_text = alditalk.custom_STT(target_lang)
        return jsonify({"recognized_text": recognized_text})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Endpoint for translating Hokkien
@app.route("/translate_hokkien", methods=["POST"])
def handle_translate_hokkien():
    try:
        data = request.get_json()
        if not data or "text" not in data:
            return jsonify({"error": "Invalid request data"}), 400

        input_text = data["text"]
        print(f"Received Hokkien translation request: {input_text}")  # Debugging

        translation, audio_file_path = alditalk.translate_hokkien(input_text) 

        if translation is None:
            return jsonify({"error": "Hokkien translation failed"}), 400

        return jsonify({"translation": translation ,"audio_url": audio_file_path})  # Only return translation
    except Exception as e:
        print(f"Error in Translate Hokkien: {str(e)}")  # Debugging log
        return jsonify({"error": str(e)}), 500

# Endpoint for tts
@app.route("/tts", methods=["POST"])
def handle_tts():
    try:
        data = request.get_json()
        if not data or "text" not in data or "language" not in data:
            return jsonify({"error": "Invalid request data"}), 400

        text = data["text"]
        language = data["language"]

        print(f"🎙️ TTS Request: {language} - {text}")  # Debugging

        audio_url = alditalk.TTS(text, language)

        if not audio_url:
            return jsonify({"error": "TTS generation failed"}), 500

        return jsonify({"audio_url": audio_url})

    except Exception as e:
        pass

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
