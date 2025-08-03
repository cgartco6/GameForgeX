from gtts import gTTS

class AudioAgent:
    def create_audio(self, prompt):
        print("[AudioAgent] 🔊 Generating narration and SFX...")
        intro_text = f"Welcome to {prompt.get('title', 'your adventure')}."
        tts = gTTS(intro_text)
        tts.save("assets/intro_voice.wav")
