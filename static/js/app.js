/**
 * MedCrew AI — Frontend Logic
 * Handles form submission, agent pipeline animation, and results display
 */

// ── STATE ───────────────────────────────────────────────────
const AGENTS = [
    { id: 1, key: 'symptom_analysis', name: 'Symptom Analyzer' },
    { id: 2, key: 'diagnosis', name: 'Diagnostic Specialist' },
    { id: 3, key: 'treatment_plan', name: 'Treatment Planner' },
    { id: 4, key: 'medication', name: 'Medication Advisor' },
    { id: 5, key: 'wellness', name: 'Wellness Coach' },
];

let isAnalyzing = false;

// ── DOM READY ───────────────────────────────────────────────
document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('patient-form');
    form.addEventListener('submit', handleSubmit);

    // Health check
    checkHealth();
});

// ── HEALTH CHECK ────────────────────────────────────────────
async function checkHealth() {
    try {
        const res = await fetch('/api/health');
        const data = await res.json();
        if (!data.groq_configured) {
            console.warn('⚠️ Groq API key not configured. Set GROQ_API_KEY in .env file.');
        }
    } catch (e) {
        console.error('Health check failed:', e);
    }
}

// ── FORM SUBMISSION ─────────────────────────────────────────
async function handleSubmit(e) {
    e.preventDefault();

    if (isAnalyzing) return;
    isAnalyzing = true;

    const formData = {
        symptoms: document.getElementById('symptoms').value.trim(),
        age: document.getElementById('age').value || 'Not specified',
        gender: document.getElementById('gender').value || 'Not specified',
        medical_history: document.getElementById('medical_history').value.trim() || 'None reported',
        current_medications: document.getElementById('current_medications').value.trim() || 'None',
        allergies: document.getElementById('allergies').value.trim() || 'None known',
    };

    if (!formData.symptoms) {
        alert('Please describe your symptoms.');
        isAnalyzing = false;
        return;
    }

    // Show pipeline, hide results/errors
    showSection('pipeline-section');
    hideSection('results-section');
    hideSection('error-section');

    // Toggle button
    toggleButton(true);

    // Start pipeline animation
    startPipelineAnimation();

    try {
        const response = await fetch('/api/analyze', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(formData),
        });

        const data = await response.json();

        if (!response.ok || data.error) {
            throw new Error(data.error || 'Analysis failed');
        }

        // Complete pipeline
        completePipelineAnimation();

        // Show results after a brief delay
        setTimeout(() => {
            displayResults(data.results);
        }, 800);

    } catch (error) {
        console.error('Analysis error:', error);
        showError(error.message);
        resetPipeline();
    } finally {
        toggleButton(false);
        isAnalyzing = false;
    }
}

// ── PIPELINE ANIMATION ─────────────────────────────────────
function startPipelineAnimation() {
    const progressFill = document.getElementById('progress-fill');
    const progressText = document.getElementById('progress-text');

    // Reset all agents
    AGENTS.forEach((agent) => {
        const el = document.getElementById(`agent-${agent.id}`);
        el.classList.remove('pipeline__agent--active', 'pipeline__agent--done');
        const dot = el.querySelector('.status-dot');
        dot.className = 'status-dot status-dot--idle';
        el.querySelector('.status-text').textContent = 'Waiting';
    });

    progressFill.style.width = '0%';

    // Simulate sequential activation
    let currentAgent = 0;
    const interval = setInterval(() => {
        if (currentAgent >= AGENTS.length) {
            clearInterval(interval);
            return;
        }

        // Mark previous as done
        if (currentAgent > 0) {
            const prev = document.getElementById(`agent-${AGENTS[currentAgent - 1].id}`);
            prev.classList.remove('pipeline__agent--active');
            prev.classList.add('pipeline__agent--done');
            prev.querySelector('.status-dot').className = 'status-dot status-dot--done';
            prev.querySelector('.status-text').textContent = 'Done';
        }

        // Activate current
        const el = document.getElementById(`agent-${AGENTS[currentAgent].id}`);
        el.classList.add('pipeline__agent--active');
        el.querySelector('.status-dot').className = 'status-dot status-dot--active';
        el.querySelector('.status-text').textContent = 'Working';

        // Update progress
        const progress = ((currentAgent + 1) / AGENTS.length) * 90; // Leave 10% for completion
        progressFill.style.width = `${progress}%`;
        progressText.textContent = `Agent ${currentAgent + 1}/${AGENTS.length}: ${AGENTS[currentAgent].name} is analyzing...`;

        currentAgent++;
    }, 8000); // ~8s per agent simulation

    // Store interval ID for cleanup
    window._pipelineInterval = interval;
}

