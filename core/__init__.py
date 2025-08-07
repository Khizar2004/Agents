"""
Core Package

Contains evaluation and system orchestration components.
"""

from .evaluator import AgentEvaluator
from .system import MarketResearchSystem

__all__ = [
    'AgentEvaluator',
    'MarketResearchSystem'
]
