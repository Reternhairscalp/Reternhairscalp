"""
============================================================
Retern Intelligence Platform (RIP)
Knowledge Database
============================================================
"""


class KnowledgeDB:

    def __init__(self):
        self.data = {}

    def add(self, category, title, content):

        if category not in self.data:
            self.data[category] = {}

        self.data[category][title] = content

    def get(self, category, title):

        return self.data.get(category, {}).get(title)

    def categories(self):

        return list(self.data.keys())