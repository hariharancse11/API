from flask import Flask, request, jsonify, send_file
from gtts import gTTS
from googletrans import Translator
import os

app = Flask(__name__)

@app.route('/translate', methods=['POST'])
def translate_text():
    try:
        data = request.json
        text_to_translate = data.get('text_to_translate', '')
        destination_language = data.get('destination_language', 'en')

        # Translate text
        translator = Translator()
        translated_text = translator.translate(text_to_translate, dest=destination_language).text

        # Convert translated text to speech
        # tts = gTTS(text=translated_text, lang=destination_language)
        # audio_file_path = "translated_audio.mp3"
        # tts.save(audio_file_path)

        return jsonify({'translated_text': translated_text})

    except Exception as e:
        return jsonify({'error': str(e)}), 400
    
@app.route('/get_audio', methods=['POST'])
def get_audio():
    try:
        data = request.json
        text_to_translate = data.get('text_to_translate', '')
        destination_language = data.get('destination_language', 'en')

        # Translate text
        translator = Translator()
        translated_text = translator.translate(text_to_translate, dest=destination_language).text

        # Convert translated text to speech
        tts = gTTS(text=translated_text, lang=destination_language)
        audio_file_path = "translated_audio.mp3"
        tts.save(audio_file_path)
        return send_file(audio_file_path, as_attachment=True)

    except Exception as e:
        return jsonify({'error': str(e)}), 404

if __name__ == '__main__':
    app.run(debug=True)
