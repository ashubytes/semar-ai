import streamlit as st
from agents import Agent
from strategy import StrategyManager
from memory import save, load
from debate import debate
from metrics import Metrics

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="SEMAR AI",
    page_icon="🧠",
    layout="wide"
)

# ---------- HEADER ----------
st.markdown("""
<h1 style='text-align:center;'>🧠 SEMAR</h1>
<h4 style='text-align:center;color:gray;'>
Self-Evolving Multi-Agent Reasoning System
</h4>
""", unsafe_allow_html=True)

st.divider()

# ---------- SIDEBAR ----------
st.sidebar.title("⚙ System Panel")
st.sidebar.info("Multi-Agent AI Reasoning Engine")

strategy_manager = StrategyManager()
metrics = Metrics()

st.sidebar.metric("Total Runs", metrics.total)
st.sidebar.write("Strategy Scores")
st.sidebar.write(strategy_manager.scores)

# ---------- AGENTS ----------
planner = Agent("Planner",
"You break problems into structured logical steps.")

solverA = Agent("Solver A",
"You solve problems step-by-step logically.")

solverB = Agent("Solver B",
"You solve problems analytically and deeply.")

judge = Agent("Judge",
"""
You are an evaluator.

Compare answers and choose best.

Format:
Winner: A or B
Reason: explanation
""")

# ---------- INPUT BOX ----------
problem = st.text_area(
    "Enter Problem",
    placeholder="Type a complex question here...",
    height=150
)

# ---------- RUN BUTTON ----------
if st.button("🚀 Run SEMAR", use_container_width=True):

    if not problem:
        st.warning("Please enter a problem first.")
        st.stop()

    status = st.empty()

    # Planner
    status.info("🧠 Planner thinking...")
    plan = planner.respond(problem)

    # Solver A
    status.info("🤖 Solver A reasoning...")
    ansA = solverA.respond(problem)

    # Solver B
    status.info("🤖 Solver B analyzing...")
    ansB = solverB.respond(problem)

    # Judge
    status.info("⚖ Judge evaluating...")
    verdict = judge.respond(f"""
Problem: {problem}

Answer A:
{ansA}

Answer B:
{ansB}
""")

    status.success("✅ Complete!")

    winner = "logical" if "A" in verdict else "analytical"

    strategy_manager.update(winner)
    metrics.log(winner)
    save(problem, winner)

    st.divider()

    # ---------- RESULTS LAYOUT ----------
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🧠 Planner Output")
        st.success(plan)

        st.subheader("🤖 Solver A")
        st.info(ansA)

    with col2:
        st.subheader("🤖 Solver B")
        st.info(ansB)

        st.subheader("⚖ Judge Verdict")
        st.warning(verdict)

    st.divider()

    st.success(f"🏆 Winning Strategy → {winner}")

# ---------- MEMORY ----------
st.divider()
st.subheader("📚 Memory Log")
if st.button("🗑 Clear Memory"):
    from memory import clear
    clear()
    st.success("Memory cleared!")


memories = load()
if memories:
    st.json(memories[-5:])
else:
    st.caption("No memory yet")

# ---------- FOOTER ----------
st.divider()
st.caption("SEMAR — Multi-Agent Cognitive Architecture")
