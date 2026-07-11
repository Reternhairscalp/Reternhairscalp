"""
============================================================
Retern Intelligence Platform (RIP)
Knowledge Loader
Version 1.0
============================================================
"""

from pathlib import Path


class KnowledgeLoader:

    def __init__(self):

        # Project Root
        self.project_root = Path(__file__).resolve().parent.parent.parent

    def load_markdown(self, relative_path):

        file_path = self.project_root / relative_path

        try:

            with open(file_path, "r", encoding="utf-8") as file:

                return file.read()

        except FileNotFoundError:

            print(f"❌ File not found: {relative_path}")

            return ""

    def load_customer_dna(self):

        print("\n📚 Loading Customer Knowledge...\n")

        documents = {

            "Customer DNA":
                self.load_markdown("Customer DNA/01-Customer-DNA.md"),

            "Ideal Customer":
                self.load_markdown("Customer DNA/02-Ideal-Customer.md"),

            "Customer Personas":
                self.load_markdown("Customer DNA/03-Customer-Personas.md")

        }

        loaded = 0

        for name, content in documents.items():

            if content:

                print(f"✅ {name}")

                loaded += 1

            else:

                print(f"⚠️ {name} (Empty)")

        print(f"\nKnowledge Files Loaded : {loaded}/{len(documents)}")

        return documents

    def startup(self):

        print("=" * 60)
        print("📖 KNOWLEDGE LOADER")
        print("=" * 60)

        return self.load_customer_dna()