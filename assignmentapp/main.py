from fastapi import FastAPI
from assignmentapp.routes.user_routes import user_router
from assignmentapp.routes.admin_routes import admin_router

app = FastAPI(title="Assignment Submission Portal")

# Include routes
app.include_router(user_router, prefix="/user")
app.include_router(admin_router, prefix="/admin")

# Root endpoint
@app.get("/")
def home():
    return {"message": "Welcome to the Assignment Submission Portal!"}
