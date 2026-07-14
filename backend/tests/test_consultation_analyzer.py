"""Unit and regression tests for consultation analysis."""

import json
import sys
import unittest
from pathlib import Path

BACKEND = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BACKEND))

from consultation.analyzer import ConsultationAnalyzer  # noqa: E402


class ConsultationAnalyzerTests(unittest.TestCase):
    """Verify normalized extraction and safety behavior."""

    def setUp(self) -> None:
        self.analyzer = ConsultationAnalyzer()

    def test_fixture_cases(self) -> None:
        fixture = Path(__file__).parent / "fixtures" / "consultation_cases.json"
        cases = json.loads(fixture.read_text(encoding="utf-8"))
        for case in cases:
            with self.subTest(case=case["name"]):
                result = self.analyzer.analyze(case["text"])
                for key, expected in case["expected"].items():
                    self.assertEqual(result[key], expected)

    def test_invalid_input_is_safe(self) -> None:
        result = self.analyzer.analyze(None)
        self.assertEqual(result["confidence_score"], 0.0)
        self.assertEqual(result["scalp_problems"], [])
        self.assertFalse(result["hair_loss"])

    def test_age_is_not_duration(self) -> None:
        result = self.analyzer.analyze("I am a 42 year old male.")
        self.assertEqual(result["age"], 42)
        self.assertIsNone(result["duration"])

    def test_budget_formats(self) -> None:
        self.assertEqual(self.analyzer.analyze("Budget S$1,200")["budget"], 1200)
        self.assertEqual(self.analyzer.analyze("I can spend $399.50")["budget"], 399.5)

    def test_conflicting_gender_requires_review(self) -> None:
        result = self.analyzer.analyze("The message says male and female.")
        self.assertIsNone(result["gender"])
        self.assertIn("conflicting_gender", result["ambiguities"])
        self.assertTrue(result["requires_human_review"])

    def test_local_negation_does_not_hide_positive_symptom(self) -> None:
        result = self.analyzer.analyze("No bald spots, but I have heavy shedding.")
        self.assertNotIn("bald_spots", result["hair_loss_symptoms"])
        self.assertIn("shedding", result["hair_loss_symptoms"])
        self.assertTrue(result["hair_loss"])

    def test_red_flag_requires_review(self) -> None:
        result = self.analyzer.analyze("I have sudden hair loss and severe pain.")
        self.assertIn("sudden_hair_loss", result["red_flags"])
        self.assertIn("severe_pain", result["red_flags"])
        self.assertTrue(result["requires_human_review"])

    def test_confidence_is_bounded(self) -> None:
        for text in ("", "hair loss", "female age 30 oily scalp for 1 year budget $500 mild"):
            score = self.analyzer.analyze(text)["confidence_score"]
            self.assertGreaterEqual(score, 0.0)
            self.assertLessEqual(score, 1.0)


if __name__ == "__main__":
    unittest.main()
