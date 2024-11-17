from pydantic import BaseModel

class AssignmentUpload(BaseModel):
    user_id: str
    task: str
    admin: str

class AssignmentStatusUpdate(BaseModel):
    status: str  # Acceptable values: "accepted", "rejected"
