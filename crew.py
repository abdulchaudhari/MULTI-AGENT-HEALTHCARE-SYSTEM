"""
Healthcare Multi-Agent System — Crew Orchestration
Manages the sequential execution of all healthcare agents
"""

import time
from crewai import Crew, Process
from agents import (
    create_symptom_analyzer,
    create_diagnostic_specialist,
    create_treatment_planner,
    create_medication_advisor,
    create_wellness_coach,
)
from tasks import (
    create_symptom_analysis_task,
    create_diagnostic_task,
    create_treatment_task,
    create_medication_task,
    create_wellness_task,
)


def on_task_finish(task_output):
    """Pause briefly between sequential agent tasks to respect TPM token bucket refill."""
    time.sleep(5)


def run_healthcare_crew(patient_input: str) -> dict:
    """
    Run the full healthcare analysis pipeline.
    
    Args:
        patient_input: String containing patient symptoms and information
        
    Returns:
        Dictionary with results from each agent
    """
    # Create agents
    symptom_analyzer = create_symptom_analyzer()
    diagnostic_specialist = create_diagnostic_specialist()
    treatment_planner = create_treatment_planner()
    medication_advisor = create_medication_advisor()
    wellness_coach = create_wellness_coach()

    # Create tasks (chained via context)
    symptom_task = create_symptom_analysis_task(symptom_analyzer, patient_input)
    diagnostic_task = create_diagnostic_task(diagnostic_specialist, symptom_task)
    treatment_task = create_treatment_task(treatment_planner, diagnostic_task)
    medication_task = create_medication_task(medication_advisor, treatment_task)
    wellness_task = create_wellness_task(wellness_coach, medication_task)

    # Assemble crew
    crew = Crew(
        agents=[
            symptom_analyzer,
            diagnostic_specialist,
            treatment_planner,
            medication_advisor,
            wellness_coach,
        ],
        tasks=[
            symptom_task,
            diagnostic_task,
            treatment_task,
            medication_task,
            wellness_task,
        ],
        process=Process.sequential,
        task_callback=on_task_finish,
        verbose=True,
    )

    # Execute
    result = crew.kickoff()

    # Collect individual task outputs
    task_outputs = {
        "symptom_analysis": symptom_task.output.raw if symptom_task.output else "",
        "diagnosis": diagnostic_task.output.raw if diagnostic_task.output else "",
        "treatment_plan": treatment_task.output.raw if treatment_task.output else "",
        "medication": medication_task.output.raw if medication_task.output else "",
        "wellness": wellness_task.output.raw if wellness_task.output else "",
        "final_report": result.raw if result else "",
    }

    return task_outputs
