def answer(self, question):

    q = question.lower()

    print("🧠 Sales AI Analysis\n")

    if "oily" in q:

        print("Customer Concern : Oily Scalp")
        print("Treatment        : Bojin Meridian Hair Growth")
        print("Package          : 6 Sessions")
        print("Home Care        : Oily Control Shampoo")

    elif "hair loss" in q or "thinning" in q:

        print("Customer Concern : Hair Loss")
        print("Treatment        : Bojin Meridian Hair Growth")
        print("Package          : 6 Sessions")
        print("Timeline         : 4–6 Sessions")

    elif "dandruff" in q:

        print("Customer Concern : Dandruff")
        print("Treatment        : Scalp Detox Therapy")
        print("Package          : 3 Sessions")

    else:

        print("Knowledge found.")
        print("Recommendation will be available in v0.6.")