"""
============================================================
Marketing AI
============================================================
"""

from core.config import Config


class MarketingAI:

    def __init__(self, memory):

        self.memory = memory

        self.company = Config.COMPANY_NAME

    def startup(self):

        print("\n" + "=" * 55)
        print("📢 Marketing AI")
        print("=" * 55)

        print(f"Company : {self.company}")

        print("\nKnowledge Loaded")

        for document in self.memory:

            print(f"✅ {document}")

        print("\n🎯 Marketing AI Ready")