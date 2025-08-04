import os
import hashlib
import hmac
from cryptography.fernet import Fernet

class SecurityManager:
    def __init__(self):
        # In a real system, these would be securely stored and rotated
        self.encryption_key = Fernet.generate_key()
        self.hmac_secret = os.urandom(32)
        self.cipher = Fernet(self.encryption_key)
        print("Security Manager initialized")
    
    def encrypt(self, data):
        """Encrypt data using Fernet symmetric encryption"""
        if isinstance(data, str):
            data = data.encode()
        return self.cipher.encrypt(data).decode()
    
    def decrypt(self, encrypted_data):
        """Decrypt data using Fernet symmetric encryption"""
        if isinstance(encrypted_data, str):
            encrypted_data = encrypted_data.encode()
        return self.cipher.decrypt(encrypted_data).decode()
    
    def generate_signature(self, data):
        """Generate HMAC signature for data"""
        if isinstance(data, str):
            data = data.encode()
        return hmac.new(self.hmac_secret, data, hashlib.sha256).hexdigest()
    
    def verify_signature(self, data, signature):
        """Verify HMAC signature for data"""
        expected_signature = self.generate_signature(data)
        return hmac.compare_digest(expected_signature, signature)
    
    def verify_request(self, request):
        """Verify the integrity and authenticity of an incoming request"""
        # In a real implementation, this would check API keys, signatures, etc.
        return True  # Simplified for demo
    
    def verify_agent_creation(self, agent_type, params):
        """Security policy check before creating a new agent"""
        # Implement actual security policies here
        restricted_agents = ["security", "payments"]
        if agent_type in restricted_agents:
            # Check for admin privileges
            return params.get("admin_token") == "SECURE_ADMIN_TOKEN"
        return True
