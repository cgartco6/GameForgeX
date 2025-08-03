from agents.code_agent import CodeAgent
from agents.graphics_agent import GraphicsAgent
from agents.audio_agent import AudioAgent
from agents.video_agent import VideoAgent
from agents.test_agent import TestAgent
from agents.deploy_agent import DeployAgent

class MainAgent:
    def __init__(self, game_prompt):
        self.prompt = game_prompt
        self.code_agent = CodeAgent()
        self.graphics_agent = GraphicsAgent()
        self.audio_agent = AudioAgent()
        self.video_agent = VideoAgent()
        self.test_agent = TestAgent()
        self.deploy_agent = DeployAgent()

    def build_game(self):
        print("[MainAgent] 🔧 Parsing prompt and assigning tasks...")

        logic = self.code_agent.generate_game_logic(self.prompt)
        self.graphics_agent.create_assets(self.prompt)
        self.audio_agent.create_audio(self.prompt)
        self.video_agent.create_intro(self.prompt)

        print("[MainAgent] 🧪 Running tests...")
        self.test_agent.run_tests()

        print("[MainAgent] 🚀 Packaging game...")
        self.deploy_agent.package_game()

        print("[MainAgent] ✅ Game build complete.")
