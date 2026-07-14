"""Reusable deterministic extractors for consultation text."""

import re
from typing import cast

from consultation.models import Gender
from consultation.vocabulary import (
    GENDER_KEYWORDS,
    HAIR_LOSS_SYMPTOMS,
    NUMBER_WORDS,
    SCALP_PROBLEMS,
)


def normalize_text(text: object) -> str:
    """Return normalized lowercase text, or an empty string for invalid input."""
    if not isinstance(text, str):
        return ""
    return " ".join(text.lower().strip().split())


def contains_phrase(text: str, phrase: str) -> bool:
    """Match a complete phrase rather than an arbitrary substring."""
    return re.search(rf"\b{re.escape(phrase)}\b", text) is not None


class DemographicExtractor:
    """Extract age and gender while reporting contradictory gender evidence."""

    _age_patterns = (
        re.compile(r"\b(?:i(?:\s+am|'m)|age(?:d)?(?:\s+is)?|customer\s+is)\s*(\d{1,3})\b"),
        re.compile(r"\b(\d{1,3})[\s-]*(?:years?[\s-]*old)\b"),
    )

    def extract_gender(self, text: str) -> tuple[Gender | None, list[str]]:
        """Return a normalized gender and any ambiguity messages."""
        matches = [
            gender
            for gender, terms in GENDER_KEYWORDS.items()
            if any(contains_phrase(text, term) for term in terms)
        ]
        if len(matches) > 1:
            return None, ["conflicting_gender"]
        return (cast(Gender, matches[0]) if matches else None), []

    def extract_age(self, text: str) -> int | None:
        """Extract a plausible human age from explicit age wording."""
        for pattern in self._age_patterns:
            match = pattern.search(text)
            if match:
                age = int(match.group(1))
                return age if 1 <= age <= 120 else None
        return None


class SymptomExtractor:
    """Extract normalized scalp and hair-loss symptoms with local negation."""

    _negation_pattern = re.compile(r"\b(?:no|not|never|without|don't|do not)\b[^.!?,;]{0,24}$")

    def extract_scalp_problems(self, text: str) -> list[str]:
        """Return all non-negated scalp problems in stable vocabulary order."""
        return self._extract_terms(text, SCALP_PROBLEMS)

    def extract_hair_loss_symptoms(self, text: str) -> list[str]:
        """Return all non-negated hair-loss symptoms in stable vocabulary order."""
        return self._extract_terms(text, HAIR_LOSS_SYMPTOMS)

    def _extract_terms(self, text: str, vocabulary: dict[str, tuple[str, ...]]) -> list[str]:
        extracted: list[str] = []
        for normalized, phrases in vocabulary.items():
            if any(self._has_positive_match(text, phrase) for phrase in phrases):
                extracted.append(normalized)
        return extracted

    def _has_positive_match(self, text: str, phrase: str) -> bool:
        for match in re.finditer(rf"\b{re.escape(phrase)}\b", text):
            if not self._negation_pattern.search(text[max(0, match.start() - 32):match.start()]):
                return True
        return False


class DetailExtractor:
    """Extract consultation duration and customer budget."""

    _budget_patterns = (
        re.compile(r"\b(?:budget|afford|spend)\D{0,20}(?:sgd\s*|s\$\s*|\$\s*)(\d[\d,]*(?:\.\d{1,2})?)\b"),
        re.compile(r"\b(?:budget|afford|spend)(?:\s+is|\s+of|\s+around|\s+about|\s+below|\s+under|\s+up\s+to|\s+maximum|\s+max|\s*:)?\s*(\d[\d,]*(?:\.\d{1,2})?)\b"),
        re.compile(r"(?:\bsgd\s*|s\$\s*|\$\s*)(\d[\d,]*(?:\.\d{1,2})?)\b"),
    )
    _duration_pattern = re.compile(
        r"\b(?:(?:for|since|past|last|about|around|approximately|almost)\s+)?"
        r"(\d+(?:\.\d+)?|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve)\s*"
        r"(day|week|month|year)s?\b"
    )

    def extract_budget(self, text: str) -> int | float | None:
        """Extract an explicitly stated numeric budget."""
        for pattern in self._budget_patterns:
            match = pattern.search(text)
            if match:
                amount = float(match.group(1).replace(",", ""))
                return int(amount) if amount.is_integer() else amount
        return None

    def extract_duration(self, text: str) -> str | None:
        """Return a normalized duration without confusing age for duration."""
        for match in self._duration_pattern.finditer(text):
            if re.match(r"[\s-]*old\b", text[match.end():]):
                continue
            quantity, unit = match.groups()
            quantity = NUMBER_WORDS.get(quantity, quantity)
            suffix = "" if quantity == "1" else "s"
            return f"{quantity} {unit}{suffix}"
        return None
