"""
Market Research System Orchestrator

Main system class that coordinates all agents and evaluation.
"""

from typing import Dict, Any
from agents import IncumbentsAgent, FundingAgent, GrowthAgent, DecisionAgent
from .evaluator import AgentEvaluator


class MarketResearchSystem:
    """Main system that orchestrates the 4-agent market research process"""
    
    def __init__(self):
        self.incumbents_agent = IncumbentsAgent()
        self.funding_agent = FundingAgent()
        self.growth_agent = GrowthAgent()
        self.decision_agent = DecisionAgent()
        self.evaluator = AgentEvaluator()
    
    def research_product_idea(self, product_idea: str) -> Dict[str, Any]:
        """Run complete market research analysis"""
        print(f"\n Researching product idea: {product_idea}")
        print("=" * 60)
        
        results = {}
        
        # Step 1: Run individual research agents
        print("\n1️⃣  Analyzing Competitors...")
        incumbents_result = self.incumbents_agent.research(product_idea)
        results["Incumbents"] = incumbents_result
        self._print_agent_result("Incumbents", incumbents_result)
        
        print("\n2️⃣  Researching Funding Landscape...")
        funding_result = self.funding_agent.research(product_idea)
        results["Funding"] = funding_result
        self._print_agent_result("Funding", funding_result)
        
        print("\n3️⃣  Evaluating Growth Potential...")
        growth_result = self.growth_agent.research(product_idea)
        results["Growth"] = growth_result
        self._print_agent_result("Growth", growth_result)
        
        # Step 2: Make final decision
        print("\n4️⃣  Making Final Recommendation...")
        decision_result = self.decision_agent.make_decision(
            incumbents_result.get("analysis", ""),
            funding_result.get("analysis", ""),
            growth_result.get("analysis", ""),
            product_idea
        )
        results["Decision"] = decision_result
        self._print_decision_result(decision_result)
        
        # Step 3: Evaluate system performance
        print("\n📊 System Evaluation")
        print("-" * 30)
        evaluation = self.evaluator.evaluate_full_research(results)
        self._print_evaluation(evaluation)
        
        return {
            "research_results": results,
            "evaluation": evaluation,
            "product_idea": product_idea
        }
    
    def _print_agent_result(self, agent_name: str, result: Dict[str, Any]):
        """Print formatted agent result"""
        analysis = result.get("analysis", "No analysis available")
        confidence = result.get("confidence", 0.0)
        
        print(f"   Analysis: {analysis[:200]}{'...' if len(analysis) > 200 else ''}")
        print(f"   Confidence: {confidence:.1f}")
    
    def _print_decision_result(self, result: Dict[str, Any]):
        """Print formatted decision result"""
        recommendation = result.get("recommendation", "Unknown")
        reasoning = result.get("reasoning", "No reasoning available")
        confidence = result.get("confidence", 0.0)
        
        # Color coding for recommendations
        colors = {
            "Good": "🟢",
            "Neutral": "🟡", 
            "Poor": "🔴",
            "Error": "⚠️"
        }
        
        print(f"   {colors.get(recommendation, '❓')} Recommendation: {recommendation}")
        print(f"   Reasoning: {reasoning[:300]}{'...' if len(reasoning) > 300 else ''}")
        print(f"   Confidence: {confidence:.1f}")
    
    def _print_evaluation(self, evaluation: Dict[str, Any]):
        """Print system evaluation summary"""
        system_perf = evaluation.get("system_performance", {})
        overall_score = system_perf.get("overall_score", 0)
        recommendations = evaluation.get("recommendations", [])
        
        print(f"   Overall Score: {overall_score}/10")
        print(f"   Performance: {self._get_performance_label(overall_score)}")
        
        if recommendations:
            print("   Recommendations:")
            for rec in recommendations[:2]:  # Show top 2
                print(f"     • {rec}")
    
    def _get_performance_label(self, score: float) -> str:
        """Get performance label from score"""
        if score >= 8.0:
            return "Excellent ⭐"
        elif score >= 6.0:
            return "Good ✅"
        elif score >= 4.0:
            return "Adequate ⚠️"
        else:
            return "Needs Improvement ❌"
