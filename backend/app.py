from flask import Flask, request, jsonify
from agents.director_agent import DirectorAgent

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    task_description = data.get('task', '')
    
    if not task_description:
        return jsonify({"error": "Task description is required"}), 400
    
    # Call the director agent to handle the task
    director = DirectorAgent()
    result = director.handle_task(task_description)
    
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)
