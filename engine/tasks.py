import json
import logging
from datetime import datetime
from typing import Dict, Any, List

logger = logging.getLogger("AutoFlow.Tasks")

class TaskRegistry:
    """
    Standardized task library for autonomous automation workflows.
    """

    @staticmethod
    def extract_and_clean_data(raw_payload: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Cleans, normalizes, and filters incoming automation payloads.
        """
        logger.info(f"Extracting and cleaning {len(raw_payload)} input records...")
        valid_records = [r for r in raw_payload if r.get("active", True)]
        
        return {
            "total_received": len(raw_payload),
            "valid_processed": len(valid_records),
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "sample_data": valid_records[:3]
        }

    @staticmethod
    def generate_ai_report(title: str, insights: List[str]) -> Dict[str, Any]:
        """
        Generates an executive structured AI intelligence summary.
        """
        logger.info(f"Generating AI intelligence report: '{title}'")
        report = {
            "title": title,
            "generated_at": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC"),
            "author": "AutoFlow-AI Core",
            "key_insights": insights,
            "status": "APPROVED_FOR_DISPATCH"
        }
        return report

    @staticmethod
    def dispatch_webhook(target_url: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        Simulates dispatching automated webhooks to external business services.
        """
        logger.info(f"Dispatching payload to endpoint: {target_url}")
        return {
            "endpoint": target_url,
            "delivered": True,
            "payload_size_bytes": len(json.dumps(payload)),
            "http_status": 200,
            "delivery_timestamp": datetime.utcnow().isoformat()
        }
