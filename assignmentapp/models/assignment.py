from pymongo.collection import Collection
from assignmentapp.utils.db import db
from bson import ObjectId

# Get the "assignments" collection from the database
assignment_collection: Collection = db.get_collection("assignments")

def create_assignment(data: dict) -> str:
    """
    Insert a new assignment into the database.
    Returns the ID of the newly created assignment.
    """
    result = assignment_collection.insert_one(data)
    return str(result.inserted_id)

def find_assignments_by_admin(admin_id: str) -> list:
    """
    Retrieve all assignments tagged to a specific admin.
    Returns a list of assignments.
    """
    assignments = assignment_collection.find({"admin": admin_id})
    return [serialize_assignment(assignment) for assignment in assignments]

def find_assignment_by_id(assignment_id: str) -> dict:
    """
    Retrieve a specific assignment by its ID.
    Returns the assignment document if found, otherwise None.
    """
    assignment = assignment_collection.find_one({"_id": ObjectId(assignment_id)})
    return serialize_assignment(assignment) if assignment else None

def update_assignment(assignment_id: str, updates: dict) -> bool:
    """
    Update an assignment's status or details.
    Returns True if the update was successful, False otherwise.
    """
    result = assignment_collection.update_one(
        {"_id": ObjectId(assignment_id)},
        {"$set": updates}
    )
    return result.modified_count > 0

def serialize_assignment(assignment: dict) -> dict:
    """
    Convert MongoDB's BSON object to a JSON-serializable dictionary.
    """
    return {
        "id": str(assignment["_id"]),
        "user_id": assignment["user_id"],
        "task": assignment["task"],
        "admin": assignment["admin"],
        "status": assignment.get("status", "pending"),
        "created_at": assignment.get("created_at"),
    }
