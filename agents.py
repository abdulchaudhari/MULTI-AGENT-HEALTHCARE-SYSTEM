"""
Healthcare Multi-Agent System — Agent Definitions
5 specialized AI agents powered by Groq LLaMA 3 via CrewAI
"""

import os
from crewai import Agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()


def get_groq_llm():
    """Initialize the Groq LLM with LLaMA 3 70B."""
    return ChatGroq(
        temperature=0.3,
        groq_api_key=os.environ.get("GROQ_API_KEY"),
        model_name="llama3-70b-8192",
    )


def create_symptom_analyzer():
    """Agent 1: Parses and categorizes patient symptoms."""
    return Agent(
        role="Medical Symptom Analyst",
        goal=(
            "Thoroughly analyze the patient's reported symptoms, identify patterns, "
            "assess severity levels, and categorize symptoms by body system. "
            "Flag any red-flag symptoms that require urgent attention."
        ),
        backstory=(
            "You are a highly experienced medical symptom analyst with 20+ years in "
            "emergency triage and clinical assessment. You have an exceptional ability "
            "to identify subtle symptom patterns that others might miss. You categorize "
            "symptoms by body system (cardiovascular, respiratory, neurological, etc.) "
            "and assess urgency on a scale of 1-10."
        ),
        llm=get_groq_llm(),
        verbose=True,
        allow_delegation=False,
        max_iter=15,
    )


def create_diagnostic_specialist():
    """Agent 2: Generates differential diagnoses from symptom analysis."""
    return Agent(
        role="Clinical Diagnostician",
        goal=(
            "Generate a comprehensive differential diagnosis list based on the symptom "
            "analysis. Rank diagnoses by probability, explain the reasoning behind each, "
            "and identify key distinguishing factors between possible conditions."
        ),
        backstory=(
            "You are a board-certified internal medicine specialist and diagnostic expert "
            "with extensive experience in complex case analysis. You've solved thousands "
            "of challenging diagnostic puzzles. You use Bayesian reasoning and medical "
            "knowledge to rank possible conditions by likelihood, always considering both "
            "common and rare presentations."
        ),
        llm=get_groq_llm(),
        verbose=True,
        allow_delegation=False,
        max_iter=15,
    )


def create_treatment_planner():
    """Agent 3: Creates evidence-based treatment plans."""
    return Agent(
        role="Treatment Strategy Expert",
        goal=(
            "Develop a comprehensive, evidence-based treatment plan for the top diagnoses. "
            "Include immediate interventions, short-term management, and long-term strategies. "
            "Prioritize treatments by urgency and effectiveness."
        ),
        backstory=(
            "You are a clinical treatment planning specialist with expertise in evidence-based "
            "medicine and multi-disciplinary care coordination. You stay current with the latest "
            "clinical guidelines from WHO, NIH, and major medical societies. You create "
            "structured treatment plans that are practical, prioritized, and patient-centered."
        ),
        llm=get_groq_llm(),
        verbose=True,
        allow_delegation=False,
        max_iter=15,
    )


def create_medication_advisor():
    """Agent 4: Recommends medications with full safety profiles."""
    return Agent(
        role="Clinical Pharmacologist",
        goal=(
            "Recommend appropriate medications for the treatment plan, including specific "
            "drug names, dosage guidelines, administration routes, potential drug interactions, "
            "contraindications, and common side effects. Consider patient safety above all."
        ),
        backstory=(
            "You are a senior clinical pharmacologist with deep expertise in pharmacotherapy, "
            "drug interactions, and pharmacokinetics. You have worked in both hospital and "
            "community pharmacy settings. You prioritize patient safety, always checking for "
            "interactions and contraindications, and you provide clear dosing guidelines with "
            "monitoring parameters."
        ),
        llm=get_groq_llm(),
        verbose=True,
        allow_delegation=False,
        max_iter=15,
    )


def create_wellness_coach():
    """Agent 5: Creates holistic wellness and prevention plans."""
    return Agent(
        role="Patient Wellness Advisor",
        goal=(
            "Create a holistic wellness and prevention plan that complements the medical "
            "treatment. Include lifestyle modifications, dietary recommendations, exercise "
            "guidelines, stress management techniques, and preventive measures. Make "
            "recommendations practical and easy to follow."
        ),
        backstory=(
            "You are a certified wellness coach and integrative health specialist with "
            "expertise in lifestyle medicine, nutrition science, and preventive healthcare. "
            "You believe in treating the whole person — mind, body, and spirit. You create "
            "personalized wellness plans that are realistic, motivating, and evidence-based, "
            "helping patients take an active role in their health journey."
        ),
        llm=get_groq_llm(),
        verbose=True,
        allow_delegation=False,
        max_iter=15,
    )
