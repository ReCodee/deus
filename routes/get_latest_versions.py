from fastapi import APIRouter, HTTPException
import json
import os

router = APIRouter()

VERSIONS_FILE_PATH = "versions.json"

@router.get("/get-latest-versions")
async def get_latest_versions():
    """
    Fetches and returns the versions array from versions.json file.
    """
    try:
        if not os.path.exists(VERSIONS_FILE_PATH):
            raise HTTPException(
                status_code=404, 
                detail=f"Versions file not found at {VERSIONS_FILE_PATH}"
            )
        
        with open(VERSIONS_FILE_PATH, 'r') as f:
            versions_data = json.load(f)
        
        return versions_data
    
    except json.JSONDecodeError:
        raise HTTPException(
            status_code=500, 
            detail="Invalid JSON format in versions file"
        )
    except Exception as e:
        raise HTTPException(
            status_code=500, 
            detail=f"Error reading versions file: {str(e)}"
        )
