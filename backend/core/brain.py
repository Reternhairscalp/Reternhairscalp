"""
============================================================
Retern Intelligence Platform (RIP)
AI Brain
============================================================
"""

from database.knowledge_db import KnowledgeDB


class AIBrain:

    def __init__(self):
        self.db = KnowledgeDB()

    def startup(self):
        print("\n============================================================")
        print("🧠 AI BRAIN")
        print("============================================================")
        print("✅ AI Brain Ready")

    def think(self, question):
        print(f"🤔 Thinking: {question}")
        return "Knowledge Search Ready"

    def remember(self, category, title, content):
        self.db.add(category, title, content)

    def recall(self, category, title):
        return self.db.get(category, title)