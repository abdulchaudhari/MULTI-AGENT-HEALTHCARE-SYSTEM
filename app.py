"""
Healthcare Multi-Agent System — Flask Application
Serves the Neo Brutalism UI and handles API requests
"""

import os
import sys
import traceback
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

# Ensure UTF-8 output encoding on Windows console
if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if sys.stderr and hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

load_dotenv()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static"),
)


@app.route("/")
def index():
    """Serve the main UI page."""
    return render_template("index.html")


@app.route("/api/analyze", methods=["POST"])
def analyze():
    """Run the healthcare crew analysis pipeline."""
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "No data provided"}), 400

        # Build patient input string from form data
        symptoms = data.get("symptoms", "")
        age = data.get("age", "Not specified")
        gender = data.get("gender", "Not specified")
        medical_history = data.get("medical_history", "None reported")
        current_medications = data.get("current_medications", "None")
        allergies = data.get("allergies", "None known")

        if not symptoms.strip():
            return jsonify({"error": "Please describe your symptoms"}), 400

        patient_input = (
            f"Patient Information:\n"
            f"- Age: {age}\n"
            f"- Gender: {gender}\n"
            f"- Medical History: {medical_history}\n"
            f"- Current Medications: {current_medications}\n"
            f"- Known Allergies: {allergies}\n\n"
            f"Presenting Symptoms:\n{symptoms}"
        )

        # Import here to avoid circular imports and allow startup without deps
        from crew import run_healthcare_crew

        results = run_healthcare_crew(patient_input)

        return jsonify({
            "success": True,
            "results": results,
        })

    except Exception as e:
        print(f"Error during analysis: {e}")
        traceback.print_exc()
        return jsonify({
            "error": f"Analysis failed: {str(e)}",
            "details": traceback.format_exc(),
        }), 500


@app.route("/api/health", methods=["GET"])
def health_check():
    """Health check endpoint."""
    groq_key = os.environ.get("GROQ_API_KEY", "")
    return jsonify({
        "status": "healthy",
        "groq_configured": bool(groq_key and groq_key != "your_groq_api_key_here"),
    })


if __name__ == "__main__":
    # Check for API key
    groq_key = os.environ.get("GROQ_API_KEY", "")
    if not groq_key or groq_key == "your_groq_api_key_here":
        print("\n" + "=" * 60)
        print("⚠️  WARNING: GROQ_API_KEY not configured!")
        print("=" * 60)
        print("1. Get your free API key at: https://console.groq.com")
        print("2. Create a .env file with: GROQ_API_KEY=your_key_here")
        print("=" * 60 + "\n")

    app.run(debug=True, host="0.0.0.0", port=5000)
