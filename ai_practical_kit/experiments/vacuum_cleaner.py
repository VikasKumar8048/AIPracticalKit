"""Experiment 1: Simple Reflex Agent for the Vacuum Cleaner World.

Run standalone with: python -m ai_practical_kit.experiments.vacuum_cleaner
"""


def solve_vacuum(room_a, room_b, position):
    """Return the action sequence and final state for a two-room vacuum agent.

    room_a / room_b accept 'D' or 'C' (also 1=dirty, 0=clean).
    position accepts 'A' or 'B'.
    """
    def clean_status(value):
        value = str(value).strip().upper()
        if value in ("D", "1"):
            return "D"
        if value in ("C", "0"):
            return "C"
        raise ValueError("Room status must be D/C or 1/0.")

    room_a = clean_status(room_a)
    room_b = clean_status(room_b)
    position = str(position).strip().upper()
    if position not in ("A", "B"):
        raise ValueError("Position must be A or B.")

    actions = []
    while room_a == "D" or room_b == "D":
        if position == "A":
            if room_a == "D":
                actions.append("SUCK Room A")
                room_a = "C"
            else:
                actions.append("MOVE RIGHT to Room B")
                position = "B"
        else:
            if room_b == "D":
                actions.append("SUCK Room B")
                room_b = "C"
            else:
                actions.append("MOVE LEFT to Room A")
                position = "A"

    return {"actions": actions, "room_a": room_a, "room_b": room_b,
            "position": position}


def run_cli():
    print("\nEXPERIMENT 1: VACUUM CLEANER AGENT")
    print("Enter 1 for Dirty or 0 for Clean (D/C also accepted).")
    a = input("Room A status: ")
    b = input("Room B status: ")
    pos = input("Agent starts in room A or B: ")
    try:
        result = solve_vacuum(a, b, pos)
    except ValueError as error:
        print("Input error:", error)
        return
    print("\nActions:")
    if not result["actions"]:
        print("No action needed.")
    else:
        for number, action in enumerate(result["actions"], 1):
            print(str(number) + ". " + action)
    print("Final state: A =", result["room_a"], ", B =", result["room_b"])
    print("Both rooms are clean.")


if __name__ == "__main__":
    run_cli()
