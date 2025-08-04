from agents.director_agent import DirectorAgent
import time

def main():
    print("Starting AgentForge Ecosystem...")
    
    # Initialize director agent
    director = DirectorAgent()
    
    # Create initial agents
    marketing_agent = director.create_agent("marketing")
    social_agent = director.create_agent("social_media")
    security_agent = director.create_agent("security")
    healing_agent = director.create_agent("self_healing")
    training_agent = director.create_agent("training")
    compliance_agent = director.create_agent("compliance")
    payments_agent = director.create_agent("payments")
    
    print("\nAgent System Initialized. All agents are operational.\n")
    
    # Demonstrate agent capabilities
    print("Creating a marketing campaign...")
    campaign = marketing_agent.execute("create_campaign", {
        "name": "AgentForge Launch",
        "platforms": ["facebook", "instagram", "twitter"],
        "content": "Discover the future of AI agents with AgentForge!"
    })
    print(f"Campaign created: {campaign['id']}")
    
    print("\nScheduling social media posts...")
    social_agent.execute("post_to_all", {
        "content": "We're excited to launch AgentForge - the AI agent ecosystem that builds more agents! #AI #Innovation"
    })
    
    print("\nPerforming security check...")
    data = "Sensitive information"
    encrypted = security_agent.execute("encrypt", {"data": data})
    print(f"Encrypted data: {encrypted}")
    
    print("\nPerforming system health check...")
    health_report = healing_agent.execute("health_check", {})
    print(f"System health: {health_report['system_status']}")
    
    print("\nTraining a new model...")
    training_job = training_agent.execute("train_model", {
        "dataset": "customer_behavior_data",
        "model_type": "predictive"
    })
    print(f"Training completed with accuracy: {training_job.get('accuracy', 'N/A')}")
    
    print("\nAgentForge ecosystem is running and ready for tasks!")

if __name__ == "__main__":
    main()
