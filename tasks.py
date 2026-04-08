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
            f"6. Provide an overall urgency rating (1-10)"
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
            "Based on the symptom analysis provided, generate a comprehensive "
            "differential diagnosis:\n\n"
            "1. List the top 5 most likely diagnoses ranked by probability\n"
            "2. For each diagnosis, explain the supporting evidence from the symptoms\n"
            "3. Identify key distinguishing factors between similar conditions\n"
            "4. Note any additional tests or examinations needed to confirm\n"
            "5. Consider both common and uncommon presentations\n"
            "6. Provide a confidence level for each diagnosis (high/medium/low)"
        ),
        expected_output=(
            "A differential diagnosis report containing:\n"
            "- Top 5 ranked diagnoses with probability estimates\n"
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
            "Based on the differential diagnosis, create a comprehensive treatment plan:\n\n"
            "1. Immediate interventions (if urgently needed)\n"
            "2. Primary treatment strategy for the most likely diagnosis\n"
            "3. Alternative treatment approaches if primary diagnosis is ruled out\n"
            "4. Short-term management plan (1-4 weeks)\n"
            "5. Long-term management strategy\n"
            "6. Follow-up schedule and monitoring parameters\n"
            "7. When to seek emergency care"
        ),
        expected_output=(
            "A structured treatment plan containing:\n"
            "- Immediate interventions (if needed)\n"
            "- Primary and alternative treatment strategies\n"
            "- Short-term and long-term management plans\n"
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
            "1. Primary medications with specific drug names\n"
            "2. Dosage guidelines (starting dose, maintenance dose, maximum dose)\n"
            "3. Administration route and frequency\n"
            "4. Duration of therapy\n"
            "5. Common and serious side effects to watch for\n"
            "6. Drug interactions to be aware of\n"
            "7. Contraindications and precautions\n"
            "8. Monitoring parameters (labs, vitals, etc.)\n"
            "9. Over-the-counter alternatives where appropriate"
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
            "3. Sleep hygiene recommendations\n"
            "4. Stress management and mental health strategies\n"
            "5. Lifestyle modifications for disease management\n"
            "6. Preventive measures to avoid recurrence\n"
            "7. Support resources (support groups, apps, educational materials)\n"
            "8. Weekly wellness routine template\n"
            "9. Warning signs that should prompt medical attention"
        ),
        expected_output=(
            "A comprehensive wellness plan containing:\n"
            "- Dietary plan with specific food recommendations\n"
            "- Exercise program with frequency and intensity\n"
            "- Sleep and stress management strategies\n"
            "- Lifestyle modifications checklist\n"
            "- Prevention measures\n"
            "- Weekly wellness routine\n"
            "- Warning signs reference card"
        ),
        agent=agent,
        context=[medication_task],
    )
