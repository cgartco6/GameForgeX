from utils.ai_utils import generate_with_ai

class DirectorAgent:
    def __init__(self):
        pass
    
    def handle_task(self, task_description):
        # For now, we'll directly use the AI utility to generate code
        # In a more advanced system, we would determine which agent to use or create a new one
        prompt = f"""
        You are an AI agent that can generate code, scripts, or even create new AI agents.
        The user has provided the following task: 
        
        {task_description}
        
        Please generate the complete solution. If it's code, provide the code in a code block with the correct syntax.
        If the task requires multiple steps or agents, break it down and provide the complete solution.
        """
        
        response = generate_with_ai(prompt)
        return response
