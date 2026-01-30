import sys
import os
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Add root directory to sys.path to import tools
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.converter import JavaToPlaywrightConverter

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ConversionRequest(BaseModel):
    source_code: str
    output_path: str = None
    target_language: str = "typescript"

@app.post("/api/convert")
async def convert_code(request: ConversionRequest):
    try:
        converter = JavaToPlaywrightConverter(request.source_code)
        converted_code = converter.convert()
        
        # In a real scenario, we might write to disk here if output_path provided
        # For now, just return the string
        
        return {
            "status": "success",
            "conversion_result": {
                "converted_code": converted_code,
                "logs": ["Conversion completed successfully"]
            }
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }

# Serve Frontend
# Ensure frontend directory exists
frontend_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "frontend")
app.mount("/", StaticFiles(directory=frontend_path, html=True), name="frontend")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
