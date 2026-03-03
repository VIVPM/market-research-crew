# 📈 Market Research Crew AI

An autonomous AI-powered market research and business analysis system built with [CrewAI](https://crewai.com) and deployed as a Streamlit web app. Enter your product idea and let a crew of specialized AI agents handle market sizing, competitive intelligence, customer insights, product strategy, and a full business report — all in one run.

---

## 🌐 Live Demo

> Deploy on [Streamlit Cloud](https://streamlit.io/cloud) by connecting this repo and running `app.py`.

---

## ✨ Features

- 📊 **Market Research** — TAM/SAM/SOM sizing, industry trends, regulatory landscape & technology readiness
- 🕵️ **Competitive Intelligence** — Competitor profiling, comparison matrix, positioning map & gap analysis
- 👥 **Customer Insights** — Personas, pain-point matrix, customer journey maps & acquisition channels
- 🗺️ **Product Strategy** — MVP feature prioritization, differentiation strategy & 12-month roadmap
- 💼 **Business Analysis** — Pricing strategy, revenue model, risk matrix & Go/No-Go recommendation
- 📄 **Report Download** — Full business analysis report exported as `report.md` with one click

---

## 🤖 Agents

| Agent | Role |
|---|---|
| **Market Research Specialist** | Market sizing, industry trends, regulatory & technology landscape |
| **Competitive Intelligence Analyst** | Competitor mapping, feature comparison matrix, gap discovery |
| **Customer Insights Researcher** | Persona creation, pain-point analysis, customer journey mapping |
| **Product Strategy Advisor** | MVP prioritization, differentiation strategy, product roadmap |
| **Business Analyst & Report Synthesizer** | Pricing, revenue projections, risk analysis & final recommendation |

> All agents are powered by **Gemini** models via `crewai[google-genai]` and equipped with web search + scraping tools.

---

## 🛠️ Agent Tools

Every agent in the crew has access to the full research toolkit:

| Tool | Purpose |
|---|---|
| `SerperDevTool` | Real-time Google web search for market data & news |
| `ScrapeWebsiteTool` | Scrape competitor websites & product pages |
| `SeleniumScrapingTool` | Dynamic content scraping for JS-rendered pages |

---

## 📋 Tasks Pipeline (Sequential)

```
Market Research → Competitive Intelligence → Customer Insights
    → Product Strategy → Business Analysis & Final Report
```

Each task feeds its findings as context into the next, building a progressively deeper picture of the opportunity.

---

## 📊 Evaluation Results

![Market Research Crew Testing Results](Screenshot%202026-03-03%20192049.png)

During testing, the Market Research Crew demonstrated exceptionally strong performance, achieving an impressive **overall average score of 9.6/10** with an execution time of 476 seconds. The specialized agents consistently delivered highly accurate and insightful results across all their respective tasks:

- **Customer Insights Researcher** and **Product Strategy Advisor** tied for the highest average score of **9.7**, indicating deep understanding of the customer base and excellent prioritization of actionable MVP features.
- **Market Research Specialist** and **Business Analyst and Report Synthesizer** also performed incredibly well with an average score of **9.5**, successfully extracting relevant macro trends and compiling findings into a cohesive final business report.
- **Competitive Intelligence Analyst** achieved a strong **9.4**, thoroughly mapping the competitive landscape to uncover viable market gaps.

This highlights the crew's robust capability to execute comprehensive, data-driven market research and strategic planning autonomously, yielding production-ready business analysis material.

---

## 📁 Project Structure

```
market_research_crew/
├── app.py                          # Streamlit UI (entry point)
├── reports/
│   └── report.md                   # Final business analysis report (auto-generated)
├── knowledge/                      # Optional knowledge base files
├── src/
│   └── market_research_crew/
│       ├── crew.py                 # CrewAI agents, tasks & crew definition
│       ├── main.py                 # CLI entry point (crewai run)
│       ├── config/
│       │   ├── agents.yaml         # Agent roles, goals & backstories
│       │   └── tasks.yaml          # Task descriptions & expected outputs
│       └── tools/                  # Custom tool definitions
└── pyproject.toml
```

---

## 🛠️ Setup & Local Run

### 1. Clone & install

```bash
git clone https://github.com/VIVPM/market_research_crew.git
cd market_research_crew
pip install uv
crewai install
```

### 2. Set up `.env`

```env
GEMINI_API_KEY=your_gemini_api_key
SERPER_API_KEY=your_serper_api_key
```

### 3. Run locally

```bash
streamlit run app.py
```

Or run the crew via CLI (requires hard-coded input in `main.py`):

```bash
crewai run
```

---

## ☁️ Streamlit Cloud Deployment

1. Push this repo to GitHub
2. Go to [Streamlit Cloud](https://streamlit.io/cloud) → New App → select `app.py`
3. No secrets needed — users enter API keys via the sidebar at runtime

> API keys are entered by the user in the sidebar at runtime (not stored anywhere).

---

## 🔑 API Keys Required

Both keys are entered directly in the app sidebar — no Streamlit secrets configuration needed.

| Key | Where to get |
|---|---|
| **Gemini API Key** | [aistudio.google.com/apikey](https://aistudio.google.com/apikey) |
| **Serper API Key** | [serper.dev](https://serper.dev/) |

---

## 📦 Dependencies

```
crewai
crewai-tools
crewai[google-genai]
streamlit
python-dotenv
selenium
```

> This project uses [UV](https://docs.astral.sh/uv/) for fast, reliable dependency management.

---

## 📄 License

MIT License — see [LICENSE](LICENSE)
