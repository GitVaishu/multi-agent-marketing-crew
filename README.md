# Multi-Agent Marketing Crew

A CrewAI-based multi-agent system that automates marketing content creation using specialized AI agents.

## 🚀 Features

- **Head of Marketing Agent**: Conducts market research and strategy
- **Content Writer Agent**: Creates blog posts and content
- **SEO Specialist Agent**: Optimizes content for search engines
- **Social Media Agent**: Generates platform-specific content

## 🛠️ Setup

1. **Install dependencies**:
   ```bash
   pip install crewai python-dotenv
   
Get API Keys:

Get Groq API key from: https://console.groq.com

Optional: Serper API key for web search

Create .env file:
GROQ_API_KEY=your_groq_api_key_here
SERPER_API_KEY=your_serper_key_here

Run the project:
python main.py

📁 Project Structure
├── main.py          # Main execution script
├── crew.py          # Agent and crew definitions
├── agents.yaml      # Agent configurations
├── tasks.yaml       # Task descriptions
├── output/          # Generated content files
└── README.md        # This file

🤖 Agents
Head of Marketing: Leads strategy and research

Blog Content Writer: Creates written content

SEO Specialist: Optimizes for search engines

Social Media Creator: Generates platform-specific content

📋 Usage
The system automatically generates:

Market research reports

Blog posts

Social media content

SEO-optimized articles