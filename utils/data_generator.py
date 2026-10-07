import uuid
import random

def unique_name(prefix: str) -> str:
    return f"{prefix}_{uuid.uuid4().hex[:3]}"

def unique_employee_id() -> str:
    return str(random.randint(100000, 999999))