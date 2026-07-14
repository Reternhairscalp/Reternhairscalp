"""Sales AI for the Retern Intelligence Platform."""

from typing import Mapping

from core.config import Config


class SalesAI:
    """Provide the existing rule-based sales guidance interface."""

    def __init__(self, memory: Mapping[str, str]) -> None:
        self.memory = memory
        self.company = Config.COMPANY_NAME

    def startup(self) -> None:
        """Report that the Sales AI is available."""
        print("\n" + "=" * 55)
        print("💼 Sales AI")
        print("=" * 55)
        print(f"Company : {self.company}")
        print("\n🎯 Sales AI Ready")

    def answer(self, question: str) -> None:
        """Print the existing keyword-based sales guidance."""
        query = question.lower()

        print("🧠 Sales AI Analysis\n")

        if "oily" in query:
            print("Customer Concern : Oily Scalp")
            print("Treatment        : Bojin Meridian Hair Growth")
            print("Package          : 6 Sessions")
            print("Home Care        : Oily Control Shampoo")
        elif "hair loss" in query or "thinning" in query:
            print("Customer Concern : Hair Loss")
            print("Treatment        : Bojin Meridian Hair Growth")
            print("Package          : 6 Sessions")
            print("Timeline         : 4–6 Sessions")
        elif "dandruff" in query:
            print("Customer Concern : Dandruff")
            print("Treatment        : Scalp Detox Therapy")
            print("Package          : 3 Sessions")
        else:
            print("Knowledge found.")
            print("Recommendation will be available in v0.6.")
