"""
============================================================
Retern Intelligence Platform (RIP)
Daily Mission Service
Version 1.0
============================================================
"""

from datetime import datetime

from core.config import Config


class DailyMission:

    def __init__(self):

        self.today = datetime.now()

    def briefing(self):

        return {

            "Business": Config.COMPANY_NAME,

            "Date": self.today.strftime("%A, %d %B %Y"),

            "Lead Target": Config.MONTHLY_LEAD_TARGET,

            "Appointment Target": Config.MONTHLY_APPOINTMENT_TARGET,

            "Today's Tasks": [

                "Generate 2 Facebook Posts",

                "Generate 3 TikTok Videos",

                "Publish 5 SEO Blog Articles",

                "Reply Google Reviews",

                "Reply WhatsApp Leads",

                "Review Meta Ads",

                "Review TikTok Ads"

            ],

            "Today's Priority": [

                "Hair Loss",

                "Hair Thinning",

                "Oily Scalp",

                "Dandruff"

            ],

            "CEO Focus": [

                "Review Appointment Booking",

                "Check Daily Sales",

                "Review AI Reports",

                "Monitor Marketing Performance"

            ]

        }

    def startup(self):

        mission = self.briefing()

        print("\n" + "=" * 60)
        print("📋 CEO DAILY MISSION")
        print("=" * 60)

        print(f"Business : {mission['Business']}")
        print(f"Date     : {mission['Date']}")

        print("\n🎯 Monthly Targets")

        print(f"Leads            : {mission['Lead Target']}")
        print(f"Appointments     : {mission['Appointment Target']}")

        print("\n📢 Today's Tasks")

        for task in mission["Today's Tasks"]:

            print(f"✅ {task}")

        print("\n🔥 Today's Priority")

        for item in mission["Today's Priority"]:

            print(f"• {item}")

        print("\n👨‍💼 CEO Focus")

        for item in mission["CEO Focus"]:

            print(f"• {item}")

        print("\n🟢 Daily Mission Ready")