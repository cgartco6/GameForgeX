import requests

class GraphicsAgent:
    def create_assets(self, prompt):
        print("[GraphicsAgent] 🎨 Creating 4K background images...")
        image_url = "https://source.unsplash.com/3840x2160/?" + prompt.get("genre", "game")
        img_data = requests.get(image_url).content
        with open("assets/background.jpg", "wb") as handler:
            handler.write(img_data)
