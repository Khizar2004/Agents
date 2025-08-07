"""
Funding Agent

Specializes in funding landscape and investment activity research.
"""

from .base_agent import BaseAgent


class FundingAgent(BaseAgent):
    """Agent specialized in analyzing funding landscape and investor sentiment"""
    
    def __init__(self):
        system_prompt = """You are a venture capital research expert.
        Your job is to analyze funding activity and investor interest in a given product space.
        
        Focus on:
        - Recent funding rounds in similar companies
        - Investor sentiment and trends
        - Valuation trends
        - Market attractiveness to VCs
        
        Provide specific insights about funding landscape. Be data-driven where possible."""
        
        super().__init__("Funding", system_prompt)
