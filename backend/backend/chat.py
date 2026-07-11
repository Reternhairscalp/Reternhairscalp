"""
============================================================
Retern Intelligence Platform
Interactive AI Assistant
============================================================
"""

from knowledge.manager import KnowledgeManager
from agents.sales_ai import SalesAI


def main():

    print("=" * 60)
    print("🤖 RETERN AI ASSISTANT")
    print("=" * 60)

    knowledge = KnowledgeManager()
    memory = knowledge.startup()

    sales = SalesAI(memory)

    while True:

        print()

        question = input("You > ")

        if question.lower() in ["exit", "quit"]:

            print("👋 Goodbye CEO")
            break

        print()

        sales.answer(question)


if __name__ == "__main__":
    main()