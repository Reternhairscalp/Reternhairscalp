"""Severity and confidence policies for consultation extraction."""

from typing import cast

from consultation.extractors import contains_phrase
from consultation.models import Severity
from consultation.vocabulary import SEVERITY_TERMS


class SeverityClassifier:
    """Classify only severity wording explicitly supported by the message."""

    def classify(self, text: str, has_symptoms: bool) -> tuple[Severity | None, list[str]]:
        """Return severity and report conflicting severity descriptions."""
        if not has_symptoms:
            return None, []
        matches = [
            level
            for level, terms in SEVERITY_TERMS.items()
            if any(contains_phrase(text, term) for term in terms)
        ]
        if len(matches) > 1:
            return None, ["conflicting_severity"]
        return (cast(Severity, matches[0]) if matches else None), []


class ConfidenceCalculator:
    """Calculate extraction completeness, not diagnostic certainty."""

    _fields = ("gender", "age", "scalp_problems", "hair_loss_symptoms", "duration", "budget", "severity")

    def calculate(self, values: dict[str, object], ambiguities: list[str]) -> float:
        """Return completeness with a bounded penalty for contradictory evidence."""
        present = sum(self._is_present(values.get(field)) for field in self._fields)
        score = present / len(self._fields) - min(0.3, len(ambiguities) * 0.1)
        return round(max(0.0, min(1.0, score)), 2)

    def missing_fields(self, values: dict[str, object]) -> list[str]:
        """List requested facts for which no evidence was extracted."""
        return [field for field in self._fields if not self._is_present(values.get(field))]

    @staticmethod
    def _is_present(value: object) -> bool:
        return value is not None and value != "" and value != []
