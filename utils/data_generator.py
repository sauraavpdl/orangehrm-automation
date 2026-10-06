import uuid

def unique_name(prefix: str) -> str:
    return f"{prefix}_{uuid.uuid4().hex[:3]}"