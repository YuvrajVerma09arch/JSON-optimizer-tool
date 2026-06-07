from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from .validators.token_validator import TOKEN_validator
import json
from typing import Dict, Any
from .models import OptimizationResponse, TOONMetadata, TokenStats, FieldEntropy
from .detectors import TOONDetector
from .optimizers import EntropyOptimizer
from .formatters import TOONFormatter
app = FastAPI(
    title="TOON JSON Optimizer",
    description="Reduce LLM tokens by 40-60% using Table-Oriented Object Notation",
    version="1.0.0"
)

# CORS for browser
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
detector = TOONDetector()
optimizer = EntropyOptimizer()
formatter = TOONFormatter()
validator = TOKEN_validator()

@app.get("/")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "TOON JSON Optimizer",
        "version": "1.0.0",
        "endpoints": {
            "upload": "/upload",
            "docs": "/docs",
            "health": "/"
        },
        "capabilities": {
            "detection": "Pandas-powered",
            "optimization": "TensorFlow entropy analysis",
            "tokenization": "tiktoken (GPT-3.5)",
            "expected_savings": "40-60%"
        }
    }

@app.post("/upload", response_model=OptimizationResponse)
async def optimize_json(file: UploadFile = File()):
    warnings = []
    
    try:
        # Reading and parsing json file
        content = await file.read()
        original_json = json.loads(content.decode('utf-8'))
        
        # Validating in
        if not isinstance(original_json, (list, dict)):
            raise HTTPException(
                status_code=400,
                detail="JSON must be an array or object"
            )
        
        #  TOON Detection
        is_toonable, detection_meta = detector.detect(original_json)
        
        if not is_toonable:
            raise HTTPException(
                status_code=400,
                detail=f"JSON is not TOON-compatible: {detection_meta.get('error', 'Unknown error')}"
            )
        
        # DataFrame for processing
        df = detector.get_dataframe(original_json)
        
        #  Entropy Optimization (TensorFlow)
        optimized_fields, field_entropy_list = optimizer.optimize(df)
        
        # Formatting
        toon_output = formatter.format(df, optimized_fields, array_name="data")
        
        # Token Validation
        token_stats_dict = validator.validate(original_json, toon_output)
        
        # Building metadata
        metadata = TOONMetadata(
            is_toonable=is_toonable,
            detected_arrays=detection_meta.get('detected_arrays', 1),
            total_records=detection_meta.get('total_records', len(df)),
            field_count=detection_meta.get('field_count', len(df.columns)),
            optimization_method="tensorflow_entropy"
        )
        
        # Building token stats
        token_stats = TokenStats(**token_stats_dict)
        
        # Building  entropy list
        field_entropy_objects = [FieldEntropy(**fe) for fe in field_entropy_list]
        
        # Added warnings for savings is lower than expected
        if token_stats.savings_percentage < 30:
            warnings.append(
                f"Token savings ({token_stats.savings_percentage}%) below expected range (40-60%). "
                "This may occur with small datasets or highly diverse field values."
            )
        
        # Building response
        response = OptimizationResponse(
            status="success",
            original_json=original_json,
            toon_output=toon_output,
            token_stats=token_stats,
            metadata=metadata,
            field_entropy=field_entropy_objects,
            warnings=warnings
        )
        
        return response
        
    except json.JSONDecodeError:
        raise HTTPException(
            status_code=400,
            detail="Invalid JSON format. Please upload a valid JSON file."
        )
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=f"Data processing error: {str(e)}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Internal server error: {str(e)}"
        )

@app.post("/validate")
async def validate_only(file: UploadFile = File()):
    try:
        content = await file.read()
        original_json = json.loads(content.decode('utf-8'))
        
        is_toonable, detection_meta = detector.detect(original_json)
        
        return {
            "is_toonable": is_toonable,
            "metadata": detection_meta,
            "recommendation": "Proceed with /upload for full optimization" if is_toonable else "JSON structure not suitable for TOON"
        }
        
    except json.JSONDecodeError:
        raise HTTPException(
            status_code=400,
            detail="Invalid JSON format"
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Validation error: {str(e)}"
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
# Visit this http://localhost:8000/docs
# not this  http://0.0.0.0:8000

