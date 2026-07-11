"""
============================================================
Retern Intelligence Platform (RIP)
Knowledge Manager
============================================================
"""

from knowledge.loader import KnowledgeLoader


class KnowledgeManager:

    def __init__(self):

        self.loader = KnowledgeLoader()

        self.memory = {}

    def startup(self):

        print("\n🧠 Initializing Knowledge Manager...\n")

        self.memory = self.loader.startup()

        print("\n✅ Knowledge Manager Ready")

        return self.memory

    def get(self, document):

        return self.memory.get(document, "")