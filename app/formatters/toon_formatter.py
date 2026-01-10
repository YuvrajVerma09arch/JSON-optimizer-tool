import pandas as pd
from typing import List, Any

class TOONFormatter:
   
    
    def __init__(self):
        self.separator = " | "
        self.field_separator = " "
    
    def format(self, df: pd.DataFrame, optimized_fields: List[str], array_name: str = "data") -> str:
        
        # sorting cols
        df_sorted = df[optimized_fields]
        
        # TOON header
        record_count = len(df_sorted)
        field_list = ",".join(optimized_fields)
        header = f"{array_name}[{record_count}]{{{field_list}}}"
        # TOON rows
        rows = []
        for _, row in df_sorted.iterrows():
            # Formatting each value
            formatted_values = [self._format_value(val) for val in row]
            row_str = self.field_separator.join(formatted_values)
            rows.append(row_str)
        
        rows_str = self.separator.join(rows)
        toon_output = f"{header}: {rows_str}"
        
        return toon_output
    
    def _format_value(self, value: Any) -> str:
       
        if pd.isna(value) or value is None:
            return "null"
        
        if isinstance(value, bool):
            return str(value).lower()
        
        if isinstance(value, str):
            # Escape special characters
            escaped = value.replace("|", "\\|").replace(":", "\\:")
            # Quote if contains spaces or special chars
            if " " in escaped or "," in escaped:
                return f'"{escaped}"'
            return escaped
        
        if isinstance(value, (int, float)):
            return str(value)
        
        # Fallback: convert to string
        return str(value)
    
    def format_with_metadata(self, df: pd.DataFrame, optimized_fields: List[str], 
                            array_name: str = "data") -> dict:
        """
        if needed 
        Format TOON with additional metadata
    
        Returns:
            {
                "toon": "formatted TOON string",
                "statistics": {...}
            }
        """
        toon_str = self.format(df, optimized_fields, array_name)
        
        stats = {
            "record_count": len(df),
            "field_count": len(optimized_fields),
            "avg_value_length": df.applymap(lambda x: len(str(x))).mean().mean(),
            "null_count": df.isna().sum().sum(),
            "toon_length": len(toon_str)
        }
        
        return {
            "toon": toon_str,
            "statistics": stats
        }
    
    def format_preview(self, df: pd.DataFrame, optimized_fields: List[str], 
                      max_rows: int = 5, array_name: str = "data") -> str:
      
        preview_df = df.head(max_rows)
        toon_str = self.format(preview_df, optimized_fields, array_name)
        
        if len(df) > max_rows:
            toon_str += f" [{len(df) - max_rows} more records]"
        
        return toon_str