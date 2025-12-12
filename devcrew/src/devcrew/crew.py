# crew.py
from crewai import Agent, Task, Crew
from langchain_openai import ChatOpenAI
from crewai_tools import FileReadTool, FileWriterTool  # Correct names
import os
from dotenv import load_dotenv

load_dotenv()

# LLM — using the fast & cheap gpt-4o-mini (perfect for dev tasks)
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)

# Tools
read_tool = FileReadTool()
write_tool = FileWriterTool()

# ────────────────────────────── AGENTS ──────────────────────────────

requirements_agent = Agent(
    role="Requirements Analyst",
    goal="Turn the user's high-level idea into detailed, actionable specifications for the Caspio + React app.",
    backstory="You are a senior business analyst who excels at clarifying vague requests.",
    tools=[read_tool],
    llm=llm,
    verbose=True,
    allow_delegation=False
)

architect_agent = Agent(
    role="Software Architect",
    goal="Design the component structure, file layout, and data flow for the React + Caspio integration.",
    backstory="You create clean, scalable, mobile-responsive architectures.",
    tools=[read_tool, write_tool],
    llm=llm,
    verbose=True,
    allow_delegation=False
)

coder_agent = Agent(
    role="Full-Stack React Developer",
    goal="Write production-ready React/Vite code that talks to Caspio REST API, adds new features, and stays secure.",
    backstory="You love React hooks, clean JSX, Tailwind/MUI, and never expose secrets client-side.",
    tools=[read_tool, write_tool],
    llm=llm,
    verbose=True,
    allow_delegation=False
)

tester_agent = Agent(
    role="QA Engineer",
    goal="Verify the code works, catches edge cases, and suggest fixes.",
    backstory="You are relentless about bugs and love writing Jest/React Testing Library tests.",
    tools=[read_tool, write_tool],
    llm=llm,
    verbose=True,
    allow_delegation=False
)

deployer_agent = Agent(
    role="DevOps Engineer",
    goal="Commit changes, build the app, and deploy to Vercel (or Netlify) with a live URL.",
    backstory="You automate everything with Git and Vercel CLI.",
    tools=[read_tool, write_tool],
    llm=llm,
    verbose=True,
    allow_delegation=False
)

# ────────────────────────────── TASKS ──────────────────────────────

def create_crew(user_brief: str):
    task1 = Task(
        description=f"Analyze this user request and write a detailed requirements.md file:\n\n{user_brief}",
        expected_output="requirements.md",
        agent=requirements_agent,
    )

    task2 = Task(
        description="Read requirements.md and create an architecture.md plus a component tree (JSON or markdown).",
        expected_output="architecture.md and component_tree.json",
        agent=architect_agent,
    )

    task3 = Task(
        description="Implement the requested features in the existing React app (src/App.jsx, etc.). Use environment variables for Caspio secrets.",
        expected_output="Updated or new source files (App.jsx, utils/, etc.)",
        agent=coder_agent,
    )

    task4 = Task(
        description="Review the generated code, suggest or write tests, and fix any bugs found.",
        expected_output="test_report.md and any patched files",
        agent=tester_agent,
    )

    task5 = Task(
        description="Commit all changes with a clear message, push to GitHub, and deploy to Vercel. Return the live URL.",
        expected_output="deployment_log.md containing the live URL",
        agent=deployer_agent,
    )

    crew = Crew(
        agents=[requirements_agent, architect_agent, coder_agent, tester_agent, deployer_agent],
        tasks=[task1, task2, task3, task4, task5],
        verbose=True,  # Great for watching the magic happen
    )

    result = crew.kickoff()
    return result


# ─────────────────────── CHANGE YOUR BRIEF HERE ───────────────────────
if __name__ == "__main__":
    brief = """
    Enhance my existing Caspio search app (table: name_test_tbl with First_Name and Description).
    Add:
      • User login (simple email/password stored in a separate Caspio auth table)
      • Export search results to CSV button
      • Dark mode toggle
      • Make it a Progressive Web App (PWA) so it works offline on mobile
    Keep everything responsive and beautiful.
    """
    print("Starting AI DevCrew with your brief...")
    print(create_crew(brief))