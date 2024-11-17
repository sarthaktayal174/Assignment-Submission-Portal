from fastapi import APIRouter, HTTPException, Depends
from assignmentapp.services.assignment_service import get_assignments_for_admin, update_assignment_status
from assignmentapp.schemas.assignment_schema import AssignmentStatusUpdate

admin_router = APIRouter()

@admin_router.get("/assignments")
def view_assignments(admin_id: str):
    assignments = get_assignments_for_admin(admin_id)
    return assignments

@admin_router.post("/assignments/{id}/accept")
def accept_assignment(id: str):
    update_assignment_status(id, "accepted")
    return {"message": "Assignment accepted"}

@admin_router.post("/assignments/{id}/reject")
def reject_assignment(id: str):
    update_assignment_status(id, "rejected")
    return {"message": "Assignment rejected"}