function completePipelineAnimation() {
    // Clear the simulation interval
    if (window._pipelineInterval) {
        clearInterval(window._pipelineInterval);
    }

    // Mark all agents as done
    AGENTS.forEach((agent) => {
        const el = document.getElementById(`agent-${agent.id}`);
        el.classList.remove('pipeline__agent--active');
        el.classList.add('pipeline__agent--done');
        el.querySelector('.status-dot').className = 'status-dot status-dot--done';
        el.querySelector('.status-text').textContent = 'Done';
    });

    // Complete progress
    document.getElementById('progress-fill').style.width = '100%';
    document.getElementById('progress-text').textContent = '✅ All agents completed! Preparing results...';
}

function resetPipeline() {
    if (window._pipelineInterval) {
        clearInterval(window._pipelineInterval);
    }

    AGENTS.forEach((agent) => {
        const el = document.getElementById(`agent-${agent.id}`);
        el.classList.remove('pipeline__agent--active', 'pipeline__agent--done');
        el.querySelector('.status-dot').className = 'status-dot status-dot--idle';
        el.querySelector('.status-text').textContent = 'Waiting';
    });

    document.getElementById('progress-fill').style.width = '0%';
    document.getElementById('progress-text').textContent = 'Initializing agents...';
}

// ── RESULTS DISPLAY ─────────────────────────────────────────
function displayResults(results) {
    hideSection('pipeline-section');
    showSection('results-section');

    const sections = [
        { key: 'symptom_analysis', data: results.symptom_analysis },
        { key: 'diagnosis', data: results.diagnosis },
        { key: 'treatment_plan', data: results.treatment_plan },
        { key: 'medication', data: results.medication },
        { key: 'wellness', data: results.wellness },
    ];

    sections.forEach((section, index) => {
        const contentEl = document.getElementById(`content-${section.key}`);
        const bodyEl = document.getElementById(`body-${section.key}`);
        const chevronEl = document.getElementById(`chevron-${section.key}`);

        const text = section.data || 'No data available for this section.';
        contentEl.innerHTML = formatMarkdown(text);

        // Auto-expand first result, collapse others
        if (index === 0) {
            bodyEl.classList.add('result-card__body--open');
            chevronEl.classList.add('result-card__chevron--open');
        } else {
            bodyEl.classList.remove('result-card__body--open');
            chevronEl.classList.remove('result-card__chevron--open');
        }
    });

    // Scroll to results
    document.getElementById('results-section').scrollIntoView({ behavior: 'smooth', block: 'start' });
}

// ── ACCORDION TOGGLE ────────────────────────────────────────
function toggleResult(key) {
    const bodyEl = document.getElementById(`body-${key}`);
    const chevronEl = document.getElementById(`chevron-${key}`);

    bodyEl.classList.toggle('result-card__body--open');
    chevronEl.classList.toggle('result-card__chevron--open');
}

// ── MARKDOWN FORMATTING ────────────────────────────────────
function formatMarkdown(text) {
    if (!text) return '';

    let formatted = text
        // Headers
        .replace(/^### (.+)$/gm, '<h4 class="md-h4">$1</h4>')
        .replace(/^## (.+)$/gm, '<h3 class="md-h3">$1</h3>')
        .replace(/^# (.+)$/gm, '<h2 class="md-h2">$1</h2>')
        // Bold
        .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
        // Italic
        .replace(/\*(.+?)\*/g, '<em>$1</em>')
        // Bullet points
        .replace(/^[-•] (.+)$/gm, '<div class="md-bullet">• $1</div>')
        .replace(/^\d+\. (.+)$/gm, '<div class="md-bullet md-bullet--numbered">$&</div>')
        // Line breaks
        .replace(/\n\n/g, '<br><br>')
        .replace(/\n/g, '<br>');

    return `<div class="md-content">${formatted}</div>`;
}

// ── ERROR DISPLAY ──────────────────────────────────────────
function showError(message) {
    hideSection('pipeline-section');
    showSection('error-section');
    document.getElementById('error-message').textContent = message;
}

// ── RESET ──────────────────────────────────────────────────
function resetForm() {
    hideSection('results-section');
    hideSection('error-section');
    hideSection('pipeline-section');

    // Reset form
    document.getElementById('patient-form').reset();

    // Scroll to top
    document.getElementById('input-section').scrollIntoView({ behavior: 'smooth', block: 'start' });

    // Reset pipeline
    resetPipeline();
}

// ── HELPERS ────────────────────────────────────────────────
function showSection(id) {
    const el = document.getElementById(id);
    if (el) {
        el.style.display = 'block';
        el.style.animation = 'slideUp 0.5s ease-out';
    }
}

function hideSection(id) {
    const el = document.getElementById(id);
    if (el) el.style.display = 'none';
}

function toggleButton(loading) {
    const btn = document.getElementById('submit-btn');
    const textEl = btn.querySelector('.btn__text');
    const loaderEl = btn.querySelector('.btn__loader');

    if (loading) {
        textEl.style.display = 'none';
        loaderEl.style.display = 'inline-flex';
        btn.disabled = true;
    } else {
        textEl.style.display = 'inline';
        loaderEl.style.display = 'none';
        btn.disabled = false;
    }
}
