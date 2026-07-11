"""
============================================================
Retern Intelligence Platform (RIP)
Business Schedule Engine
============================================================
"""

from datetime import datetime


class BusinessSchedule:

    def current_status(self):

        now = datetime.now()

        weekday = now.strftime("%A")

        current_time = now.strftime("%H:%M")

        print("\n==============================")
        print("🕒 Business Schedule")
        print("==============================")

        print(f"Today : {weekday}")
        print(f"Time  : {current_time}")

        if weekday == "Sunday":

            print("\n🔴 Business Closed")

            return

        if weekday == "Saturday":

            if current_time < "10:30":
                print("🟡 Before Opening")

            elif current_time <= "19:00":
                print("🟢 Business Open")

            else:
                print("🔴 Business Closed")

            return

        # Monday - Friday

        if current_time < "11:00":

            print("🟡 Staff Preparation")

        elif current_time <= "20:00":

            print("🟢 Business Open")

        else:

            print("🔴 Business Closed")