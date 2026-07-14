"""Public type contracts for the consultation package."""

from typing import Literal, TypedDict

SCHEMA_VERSION = "1.0"

Gender = Literal["female", "male"]
Severity = Literal["mild", "moderate", "severe"]


class ConsultationAnalysis(TypedDict):
    """Serializable result returned by :class:`ConsultationAnalyzer`."""

    schema_version: str
    hair_loss: bool
    oily_scalp: bool
    dandruff: bool
    sensitive_scalp: bool
    thinning: bool
    gender: Gender | None
    age: int | None
    scalp_problems: list[str]
    hair_loss_symptoms: list[str]
    duration: str | None
    budget: int | float | None
    severity: Severity | None
    confidence_score: float
    missing_fields: list[str]
    ambiguities: list[str]
    red_flags: list[str]
    requires_human_review: bool


class TreatmentRecommendation(TypedDict):
    """Result returned by the treatment recommender."""

    treatments: list[str]
    home_care: list[str]
    package: str | None
    timeline: str | None
    requires_human_review: bool


class ConsultationResult(TypedDict):
    """Top-level result returned by the consultation engine."""

    analysis: ConsultationAnalysis
    recommendation: TreatmentRecommendation
    whatsapp: str
