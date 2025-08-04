import uuid
import hashlib
import hmac
import os
from utils.security_utils import SecurityManager

class SecurityAgent:
    def __init__(self, params=None):
        self.agent_id = "security-" + str(uuid.uuid4())
        self.params = params or {}
        self.security_manager = SecurityManager()
        print(f"Security Agent {self.agent_id} initialized")
    
    def encrypt_data(self, data):
        return self.security_manager.encrypt(data)
    
    def decrypt_data(self, encrypted_data):
        return self.security_manager.decrypt(encrypted_data)
    
    def verify_integrity(self, data, signature):
        return self.security_manager.verify_signature(data, signature)
    
    def monitor_threats(self):
        # In a real implementation, this would continuously monitor for threats
        return {"status": "system_secure", "threats_detected": 0}
    
    def execute(self, task, params):
        if task == "encrypt":
            return self.encrypt_data(params.get("data"))
        elif task == "decrypt":
            return self.decrypt_data(params.get("data"))
        elif task == "verify":
            return self.verify_integrity(
                params.get("data"),
                params.get("signature")
            )
        elif task == "monitor":
            return self.monitor_threats()
        else:
            raise ValueError(f"Unknown task: {task}")
