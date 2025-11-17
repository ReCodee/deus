from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import os
from datetime import datetime

router = APIRouter()

LOGS_DIR = "logs"

class LogData(BaseModel):
    data: str

@router.post("/push-logs")
async def push_logs(log_data: LogData):
    """
    Saves the provided data in a text file.
    Data is cleaned, trimmed, and appended only if not empty.
    Logs are saved in logs directory with filename DD-MM-YYYY.txt
    Request format: {"data": "..."}
    """
    try:
        # Clean and trim the data
        cleaned_data = log_data.data.strip()
        
        # Only append if data is not empty
        if not cleaned_data:
            return {
                "success": True, 
                "message": "Empty data after cleaning, nothing appended"
            }
        
        # Create logs directory if it doesn't exist
        os.makedirs(LOGS_DIR, exist_ok=True)
        
        # Generate filename based on current date (DD-MM-YYYY)
        current_date = datetime.now().strftime("%d-%m-%Y")
        log_file_path = os.path.join(LOGS_DIR, f"{current_date}.txt")
        
        # Append to the log file (create if doesn't exist)
        with open(log_file_path, 'a') as f:
            f.write(cleaned_data + '\n')
        
        return {
            "success": True, 
            "message": f"Log data appended successfully to {current_date}.txt"
        }
    
    except Exception as e:
        raise HTTPException(
            status_code=500, 
            detail=f"Error writing to log file: {str(e)}"
        )
