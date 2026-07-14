"""
============================================================
Consultation Engine
Retern Hair Growth
============================================================
"""

from consultation.analyzer import ConsultationAnalyzer
from consultation.recommender import TreatmentRecommender
from consultation.whatsapp import WhatsAppGenerator
from consultation.models import ConsultationResult


class ConsultationEngine:
    """Coordinate analysis, recommendation, and customer-message generation."""

    def __init__(
        self,
        analyzer: ConsultationAnalyzer | None = None,
        recommender: TreatmentRecommender | None = None,
        whatsapp: WhatsAppGenerator | None = None,
    ) -> None:
        """Initialize default components or use injected compatible instances."""
        self.analyzer = analyzer or ConsultationAnalyzer()
        self.recommender = recommender or TreatmentRecommender()
        self.whatsapp = whatsapp or WhatsAppGenerator()

    def process(self, customer_text: object) -> ConsultationResult:
        """Run the existing consultation pipeline and return its result envelope."""

        print("\n============================================================")
        print("🧠 RETERN CONSULTATION ENGINE")
        print("============================================================")

        analysis = self.analyzer.analyze(customer_text)

        recommendation = self.recommender.recommend(analysis)

        message = self.whatsapp.generate(
            analysis,
            recommendation
        )

        print("\nCustomer Analysis")
        print("----------------------------")

        for item, value in analysis.items():
            print(f"{item:20} : {value}")

        print("\nRecommended Treatments")
        print("----------------------------")

        for treatment in recommendation["treatments"]:
            print(f"• {treatment}")

        print("\nHome Care")
        print("----------------------------")

        for item in recommendation["home_care"]:
            print(f"• {item}")

        print(f"\nPackage  : {recommendation['package']}")
        print(f"Timeline : {recommendation['timeline']}")

        print("\nWhatsApp Reply")
        print("----------------------------")
        print(message)

        return {
            "analysis": analysis,
            "recommendation": recommendation,
            "whatsapp": message
        }
