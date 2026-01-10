import numpy as np
import pandas as pd
import tensorflow as tf
import tiktoken
from typing import List, Dict, Tuple
from collections import Counter

class EntropyOptimizer:
    
    def __init__(self, model_name: str = "gpt-3.5-turbo"):
        self.encoding = tiktoken.encoding_for_model(model_name)
        self.field_stats = {}
    
    def optimize(self, df: pd.DataFrame) -> Tuple[List[str], List[Dict]]:
       
        fields = list(df.columns)
        
        # Tokenization
        field_tokens = {field: self._tokenize_field(field) for field in fields}
        
        # calculate freq
        token_frequencies = self._calculate_token_frequencies(field_tokens)
        
        # calculate Shannon entropy
        entropy_scores = {}
        for field in fields:
            entropy = self._calculate_entropy(field, df[field], token_frequencies[field])
            entropy_scores[field] = entropy
        
        # sorting
        sorted_fields = sorted(entropy_scores.items(), key=lambda x: x[1])
        optimized_order = [field for field, _ in sorted_fields]
        
        # metrics of response
        field_metrics = []
        for idx, (field, entropy) in enumerate(sorted_fields):
            field_metrics.append({
                "field_name": field,
                "entropy_score": float(entropy),
                "token_frequency": int(token_frequencies[field]),
                "optimized_position": idx
            })
        
        return optimized_order, field_metrics
    
    def _tokenize_field(self, field_name: str) -> List[int]:
        return self.encoding.encode(field_name)
    
    def _calculate_token_frequencies(self, field_tokens: Dict[str, List[int]]) -> Dict[str, int]:
        
        all_tokens = []
        for tokens in field_tokens.values():
            all_tokens.extend(tokens)
        
        token_tensor = tf.constant(all_tokens, dtype=tf.int32)
        unique_tokens, _, counts = tf.unique_with_counts(token_tensor)
        
        token_freq_map = {
            int(token): int(count) 
            for token, count in zip(unique_tokens.numpy(), counts.numpy())
        }
        
        field_frequencies = {}
        for field, tokens in field_tokens.items():
            total_freq = sum(token_freq_map.get(token, 1) for token in tokens)
            field_frequencies[field] = total_freq
        
        return field_frequencies
    
    def _calculate_entropy(self, field_name: str, field_data: pd.Series, token_freq: int) -> float:
        
        #Calculate Shannon entropy: H = -Σ(p_i * log(p_i))
        # Value diversity entropy
        value_counts = field_data.value_counts(normalize=True)
        value_probs = value_counts.values
        
        # Calculate Shannon entropy using TensorFlow
        probs_tensor = tf.constant(value_probs, dtype=tf.float32)
        epsilon = tf.constant(1e-10, dtype=tf.float32)
        log_probs = tf.math.log(probs_tensor + epsilon)
        entropy_tensor = -tf.reduce_sum(probs_tensor * log_probs)
        value_entropy = float(entropy_tensor.numpy())
        
        # Normalize token frequency
        max_freq = 100
        token_entropy = 1.0 - min(token_freq / max_freq, 1.0)
        
        
        combined_entropy = 0.7 * value_entropy + 0.3 * token_entropy
        
        return combined_entropy
    
    def get_optimization_summary(self) -> Dict:
        # generation of summary..
        return {
            "tokenizer": "tiktoken (GPT-3.5)",
            "entropy_formula": "H = -Σ(p_i * log(p_i))",
            "optimization_strategy": "Low entropy fields first (high predictability)",
            "ml_framework": "TensorFlow 2.15"
        }