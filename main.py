"""
AutoFlow-AI: CLI Launcher & Demo
Author: Sakil Ahammed (https://github.com/sakilahammed-dev)
"""

import sys
import json

# Ensure cross-platform UTF-8 terminal encoding support
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from engine.agent import AutonomousAgent
from engine.workflow import WorkflowPipeline

def run_demo():
    print("=" * 65)
    print(" [AutoFlow-AI] Autonomous Workflow Engine")
    print(" Developed by: Sakil Ahammed (AI & Full-Stack Software Developer)")
    print("=" * 65)

    # 1. Initialize Autonomous Agent
    agent = AutonomousAgent(
        name="Nova-Agent",
        role="Intelligence & Workflow Automation Specialist",
        capabilities=["task_planning", "data_transformation", "webhook_dispatch"]
    )

    # 2. Build Pipeline
    pipeline = WorkflowPipeline(
        title="Automated Enterprise Lead Intelligence & Dispatch",
        agent=agent
    )

    # 3. Mock Input Payload
    sample_data = {
        "source": "Global CRM Webhook",
        "records": [
            {"id": "lead_101", "name": "Tech Corp Europe", "active": True, "score": 94},
            {"id": "lead_102", "name": "Innovate AI Labs", "active": True, "score": 88},
            {"id": "lead_103", "name": "Legacy Systems LLC", "active": False, "score": 42}
        ]
    }

    print("\n[+] Triggering Autonomous Pipeline Execution...")
    result = pipeline.run(sample_data)

    print("\n" + "=" * 65)
    print(" [*] WORKFLOW EXECUTION SUMMARY")
    print("=" * 65)
    print(f"Status        : {result['status']}")
    print(f"Workflow ID   : {result['workflow_id']}")
    print(f"Agent         : {result['agent_assigned']}")
    print(f"Stages Run    : {result['stages_executed']}")
    print("\nGenerated AI Insights:")
    if result.get("final_report"):
        for insight in result["final_report"]["key_insights"]:
            print(f"  • {insight}")
    print("=" * 65)
    print("[✓] To launch the interactive Web Dashboard, open 'web/index.html' in your browser.\n")

if __name__ == "__main__":
    run_demo()
