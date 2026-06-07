import pandas as pd
from typing import Dict, List, Any, Tuple

class TOONDetector:
    
    def __init__(self):
        self.detected_arrays = []
        self.metadata = {}
    
    def detect(self, json_data: Any) -> Tuple[bool, Dict[str, Any]]:
       
        if isinstance(json_data, list):
            return self._detect_array(json_data)
        elif isinstance(json_data, dict):
            return self._detect_object(json_data)
        else:
            return False, {"error": "Unsupported JSON type"}
    
    def _detect_array(self, data: List[Any]) -> Tuple[bool, Dict[str, Any]]:
        if not data:
            return False, {"error": "Empty array"}
        
        if not all(isinstance(item, dict) for item in data):
            return False, {"error": "Array contains non-dict items"}
        
        
        try:
            df = pd.json_normalize(data)
            
            metadata = {
                "is_toonable": True,
                "detected_arrays": 1,
                "total_records": len(data),
                "field_count": len(df.columns),
                "fields": list(df.columns),
                "data_types": df.dtypes.astype(str).to_dict(),
                "sample_data": df.head(3).to_dict('records')
            }
            
            return True, metadata
            
        except Exception as e:
            return False, {"error": f"Pandas normalization failed: {str(e)}"}
    
    def _detect_object(self, data: Dict[str, Any]) -> Tuple[bool, Dict[str, Any]]:
        toonable_arrays = []
        
        for key, value in data.items():
            if isinstance(value, list) and value:
                is_toonable, meta = self._detect_array(value)
                if is_toonable:
                    toonable_arrays.append({
                        "key": key,
                        "metadata": meta
                    })
        
        if toonable_arrays:
            return True, {
                "is_toonable": True,
                "detected_arrays": len(toonable_arrays),
                "arrays": toonable_arrays
            }
        
        return False, {"error": "No TOON-compatible arrays found in object"}
    #generation of dataframe
    def get_dataframe(self, json_data: Any) -> pd.DataFrame:
       
        if isinstance(json_data, list):
            return pd.json_normalize(json_data)
        elif isinstance(json_data, dict):
            # will Finding first TOON-compatible array
            for value in json_data.values():
                if isinstance(value, list) and value:
                    is_toonable, _ = self._detect_array(value)
                    if is_toonable:
                        return pd.json_normalize(value)
        
        raise ValueError("No TOON-compatible structure found")
