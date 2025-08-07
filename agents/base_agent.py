"""
Base Agent Class

Provides common functionality for all market research agents.
"""

import openai
from typing import Dict, Any
from config import OPENAI_API_KEY, OPENAI_MODEL


class BaseAgent:
    """Base class for all market research agents"""
    
    def __init__(self, name: str, system_prompt: str):
        self.name = name
        self.system_prompt = system_prompt
        self.client = openai.OpenAI(api_key=OPENAI_API_KEY)
    
    def research(self, product_idea: str) -> Dict[str, Any]:
        """Main research method - to be implemented by subclasses"""
        try:
            response = self.client.chat.completions.create(
                model=OPENAI_MODEL,
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": f"Research this product idea: {product_idea}"}
                ],
                temperature=0.7,
                max_tokens=500
            )
            
            content = response.choices[0].message.content
            return {
                "agent": self.name,
                "product_idea": product_idea,
                "analysis": content,
                "confidence": self._calculate_confidence(content)
            }
        except Exception as e:
            return {
                "agent": self.name,
                "product_idea": product_idea,
                "analysis": f"Error: {str(e)}",
                "confidence": 0.0
            }
    
    def _calculate_confidence(self, analysis: str) -> float:
        """Simple confidence calculation based on response length and keywords"""
        if not analysis or len(analysis) < 50:
            return 0.3
        
        confidence_keywords = ["likely", "evidence", "data", "research", "analysis"]
        uncertainty_keywords = ["unclear", "uncertain", "difficult", "limited"]
        
        confidence_score = len([w for w in confidence_keywords if w in analysis.lower()])
        uncertainty_score = len([w for w in uncertainty_keywords if w in analysis.lower()])
        
        base_confidence = min(0.9, len(analysis) / 300)
        keyword_adjustment = (confidence_score - uncertainty_score) * 0.1
        
        return max(0.1, min(0.9, base_confidence + keyword_adjustment))
