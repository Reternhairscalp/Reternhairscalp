"""
============================================================
Retern Intelligence Platform (RIP)
Core System
Version : 0.4
============================================================
"""

from core.config import Config
from core.business_schedule import BusinessSchedule
from core.brain import AIBrain

from dashboard.ceo_dashboard import CEODashboard

from knowledge.manager import KnowledgeManager

from agents.marketing_ai import MarketingAI
from agents.sales_ai import SalesAI


class RIPSystem:

    def __init__(self):

        self.company = Config.COMPANY_NAME
        self.version = Config.VERSION

    def startup(self):

        # ============================================
        # System Header
        # ============================================

        self.print_header()

        # ============================================
        # Load Core Modules
        # ============================================

        self.load_modules()

        # ============================================
        # Business Schedule
        # ============================================

        schedule = BusinessSchedule()
        schedule.current_status()

        # ============================================
        # CEO Dashboard
        # ============================================

        dashboard = CEODashboard()
        dashboard.startup()

        # ============================================
        # Knowledge Engine
        # ============================================

        knowledge = KnowledgeManager()
        memory = knowledge.startup()

        # ============================================
        # AI Brain
        # ============================================

        brain = AIBrain()
        brain.startup()

        # ============================================
        # AI Workforce
        # ============================================

        marketing = MarketingAI(memory)
        marketing.startup()

        sales = SalesAI(memory)
        sales.startup()

        # ============================================
        # System Ready
        # ============================================

        self.print_footer()

    def print_header(self):

        print("=" * 70)
        print("🚀 Retern Intelligence Platform")
        print(f"Company : {self.company}")
        print(f"Version : {self.version}")
        print("=" * 70)

    def print_footer(self):

        print("\n" + "=" * 70)
        print("✅ RIP Started Successfully")
        print("=" * 70)

    def load_modules(self):

        print("\nLoading Core Modules...\n")

        modules = [

            "Business Engine",

            "Knowledge Engine",

            "Customer DNA",

            "AI Brain",

            "AI Workforce",

            "Automation Engine",

            "CEO Dashboard"

        ]

        for module in modules:

            print(f"✅ {module}")