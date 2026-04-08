# 🧬 MedCrew AI — Healthcare Multi-Agent System

> **5 AI Specialists. One Patient. One Comprehensive Report.**

A multi-agent healthcare analysis system powered by **CrewAI** for agent orchestration and **Groq API** (LLaMA 3 70B) for ultra-fast inference — wrapped in a bold **Neo Brutalism** UI.

Enter your symptoms and watch a crew of 5 specialized AI agents collaboratively analyze, diagnose, plan treatment, recommend medications, and prescribe a wellness strategy — all in under 60 seconds.

---

## 🎨 Neo Brutalism UI

<p align="center">
  <img src="https://img.shields.io/badge/CrewAI-Agents-4ECDC4?style=for-the-badge&labelColor=1A1A1A" />
  <img src="https://img.shields.io/badge/Groq-LLaMA%203%2070B-FF8C42?style=for-the-badge&labelColor=1A1A1A" />
  <img src="https://img.shields.io/badge/Flask-Backend-FFE66D?style=for-the-badge&labelColor=1A1A1A" />
  <img src="https://img.shields.io/badge/UI-Neo%20Brutalism-FF69B4?style=for-the-badge&labelColor=1A1A1A" />
</p>

---

## 🤖 The Agent Crew

| # | Agent | Role | What It Does |
|:-:|-------|------|--------------|
| 1 | 🔬 **Symptom Analyzer** | Medical Symptom Analyst | Parses symptoms, categorizes by body system, assesses severity, flags red flags |
| 2 | 🩺 **Diagnostic Specialist** | Clinical Diagnostician | Generates top 5 differential diagnoses ranked by probability |
| 3 | 💊 **Treatment Planner** | Treatment Strategy Expert | Creates evidence-based treatment plans (immediate + long-term) |
| 4 | 💉 **Medication Advisor** | Clinical Pharmacologist | Recommends medications with dosages, interactions & side effects |
| 5 | 🧘 **Wellness Coach** | Patient Wellness Advisor | Builds holistic wellness plans: diet, exercise, stress management |

All agents execute **sequentially** — each builds on the previous agent's analysis for a comprehensive report.

---

## 🏗️ Architecture

```
Patient Input → Flask API → CrewAI Orchestrator
                                    ↓
                    ┌───────────────────────────────┐
                    │  🔬 Symptom Analyzer          │
                    │         ↓                     │
                    │  🩺 Diagnostic Specialist     │
                    │         ↓                     │
                    │  💊 Treatment Planner         │
                    │         ↓                     │
                    │  💉 Medication Advisor        │
                    │         ↓                     │
                    │  🧘 Wellness Coach            │
                    └───────────────────────────────┘
                                    ↓
                        Comprehensive Report → UI
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- A free [Groq API key](https://console.groq.com)

### Installation

```bash
# Clone the repo
git clone https://github.com/yourusername/MedCrew-AI.git
cd MedCrew-AI

# Install dependencies
pip install -r requirements.txt

# Set up your API key
cp .env.example .env
# Edit .env and add your Groq API key
```

### Run

```bash
python app.py
```

Open **http://localhost:5000** in your browser.

---

## 📁 Project Structure

```
MedCrew-AI/
├── app.py                 # Flask server & API routes
├── agents.py              # 5 CrewAI agent definitions
├── tasks.py               # 5 sequential task definitions
├── crew.py                # Crew orchestration logic
├── requirements.txt       # Python dependencies
├── .env.example           # Environment variable template
├── templates/
│   └── index.html         # Neo Brutalism UI
└── static/
    ├── css/
    │   └── style.css      # Neo Brutalism design system
    └── js/
        └── app.js         # Frontend logic & animations
```

---

## 🎨 Design: Neo Brutalism

The UI follows the **Neo Brutalism** design philosophy:

| Element | Implementation |
|---------|----------------|
| **Borders** | 3–4px solid black on all components |
| **Shadows** | Hard offset `6px 6px 0px #000` — no blur |
| **Colors** | Vibrant palette: Red, Teal, Yellow, Mint, Plum |
| **Typography** | Space Grotesk — bold, geometric sans-serif |
| **Border Radius** | 0px — sharp, boxy aesthetic |
| **Hover States** | Shadow shifts on interaction |
| **Animations** | Slide-up entrances, pulse indicators |

---

## ⚙️ Tech Stack

| Layer | Technology |
|-------|-----------|
| **Agent Framework** | [CrewAI](https://crewai.com) |
| **LLM Provider** | [Groq](https://groq.com) — LLaMA 3 70B |
| **Backend** | Flask (Python) |
| **Frontend** | Vanilla HTML/CSS/JS |
| **Design** | Neo Brutalism |

---

## ⚕️ Disclaimer

> **This is an educational/demonstration project.** It does NOT provide real medical advice, diagnosis, or treatment. Always consult a qualified healthcare professional for medical concerns. Never disregard professional medical advice because of AI-generated content.

---

## 📄 License

MIT License — feel free to use, modify, and distribute.

---

<p align="center">
  Built with ❤️ using <strong>CrewAI</strong> + <strong>Groq</strong> + <strong>Flask</strong>
</p>
