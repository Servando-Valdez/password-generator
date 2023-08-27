import random

from fastapi import HTTPException

def create_password(length: int, uppercase_bool: bool, lowercase_bool: bool, digits_bool: bool, symbols_bool: bool):

    check = [uppercase_bool, lowercase_bool, digits_bool, symbols_bool]
    if not True in check or length == 0:
        raise HTTPException(status_code=400, detail="Error creating password")
    if length > 50 or length < 1:
        raise HTTPException(status_code=400, detail="The range of the bassword must be between 1 and 50")
        
        # raise ValueError("At least one of the parameters must be True")

    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase_letters = uppercase_letters.lower()
    digits = "0123456789"
    symbols = "()[]{},;:.-_/\\?+*#"
    all = ""
    if uppercase_bool:
        all += uppercase_letters
    if lowercase_bool:
        all += lowercase_letters
    if digits_bool:
        all += digits
    if symbols_bool:
        all += symbols
    return "".join(random.choices(all, k=length))