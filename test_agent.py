import subprocess

class TestAgent:
    def run_tests(self):
        print("[TestAgent] 🧪 Testing game file...")
        try:
            subprocess.run(["python", "game.py"], check=True)
            print("[TestAgent] ✅ No errors detected.")
        except subprocess.CalledProcessError as e:
            print(f"[TestAgent] ❌ Game crashed: {e}")
