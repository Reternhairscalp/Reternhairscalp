"""Contract tests for Consultation AI consumers."""

import json
import sys
import unittest
from pathlib import Path

BACKEND = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BACKEND))

from consultation.analyzer import ConsultationAnalyzer  # noqa: E402
from consultation.models import SCHEMA_VERSION  # noqa: E402


class ConsultationContractTests(unittest.TestCase):
    """Protect the versioned and legacy result contracts."""

    def test_required_and_legacy_keys(self) -> None:
        result = ConsultationAnalyzer().analyze("Oily scalp and thinning hair")
        required = {
            "schema_version", "hair_loss", "oily_scalp", "dandruff",
            "sensitive_scalp", "thinning", "gender", "age",
            "scalp_problems", "hair_loss_symptoms", "duration", "budget",
            "severity", "confidence_score", "missing_fields", "ambiguities",
            "red_flags", "requires_human_review",
        }
        self.assertEqual(set(result), required)
        self.assertEqual(result["schema_version"], SCHEMA_VERSION)
        for key in ("hair_loss", "oily_scalp", "dandruff", "sensitive_scalp", "thinning"):
            self.assertIsInstance(result[key], bool)

    def test_result_is_json_serializable(self) -> None:
        result = ConsultationAnalyzer().analyze("Female age 35, dandruff for 2 months, budget SGD 500")
        json.dumps(result)


if __name__ == "__main__":
    unittest.main()
