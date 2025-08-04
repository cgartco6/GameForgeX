import time
import random

class SocialMediaAPI:
    def __init__(self):
        self.platforms = {
            "facebook": {"api_key": "fb_12345"},
            "twitter": {"api_key": "tw_67890"},
            "instagram": {"api_key": "ig_abcde"},
            "linkedin": {"api_key": "li_fghij"},
            "tiktok": {"api_key": "tt_klmno"}
        }
    
    def post_to_platform(self, platform, content):
        if platform not in self.platforms:
            raise ValueError(f"Unsupported platform: {platform}")
        
        # Simulate API call
        time.sleep(random.uniform(0.5, 2.0))
        
        # Simulate success or failure
        success = random.random() > 0.2  # 80% success rate
        
        if success:
            return {
                "status": "success",
                "platform": platform,
                "post_id": f"{platform[:2]}_{random.randint(10000, 99999)}",
                "content": content
            }
        else:
            return {
                "status": "error",
                "platform": platform,
                "error_code": "API_ERROR",
                "message": "Failed to post to platform"
            }
