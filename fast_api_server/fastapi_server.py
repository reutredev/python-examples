from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Sample data
class Task(BaseModel):
    id: int
    title: str
    description: str

tasks = [
    Task(id=1, title='Task 1', description='Description 1'),
    Task(id=2, title='Task 2', description='Description 2'),
]

# Routes
@app.get('/tasks', response_model=list[Task])
def get_tasks():
    return tasks

@app.get('/tasks/{task_id}', response_model=Task)
def get_task(task_id: int) -> Task:
    task = next((task for task in tasks if task.id == task_id), None)
    if task:
        return task
    raise HTTPException(status_code=404, detail='Task not found')

@app.post('/tasks', response_model=Task, status_code=201)
def create_task(task: Task):
    tasks.append(task)
    return task

@app.put('/tasks/{task_id}', response_model=Task)
def update_task(task_id: int, updated_task: Task):
    task = next((task for task in tasks if task.id == task_id), None)
    if not task:
        raise HTTPException(status_code=404, detail='Task not found')
    task.title = updated_task.title
    task.description = updated_task.description
    return task

@app.delete('/tasks/{task_id}')
def delete_task(task_id: int):
    task = next((task for task in tasks if task.id == task_id), None)
    if not task:
        raise HTTPException(status_code=404, detail='Task not found')
    tasks.remove(task)
    return {'message': 'Task deleted'}

# Run the server
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=5000)
