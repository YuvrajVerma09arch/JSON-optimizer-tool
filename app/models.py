from pydantic import BaseModel, Field
from typing import Any, Dict, List, Optional

class TOONMetadata(BaseModel):
    is_toonable: bool = Field(..., description="Whether data is TOON-compatible")
    detected_arrays: int = Field(0, description="Number of uniform arrays detected")
    total_records: int = Field(0, description="Total records in arrays")
    field_count: int = Field(0, description="Number of fields per record")
    optimization_method: str = Field("entropy", description="Optimization algorithm used")
    
class TokenStats(BaseModel):
    original_tokens: int = Field(..., description="Tokens in original JSON")
    toon_tokens: int = Field(..., description="Tokens in TOON format")
    savings_tokens: int = Field(..., description="Absolute token reduction")
    savings_percentage: float = Field(..., description="Percentage token reduction")
    
class FieldEntropy(BaseModel):
    # entropy optimizer using TensorFlow
    field_name: str
    entropy_score: float = Field(..., description="Shannon entropy H = -Σ(p*log(p))")  # basically formula for predicting the frequent key first
    token_frequency: int = Field(..., description="Predicted token count")
    optimized_position: int = Field(..., description="Position after entropy sorting")

class OptimizationResponse(BaseModel):
    status: str = Field("success", description="Processing status")
    original_json: Any = Field(..., description="Original uploaded JSON")
    toon_output: Optional[str] = Field(None, description="TOON-formatted output")
    token_stats: TokenStats
    metadata: TOONMetadata
    field_entropy: Optional[List[FieldEntropy]] = Field(None, description="Per-field entropy analysis")
    warnings: List[str] = Field(default_factory=list, description="Processing warnings")
    
class ErrorResponse(BaseModel):
    status: str = "error aagayi"
    detail: str
    error_type: str