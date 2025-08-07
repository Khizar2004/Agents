"""
Decision Agent

Synthesizes research from all agents and makes final investment recommendation.
"""

from typing import Dict, Any
from .base_agent import BaseAgent
from config import OPENAI_MODEL


class DecisionAgent(BaseAgent):
    """Agent specialized in synthesizing research and making final recommendations"""
    
    def __init__(self):
        system_prompt = """You are a strategic investment advisor.
        Your job is to synthesize market research and make a final recommendation.
        
        You will receive analysis from three areas: competitors, funding, and growth.
        Based on this, provide:
        - Overall recommendation (Good/Neutral/Poor opportunity)
        - Key reasons supporting your decision
        - Main risks and opportunities
        - Confidence level in your assessment
        
        Be decisive but balanced in your judgment."""
        
        super().__init__("Decision", system_prompt)
    
    def make_decision(self, incumbents_analysis: str, funding_analysis: str, 
                     growth_analysis: str, product_idea: str) -> Dict[str, Any]:
        """Make final decision based on all agent inputs"""
        combined_prompt = f"""
        Product Idea: {product_idea}
        
        COMPETITORS ANALYSIS:
        {incumbents_analysis}
        
        FUNDING ANALYSIS:
        {funding_analysis}
        
        GROWTH ANALYSIS:
        {growth_analysis}
        
        Based on the above research, provide your final recommendation."""
        
        try:
            response = self.client.chat.completions.create(
                model=OPENAI_MODEL,
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": combined_prompt}
                ],
                temperature=0.5,   # Lower temperature for more consistent decisions
                max_tokens=400
            )
            
            content = response.choices[0].message.content
            recommendation = self._extract_recommendation(content)
            
            return {
                "agent": self.name,
                "product_idea": product_idea,
                "recommendation": recommendation,
                "reasoning": content,
                "confidence": self._calculate_confidence(content)
            }
        except Exception as e:
            return {
                "agent": self.name,
                "product_idea": product_idea,
                "recommendation": "Error",
                "reasoning": f"Error: {str(e)}",
                "confidence": 0.0
            }
    
    def _extract_recommendation(self, analysis: str) -> str:
        """Extract recommendation from analysis text"""
        analysis_lower = analysis.lower()
        
        if any(word in analysis_lower for word in ["good opportunity", "recommend", "positive", "strong potential"]):
            return "Good"
        elif any(word in analysis_lower for word in ["poor", "avoid", "risky", "challenging", "difficult"]):
            return "Poor"
        else:
            return "Neutral"
