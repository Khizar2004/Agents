from typing import Dict, List, Any
import json


class AgentEvaluator:
    def __init__(self):
        self.evaluation_criteria = {
            "incumbents": {
                "completeness": "Does the analysis cover main competitors?",
                "specificity": "Are specific companies and features mentioned?",
                "insight_quality": "Does it provide actionable insights?"
            },
            "funding": {
                "relevance": "Is the funding analysis relevant to the product space?",
                "recency": "Does it mention recent funding trends?",
                "investor_perspective": "Does it consider investor viewpoint?"
            },
            "growth": {
                "market_sizing": "Does it address market size?",
                "growth_trends": "Are growth trends discussed?",
                "revenue_potential": "Is revenue opportunity assessed?"
            },
            "decision": {
                "synthesis": "Does it properly combine all inputs?",
                "clarity": "Is the recommendation clear?",
                "reasoning": "Are the reasons well-justified?"
            }
        }
    
    def evaluate_agent_response(self, agent_name: str, response: Dict[str, Any]) -> Dict[str, Any]:
        """Evaluate a single agent's response"""
        agent_key = agent_name.lower()
        
        if agent_key not in self.evaluation_criteria:
            return {"error": f"No evaluation criteria for agent: {agent_name}"}
        
        analysis = response.get("analysis", "") or response.get("reasoning", "")
        
        scores = {}
        criteria = self.evaluation_criteria[agent_key]
        
        for criterion, description in criteria.items():
            scores[criterion] = self._score_criterion(analysis, criterion, agent_key)
        
        overall_score = sum(scores.values()) / len(scores)
        
        return {
            "agent": agent_name,
            "individual_scores": scores,
            "overall_score": round(overall_score, 2),
            "evaluation_summary": self._generate_summary(scores, overall_score),
            "response_length": len(analysis),
            "confidence": response.get("confidence", 0.0)
        }
    
    def _score_criterion(self, analysis: str, criterion: str, agent_type: str) -> float:
        """Score a specific criterion (simplified heuristic approach)"""
        analysis_lower = analysis.lower()
        
        # Define keyword sets for each criterion
        keyword_sets = {
            "completeness": ["competitor", "company", "market", "player", "incumbent"],
            "specificity": ["feature", "product", "service", "$", "million", "billion"],
            "insight_quality": ["opportunity", "advantage", "weakness", "trend", "strategy"],
            "relevance": ["funding", "investment", "venture", "capital", "round"],
            "recency": ["recent", "2023", "2024", "latest", "current"],
            "investor_perspective": ["investor", "valuation", "return", "portfolio", "vc"],
            "market_sizing": ["market", "size", "billion", "million", "tam", "revenue"],
            "growth_trends": ["growth", "increase", "trend", "forecast", "projection"],
            "revenue_potential": ["revenue", "profit", "monetization", "pricing", "income"],
            "synthesis": ["based on", "considering", "overall", "combination", "together"],
            "clarity": ["recommend", "good", "poor", "neutral", "opportunity"],
            "reasoning": ["because", "due to", "reason", "evidence", "analysis"]
        }
        
        if criterion in keyword_sets:
            keywords = keyword_sets[criterion]
            keyword_count = sum(1 for keyword in keywords if keyword in analysis_lower)
            
            # Base score on keyword presence and response length
            keyword_score = min(keyword_count / 3, 1.0) * 6  # Max 6 points from keywords
            length_score = min(len(analysis) / 200, 1.0) * 4  # Max 4 points from length
            
            return min(10.0, keyword_score + length_score)
        
        # Default scoring
        return 5.0 if len(analysis) > 50 else 2.0
    
    def _generate_summary(self, scores: Dict[str, float], overall_score: float) -> str:
        """Generate evaluation summary"""
        if overall_score >= 8.0:
            return "Excellent response with strong analysis across all criteria"
        elif overall_score >= 6.0:
            return "Good response with solid insights, minor improvements possible"
        elif overall_score >= 4.0:
            return "Adequate response but lacks depth in some areas"
        else:
            return "Poor response, needs significant improvement"
    
    def evaluate_full_research(self, research_results: Dict[str, Any]) -> Dict[str, Any]:
        """Evaluate the complete research from all agents"""
        agent_evaluations = {}
        
        for agent_name, result in research_results.items():
            if agent_name != "summary":
                agent_evaluations[agent_name] = self.evaluate_agent_response(agent_name, result)
        
        # Calculate system-wide metrics
        overall_scores = [eval_data["overall_score"] for eval_data in agent_evaluations.values()]
        system_score = sum(overall_scores) / len(overall_scores) if overall_scores else 0
        
        return {
            "individual_evaluations": agent_evaluations,
            "system_performance": {
                "overall_score": round(system_score, 2),
                "agent_count": len(agent_evaluations),
                "score_distribution": {
                    "excellent": len([s for s in overall_scores if s >= 8]),
                    "good": len([s for s in overall_scores if 6 <= s < 8]),
                    "adequate": len([s for s in overall_scores if 4 <= s < 6]),
                    "poor": len([s for s in overall_scores if s < 4])
                }
            },
            "recommendations": self._get_system_recommendations(agent_evaluations, system_score)
        }
    
    def _get_system_recommendations(self, evaluations: Dict, system_score: float) -> List[str]:
        """Generate recommendations for system improvement"""
        recommendations = []
        
        if system_score < 6.0:
            recommendations.append("Consider adjusting agent prompts for better specificity")
            recommendations.append("Add more domain-specific keywords to improve analysis depth")
        
        # Check individual agent performance
        for agent, eval_data in evaluations.items():
            if eval_data["overall_score"] < 5.0:
                recommendations.append(f"Agent {agent} needs improvement in analysis quality")
        
        if not recommendations:
            recommendations.append("System performing well - continue current approach")
        
        return recommendations
