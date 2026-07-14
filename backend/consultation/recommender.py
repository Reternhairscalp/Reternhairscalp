"""

from consultation.models import ConsultationAnalysis, TreatmentRecommendation
============================================================
Consultation Recommender
Retern Hair Growth
============================================================
"""


class TreatmentRecommender:
    """Create conservative wellness recommendations from structured analysis."""

    def recommend(self, analysis: ConsultationAnalysis) -> TreatmentRecommendation:
        """Return the legacy recommendation shape with an added review signal."""

        recommendations: TreatmentRecommendation = {
            "treatments": [],
            "home_care": [],
            "package": None,
            "timeline": None,
            "requires_human_review": analysis["requires_human_review"],
        }

        if analysis["requires_human_review"]:
            return recommendations

        if analysis["hair_loss"] or analysis["thinning"]:

            recommendations["treatments"].append(
                "Bojin Meridian Hair Growth Therapy"
            )

            recommendations["home_care"].append(
                "Hair Growth Shampoo"
            )

            recommendations["home_care"].append(
                "CM+ Scalp Serum"
            )

            recommendations["package"] = "6 Sessions"
            recommendations["timeline"] = "4–6 Sessions"

        if analysis["oily_scalp"]:

            recommendations["treatments"].append(
                "Scalp Detox Treatment"
            )

            recommendations["home_care"].append(
                "Oily Control Shampoo"
            )

            if recommendations["package"] is None:
                recommendations["package"] = "3 Sessions"

        if analysis["dandruff"]:

            recommendations["treatments"].append(
                "Anti-Dandruff Scalp Therapy"
            )

            recommendations["home_care"].append(
                "Anti-Dandruff Shampoo"
            )

        if analysis["sensitive_scalp"]:

            recommendations["treatments"].append(
                "Sensitive Scalp Recovery Therapy"
            )

            recommendations["home_care"].append(
                "Sensitive Scalp Shampoo"
            )

        return recommendations
