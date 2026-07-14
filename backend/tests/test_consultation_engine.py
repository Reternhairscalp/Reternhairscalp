"""Integration tests for the existing consultation pipeline."""

import contextlib
import io
import sys
import unittest
from pathlib import Path

BACKEND = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BACKEND))

from consultation.engine import ConsultationEngine  # noqa: E402


class ConsultationEngineTests(unittest.TestCase):
    """Verify compatibility across analysis, recommendations, and replies."""

    def process(self, text: str) -> dict[str, object]:
        with contextlib.redirect_stdout(io.StringIO()):
            return ConsultationEngine().process(text)

    def test_existing_envelope_and_recommendation(self) -> None:
        result = self.process("I have oily scalp and hair loss for 6 months.")
        self.assertEqual(set(result), {"analysis", "recommendation", "whatsapp"})
        analysis = result["analysis"]
        recommendation = result["recommendation"]
        self.assertTrue(analysis["hair_loss"])
        self.assertTrue(analysis["oily_scalp"])
        self.assertTrue(recommendation["treatments"])
        self.assertIsInstance(result["whatsapp"], str)

    def test_review_case_suppresses_automatic_treatment(self) -> None:
        result = self.process("I have sudden hair loss and severe pain.")
        self.assertTrue(result["analysis"]["requires_human_review"])
        self.assertEqual(result["recommendation"]["treatments"], [])
        self.assertIn("professional team", result["whatsapp"])


if __name__ == "__main__":
    unittest.main()
