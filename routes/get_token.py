from fastapi import APIRouter, HTTPException
import json
import os

router = APIRouter()

TOKEN_FILE_PATH = "token.json"

@router.get("/get-token")
async def get_token():
    """
    Fetches and serves the JSON token from a file.
    Returns format: {"token": "..."}
    """
    try:
        if not os.path.exists(TOKEN_FILE_PATH):
            raise HTTPException(
                status_code=404, 
                detail=f"Token file not found at {TOKEN_FILE_PATH}"
            )
        
        with open(TOKEN_FILE_PATH, 'r') as f:
            token_data = json.load(f)
        
        # Ensure the response has the correct format
        if "token" not in token_data:
            raise HTTPException(
                status_code=500, 
                detail="Invalid token file format. Expected 'token' key."
            )
        
        return token_data
    
    except json.JSONDecodeError:
        raise HTTPException(
            status_code=500, 
            detail="Invalid JSON format in token file"
        )
    except Exception as e:
        raise HTTPException(
            status_code=500, 
            detail=f"Error reading token file: {str(e)}"
        )
