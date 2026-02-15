# debate.py

def debate(problem, planner, agent_a, agent_b, judge, strategy):
    """
    Given a problem string and agent instances, run the plan, solution, and judging steps.
    """
    # 1. Planner creates a plan
    plan = planner.respond(problem)

    # 2. Both solver agents respond, using the chosen strategy label in the prompt
    answerA = agent_a.respond(f"{problem}\nStrategy: {strategy}")
    answerB = agent_b.respond(f"{problem}\nStrategy: {strategy}")

    # 3. Prepare a combined prompt for the judge to compare answers
    prompt = (
        f"Problem: {problem}\n\n"
        "Answer A:\n" + answerA + "\n\n"
        "Answer B:\n" + answerB + "\n\n"
        "Who provides the better answer? Answer with 'Winner: A' or 'Winner: B', and explain."
    )
    verdict = judge.respond(prompt)

    # 4. Determine which agent won based on the verdict string
    if "Winner: A" in verdict:
        winner = "logical"
    else:
        winner = "analytical"
    return plan, answerA, answerB, verdict, winner
