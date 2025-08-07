"""
Market Research System - Main Execution Script

This script orchestrates the 4-agent market research system:
1. Incumbents Agent - Analyzes competitors
2. Funding Agent - Researches funding landscape  
3. Growth Agent - Evaluates market growth
4. Decision Agent - Makes final recommendation

Usage: python3 main.py "product idea"
"""

import sys
import json
from core import MarketResearchSystem


def main():
    if len(sys.argv) != 2:      # correct user if they do not provide a product idea
        print("Usage: python main.py \"your product idea\"")
        print("\nExample:")
        print("python main.py \"AI-powered fitness app\"")
        sys.exit(1)
    
    product_idea = sys.argv[1]
    
    # Initialize system
    system = MarketResearchSystem()
    
    try:
        # Run research
        results = system.research_product_idea(product_idea)
        
        # Save results to file
        output_file = f"research_results_{product_idea.replace(' ', '_')[:20]}.json"
        with open(output_file, 'w') as f:
            json.dump(results, f, indent=2)
        
        print(f"\n Results saved to: {output_file}")
        
    except Exception as e:
        print(f"\n Error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
