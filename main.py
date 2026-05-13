from fastapi import FastAPI

app = FastAPI()

tasks = [
  "homework",
  "build frontend",
  "check api routes"
]

@app.get("/")
def home_page():
  return "Home page"



@app.get("/api/tasks")
def get_all_tasks():
  return tasks
