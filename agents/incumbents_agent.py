"""
Incumbents Agent

Specializes in competitive analysis and market incumbents research.
"""

from .base_agent import BaseAgent


class IncumbentsAgent(BaseAgent):
    """Agent specialized in analyzing competitors and market incumbents"""
    
    def __init__(self):
        system_prompt = """You are a market research expert specializing in competitive analysis. 
        Your job is to identify existing competitors and their key features for a given product idea.
        
        Focus on:
        - Main competitors in the space
        - Their key features and differentiators
        - Market positioning
        - Strengths and weaknesses
        
        Provide specific, actionable insights. Be concise but thorough."""
        
        super().__init__("Incumbents", system_prompt)
