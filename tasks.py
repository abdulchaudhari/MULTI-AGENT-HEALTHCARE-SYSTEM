"""
Healthcare Multi-Agent System — Task Definitions
5 sequential tasks forming the healthcare analysis pipeline
"""

from crewai import Task


def create_symptom_analysis_task(agent, patient_input):
    """Task 1: Analyze and categorize patient symptoms."""
    return Task(
        description=(
            f"Analyze the following patient information and symptoms:\n\n"
            f"{patient_input}\n\n"
            f"Perform a thorough symptom analysis:\n"
            f"1. List and categorize each symptom by body system\n"
            f"2. Assess the severity of each symptom (mild/moderate/severe)\n"
            f"3. Identify any symptom clusters or patterns\n"
            f"4. Flag any RED FLAG symptoms requiring urgent attention\n"
            f"5. Note the duration and progression of symptoms\n"
            f"6. Provide an overall urgency rating (1-10)\n\n"
            f"Format with clean markdown. Keep the analysis concise, structured, and under 250 words."
        ),
        expected_output=(
            "A structured symptom analysis report containing:\n"
            "- Categorized symptoms by body system\n"
            "- Severity assessment for each symptom\n"
            "- Identified patterns and clusters\n"
            "- Red flag alerts (if any)\n"
            "- Overall urgency rating with justification"
        ),
        agent=agent,
    )


def create_diagnostic_task(agent, symptom_task):
    """Task 2: Generate differential diagnoses from symptom analysis."""
    return Task(
        description=(
            "Based on the symptom analysis provided, generate a differential diagnosis:\n\n"
            "1. List the top 3 to 5 most likely diagnoses ranked by probability\n"
            "2. For each diagnosis, briefly explain supporting evidence\n"
            "3. Identify key distinguishing factors between conditions\n"
            "4. Note any additional tests or examinations needed to confirm\n"
            "5. Provide a confidence level for each diagnosis (high/medium/low)\n\n"
            "Format with clean markdown. Keep the report focused, structured, and under 250 words."
        ),
        expected_output=(
            "A differential diagnosis report containing:\n"
            "- Top ranked diagnoses with probability estimates\n"
            "- Supporting evidence for each diagnosis\n"
            "- Distinguishing factors between conditions\n"
            "- Recommended confirmatory tests\n"
            "- Confidence levels with reasoning"
        ),
        agent=agent,
        context=[symptom_task],
    )


def create_treatment_task(agent, diagnostic_task):
    """Task 3: Create evidence-based treatment plans."""
    return Task(
        description=(
            "Based on the differential diagnosis, create an evidence-based treatment plan:\n\n"
            "1. Immediate interventions (if urgently needed)\n"
            "2. Primary treatment strategy for the most likely diagnosis\n"
            "3. Alternative treatment approaches if primary diagnosis is ruled out\n"
            "4. Short-term management plan (1-4 weeks)\n"
            "5. Follow-up schedule and emergency care triggers\n\n"
            "Format with clean markdown. Keep the plan practical, structured, and under 250 words."
        ),
        expected_output=(
            "A structured treatment plan containing:\n"
            "- Immediate interventions (if needed)\n"
            "- Primary and alternative treatment strategies\n"
            "- Short-term management plans\n"
            "- Follow-up schedule\n"
            "- Emergency care triggers"
        ),
        agent=agent,
        context=[diagnostic_task],
    )


def create_medication_task(agent, treatment_task):
    """Task 4: Recommend medications with safety profiles."""
    return Task(
        description=(
            "Based on the treatment plan, recommend appropriate medications:\n\n"
            "1. Primary medications with specific drug names and dosage guidelines\n"
            "2. Administration route, frequency, and duration\n"
            "3. Common and serious side effects to watch for\n"
            "4. Key drug interactions and contraindications\n"
            "5. Over-the-counter alternatives where appropriate\n\n"
            "Format with clean markdown. Keep the medication guide clear, safe, and under 250 words."
        ),
        expected_output=(
            "A medication recommendation report containing:\n"
            "- Recommended medications with dosages\n"
            "- Administration guidelines\n"
            "- Side effects and interactions\n"
            "- Contraindications\n"
            "- Monitoring requirements\n"
            "- OTC alternatives where applicable"
        ),
        agent=agent,
        context=[treatment_task],
    )


def create_wellness_task(agent, medication_task):
    """Task 5: Create holistic wellness and prevention plan."""
    return Task(
        description=(
            "Create a holistic wellness and prevention plan to complement the medical treatment:\n\n"
            "1. Dietary recommendations specific to the condition\n"
            "2. Exercise and physical activity guidelines\n"
            "3. Sleep hygiene and stress management strategies\n"
            "4. Lifestyle modifications and preventive measures\n"
            "5. Warning signs that should prompt medical attention\n\n"
            "Format with clean markdown. Keep the advice actionable, motivating, and under 250 words."
        ),
        expected_output=(
            "A comprehensive wellness plan containing:\n"
            "- Dietary recommendations\n"
            "- Exercise guidance\n"
            "- Sleep and stress management strategies\n"
            "- Prevention measures\n"
            "- Warning signs reference"
        ),
        agent=agent,
        context=[medication_task],
    )
