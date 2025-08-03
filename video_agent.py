from moviepy.editor import ImageClip, AudioFileClip

class VideoAgent:
    def create_intro(self, prompt):
        print("[VideoAgent] 🎥 Creating intro cutscene...")
        clip = ImageClip("assets/background.jpg").set_duration(6)
        clip = clip.set_audio(AudioFileClip("assets/intro_voice.wav"))
        clip.write_videofile("assets/intro.mp4", fps=24)
