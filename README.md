# Market Research System

A 4-agent system for comprehensive product idea market research. Built without LangChain or LlamaIndex, using direct OpenAI API calls for simplicity and transparency.

## 🏗️ System Architecture

```
/Agents
├── main.py              # Main execution script
├── config.py            # Configuration settings
├── requirements.txt     # Dependencies
├── .env                # Environment variables (API keys)
├── /agents             # Agent implementations
│   ├── __init__.py
│   ├── base_agent.py   # Base agent class
│   ├── incumbents_agent.py   # Competitor analysis
│   ├── funding_agent.py      # Funding research
│   ├── growth_agent.py       # Market growth analysis
│   └── decision_agent.py     # Final recommendation
├── /core               # Core system components  
│   ├── __init__.py
│   ├── system.py       # Main system orchestrator
│   └── evaluator.py    # Agent evaluation system
└── /results            # Generated research reports (JSON)
```

## 🤖 The 4 Agents

### 1. **IncumbentsAgent**
- **Purpose**: Competitive landscape analysis
- **Focus**: Existing competitors, features, market positioning, strengths/weaknesses
- **Output**: Detailed competitor analysis with actionable insights

### 2. **FundingAgent** 
- **Purpose**: Investment and funding research
- **Focus**: Recent funding rounds, investor sentiment, valuation trends, VC attractiveness
- **Output**: Funding landscape analysis with investor perspective

### 3. **GrowthAgent**
- **Purpose**: Market growth and revenue analysis  
- **Focus**: Market size, growth rates, revenue potential, economic factors
- **Output**: Quantitative growth assessment with market dynamics

### 4. **DecisionAgent**
- **Purpose**: Synthesis and final recommendation
- **Focus**: Combines all research to make investment recommendation
- **Output**: Final decision (Good/Neutral/Poor) with detailed reasoning

## 📊 Built-in Evaluation System

The system includes comprehensive evaluation across multiple criteria:

- **Completeness**: Coverage of key research areas
- **Specificity**: Concrete details vs generic statements  
- **Insight Quality**: Depth of analysis and actionable insights
- **Synthesis**: How well the decision agent combines research
- **Overall Performance**: System-wide scoring and recommendations

## 🚀 Quick Start

1. **Setup Environment:**
   ```bash
   # Clone/download the project
   cd Agents
   
   # Install dependencies
   pip install -r requirements.txt
   
   # Add your OpenAI API key to .env
   echo "OPENAI_API_KEY=your_key_here" > .env
   ```

2. **Run Market Research:**
   ```bash
   python main.py "your product idea"
   ```

3. **Examples:**
   ```bash
   python main.py "AI-powered fitness app"
   python main.py "blockchain-based voting system"  
   python main.py "sustainable food delivery service"
   ```

## 📈 Sample Output

```
🔍 Researching product idea: AI-powered fitness app
============================================================

1️⃣  Analyzing Competitors...
   Analysis: Main competitors include Fitbit, MyFitnessPal, Peloton...
   Confidence: 0.9

2️⃣  Researching Funding Landscape...
   Analysis: Recent funding rounds show strong investor interest...
   Confidence: 0.9

3️⃣  Evaluating Growth Potential...  
   Analysis: Market expected to reach $15.96B by 2027...
   Confidence: 0.9

4️⃣  Making Final Recommendation...
   🟢 Recommendation: Good
   Reasoning: Strong market demand, favorable funding environment...
   Confidence: 0.9

📊 System Evaluation
   Overall Score: 8.0/10
   Performance: Excellent ⭐
```

## 🔧 Configuration

Edit `config.py` to customize:
- OpenAI model selection
- Agent timeout settings  
- Evaluation thresholds
- Response length limits

## 📁 Output Files

Each research session generates:
- **JSON Report**: Complete research data with evaluation scores
- **Structured Results**: Agent findings, recommendations, confidence scores
- **Performance Metrics**: System evaluation and improvement suggestions

## 🎯 Assignment Requirements Met

✅ **4 specialized agents** (Incumbents, Funding, Growth, Decision)  
✅ **3 research areas** (competitors, funding, growth)  
✅ **Final judgment** with reasoning on product viability  
✅ **No LangChain/LlamaIndex** (pure OpenAI API)  
✅ **Solid evaluation system** with scoring and metrics  
✅ **Clean, simple code** under 500 lines total  
✅ **Working end-to-end** with real AI analysis

## 📋 Dependencies

- `openai>=1.0.0` - OpenAI API client
- `python-dotenv>=1.0.0` - Environment variable management

## 🏃‍♂️ Development

The modular structure makes it easy to:
- Add new agent types
- Modify evaluation criteria  
- Extend research capabilities
- Customize output formats

Each agent is self-contained and follows the same interface pattern for easy maintenance and testing.
