"""Executable smoke test for the Consultation AI package."""

from consultation.engine import ConsultationEngine


def main() -> None:
    """Run one synthetic consultation through the complete pipeline."""
    result = ConsultationEngine().process(
        "I am a 35-year-old woman with oily scalp and hair loss for 6 months."
    )
    assert result["analysis"]["age"] == 35
    assert result["analysis"]["oily_scalp"] is True
    assert result["recommendation"]["treatments"]


if __name__ == "__main__":
    main()
