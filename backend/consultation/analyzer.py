"""Production consultation analysis for Retern Hair Growth."""

from consultation.extractors import (
    DemographicExtractor,
    DetailExtractor,
    SymptomExtractor,
    normalize_text,
)
from consultation.models import SCHEMA_VERSION, ConsultationAnalysis
from consultation.safety import SafetyEvaluator
from consultation.scoring import ConfidenceCalculator, SeverityClassifier


class ConsultationAnalyzer:
    """Convert free-text enquiries into a deterministic structured analysis.

    Confidence describes extraction completeness and consistency. It must not
    be interpreted as diagnostic or treatment confidence.
    """

    def __init__(
        self,
        demographics: DemographicExtractor | None = None,
        symptoms: SymptomExtractor | None = None,
        details: DetailExtractor | None = None,
        severity: SeverityClassifier | None = None,
        confidence: ConfidenceCalculator | None = None,
        safety: SafetyEvaluator | None = None,
    ) -> None:
        """Initialize the analyzer with replaceable extraction policies."""
        self._demographics = demographics or DemographicExtractor()
        self._symptoms = symptoms or SymptomExtractor()
        self._details = details or DetailExtractor()
        self._severity = severity or SeverityClassifier()
        self._confidence = confidence or ConfidenceCalculator()
        self._safety = safety or SafetyEvaluator()

    def analyze(self, text: object) -> ConsultationAnalysis:
        """Analyze customer text while preserving the legacy result contract."""
        normalized = normalize_text(text)

        gender, gender_ambiguities = self._demographics.extract_gender(normalized)
        age = self._demographics.extract_age(normalized)
        scalp_problems = self._symptoms.extract_scalp_problems(normalized)
        hair_loss_symptoms = self._symptoms.extract_hair_loss_symptoms(normalized)
        duration = self._details.extract_duration(normalized)
        budget = self._details.extract_budget(normalized)
        severity, severity_ambiguities = self._severity.classify(
            normalized,
            bool(scalp_problems or hair_loss_symptoms),
        )

        ambiguities = gender_ambiguities + severity_ambiguities
        red_flags = self._safety.red_flags(normalized)
        extracted: dict[str, object] = {
            "gender": gender,
            "age": age,
            "scalp_problems": scalp_problems,
            "hair_loss_symptoms": hair_loss_symptoms,
            "duration": duration,
            "budget": budget,
            "severity": severity,
        }

        return {
            "schema_version": SCHEMA_VERSION,
            # Legacy keys remain top-level for current downstream consumers.
            "hair_loss": any(
                symptom in hair_loss_symptoms
                for symptom in ("hair_loss", "hair_fall", "shedding", "bald_spots", "receding_hairline", "balding")
            ),
            "oily_scalp": "oily_scalp" in scalp_problems,
            "dandruff": "dandruff" in scalp_problems,
            "sensitive_scalp": "sensitive_scalp" in scalp_problems,
            "thinning": "thinning" in hair_loss_symptoms,
            "gender": gender,
            "age": age,
            "scalp_problems": scalp_problems,
            "hair_loss_symptoms": hair_loss_symptoms,
            "duration": duration,
            "budget": budget,
            "severity": severity,
            "confidence_score": self._confidence.calculate(extracted, ambiguities),
            "missing_fields": self._confidence.missing_fields(extracted),
            "ambiguities": ambiguities,
            "red_flags": red_flags,
            "requires_human_review": self._safety.requires_human_review(red_flags, ambiguities),
        }
