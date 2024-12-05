def payload_arg(payload_type: str) -> str:
    return "json" if payload_type == "json" else "data"
