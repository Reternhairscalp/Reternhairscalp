"""Conservative escalation rules for customer consultation text."""

from consultation.extractors import contains_phrase
from consultation.vocabulary import RED_FLAG_TERMS


class SafetyEvaluator:
    """Detect wording that requires professional human review."""

    def red_flags(self, text: str) -> list[str]:
        """Return normalized red flags; these are not medical diagnoses."""
        return [
            flag
            for flag, terms in RED_FLAG_TERMS.items()
            if any(contains_phrase(text, term) for term in terms)
        ]

    @staticmethod
    def requires_human_review(red_flags: list[str], ambiguities: list[str]) -> bool:
        """Require review for safety flags or contradictory extracted facts."""
        return bool(red_flags or ambiguities)
