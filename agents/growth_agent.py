"""
Growth Agent

Specializes in market growth analysis and revenue potential research.
"""

from .base_agent import BaseAgent


class GrowthAgent(BaseAgent):
    """Agent specialized in market growth and revenue potential analysis"""
    
    def __init__(self):
        system_prompt = """You are a market growth analyst.
        Your job is to evaluate market size, growth potential, and revenue opportunities.
        
        Focus on:
        - Market size and growth rate
        - Revenue potential
        - Market maturity and lifecycle stage
        - Economic factors affecting growth
        
        Provide quantitative insights where possible. Focus on growth trajectory."""
        
        super().__init__("Growth", system_prompt)
