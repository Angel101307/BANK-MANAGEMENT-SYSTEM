def register_issue(account):

    print("\n--- REPORT AN ISSUE ---")

    mobile = input(
        "ENTER YOUR 10 DIGIT MOBILE NUMBER: "
    ).strip()

    if len(mobile) != 10 or not mobile.isdigit():
        print("PLEASE RECHECK YOUR PHONE NUMBER.")
        return

    issue = input("ENTER THE ISSUE: ").strip()

    if issue == "":
        print("ISSUE CANNOT BE EMPTY.")
        return

    print(
        f"ISSUE REGISTERED SUCCESSFULLY FOR "
        f"{account.name}."
    )

    print("OUR TEAM WILL REACH TO YOU SHORTLY!")
