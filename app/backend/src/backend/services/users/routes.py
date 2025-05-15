from fastapi import APIRouter

router = APIRouter(prefix="/users")


@router.post("/")
async def create_user():
    return {"message": "User created successfully"}

@router.get("/me")
async def get_current_user():
    return {"message": "User retrieved successfully"}

@router.put("/me")
async def update_user():
    return {"message": "User updated successfully"}

@router.delete("/me")
async def delete_user():
    return {"message": "User deleted successfully"}

@router.get("/")
async def get_users():
    return {"message": "Users retrieved successfully"}

@router.get("/{user_id}")
async def get_user():
    return {"message": "User retrieved successfully"}

@router.put("/{user_id}")
async def update_user():
    return {"message": "User updated successfully"}

@router.delete("/{user_id}")
async def delete_user():
    return {"message": "User deleted successfully"}

@router.get("/by-email/{email}")
async def get_user_by_email():
    return {"message": "User retrieved successfully"}

@router.get("/search")
async def search_users():
    return {"message": "Users retrieved successfully"}

@router.get("/username-available/{username}")
async def is_username_available():
    return {"message": "Username availability checked successfully"}
