from assignmentapp.models.assignment import find_assignments_by_admin, update_assignment

def get_assignments_for_admin(admin_id: str):
    return find_assignments_by_admin(admin_id)

def update_assignment_status(assignment_id: str, status: str):
    update_assignment(assignment_id, {"status": status})
