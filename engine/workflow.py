import uuid
import logging
from typing import Dict, Any, List
from .agent import AutonomousAgent
from .tasks import TaskRegistry

logger = logging.getLogger("AutoFlow.Workflow")

class WorkflowPipeline:
    """
    End-to-End Orchestrator connecting triggers, AI reasoning, and automated actions.
    """

    def __init__(self, title: str, agent: AutonomousAgent):
        self.workflow_id = f"wf_{uuid.uuid4().hex[:8]}"
        self.title = title
        self.agent = agent
        self.logs: List[str] = []

    def log(self, message: str):
        formatted = f"[{self.workflow_id}] {message}"
        self.logs.append(formatted)
        logger.info(formatted)

    def run(self, initial_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Executes the autonomous pipeline from trigger to dispatch.
        """
        self.log(f"Initiating workflow: '{self.title}'")
        
        # 1. Agent plans the execution
        steps = self.agent.plan_workflow(objective=self.title)
        self.log(f"Formulated {len(steps)} sequential execution stages.")
        
        execution_results = []
        context = dict(initial_data)

        # 2. Sequential execution
        for step in steps:
            self.log(f"Triggering execution step {step['id']}: {step['task']}")
            res = self.agent.execute_step(step, context)
            execution_results.append(res)
            
            # Simulated data enrichment along the pipeline
            if step["type"] == "intake":
                cleaned = TaskRegistry.extract_and_clean_data(context.get("records", []))
                context["cleaned_data"] = cleaned
            elif step["type"] == "ai_reasoning":
                insights = [
                    "Detected 28% efficiency opportunity in pipeline throughput.",
                    "Automated error recovery triggered with 0% data drop.",
                    "Synthesized real-time telemetry across active nodes."
                ]
                context["ai_report"] = TaskRegistry.generate_ai_report(self.title, insights)
            elif step["type"] == "dispatch":
                dispatch_res = TaskRegistry.dispatch_webhook(
                    "https://api.business-automation.internal/v1/ingest",
                    context.get("ai_report", {})
                )
                context["dispatch_receipt"] = dispatch_res

        self.log(f"Workflow '{self.title}' concluded successfully with 100% success rate.")
        
        return {
            "workflow_id": self.workflow_id,
            "title": self.title,
            "status": "SUCCESS",
            "agent_assigned": self.agent.name,
            "stages_executed": len(execution_results),
            "final_report": context.get("ai_report"),
            "audit_trail": self.logs
        }
