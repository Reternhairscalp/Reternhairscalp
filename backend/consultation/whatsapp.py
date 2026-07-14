"""

from consultation.models import ConsultationAnalysis, TreatmentRecommendation
============================================================
WhatsApp Reply Generator
Retern Hair Growth
============================================================
"""


class WhatsAppGenerator:
    """Generate a customer-safe consultation reply."""

    def generate(
        self,
        analysis: ConsultationAnalysis,
        recommendation: TreatmentRecommendation,
    ) -> str:
        """Generate guidance or a professional-review response as appropriate."""

        if analysis["requires_human_review"]:
            return self._generate_review_message()

        message = []

        message.append("Hi 😊")
        message.append("")
        message.append("Thank you for contacting Retern Hair Growth.")
        message.append("")

        if analysis["hair_loss"] or analysis["thinning"]:
            message.append(
                "Based on the information you shared, we noticed signs of hair thinning / hair loss."
            )

        if analysis["oily_scalp"]:
            message.append(
                "Your scalp may also have excessive oil production which can affect healthy hair growth."
            )

        if analysis["dandruff"]:
            message.append(
                "We also recommend improving your scalp condition to reduce dandruff."
            )

        message.append("")
        message.append("Recommended Treatment:")

        for treatment in recommendation["treatments"]:
            message.append(f"• {treatment}")

        message.append("")

        if recommendation["package"]:
            message.append(
                f"Recommended Package: {recommendation['package']}"
            )

        if recommendation["timeline"]:
            message.append(
                f"Expected Results: {recommendation['timeline']}"
            )

        message.append("")
        message.append(
            "We recommend booking a professional scalp analysis so our consultant can examine your scalp using our scalp microscope and recommend the most suitable treatment plan."
        )

        message.append("")
        message.append("Would you like us to reserve an appointment for you this week? 😊")

        return "\n".join(message)

    @staticmethod
    def _generate_review_message() -> str:
        """Return a neutral response when automated guidance is inappropriate."""
        return "\n".join([
            "Hi 😊",
            "",
            "Thank you for contacting Retern Hair Growth.",
            "",
            "The information you shared would be best reviewed by our professional team before we suggest any scalp-care options.",
            "",
            "Would you like us to arrange a professional scalp consultation for you?",
        ])
