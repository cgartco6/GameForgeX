document.addEventListener('DOMContentLoaded', function() {
    const taskForm = document.getElementById('task-form');
    const taskDescription = document.getElementById('task-description');
    const taskResult = document.getElementById('task-result');
    const resultCode = document.getElementById('result-code');

    taskForm.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        const task = taskDescription.value.trim();
        if (!task) {
            alert('Please enter a task description');
            return;
        }
        
        // Show loading state
        resultCode.textContent = 'Generating...';
        taskResult.style.display = 'block';
        
        try {
            const response = await fetch('http://localhost:5000/generate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ task })
            });
            
            const data = await response.json();
            if (data.error) {
                resultCode.textContent = data.error;
            } else {
                resultCode.textContent = data.result;
            }
        } catch (error) {
            resultCode.textContent = 'Failed to connect to the server.';
            console.error('Error:', error);
        }
    });
});
