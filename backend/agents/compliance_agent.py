import uuid
from datetime import datetime
from utils.compliance_checker import ComplianceChecker

class ComplianceAgent:
    def __init__(self, params=None):
        self.agent_id = "compliance-" + str(uuid.uuid4())
        self.params = params or {}
        self.compliance_checker = ComplianceChecker()
        self.audit_log = []
        print(f"Compliance Agent {self.agent_id} initialized")
    
    def check_compliance(self, action, context):
        result = self.compliance_checker.check_action(action, context)
        
        audit_entry = {
            "timestamp": datetime.now().isoformat(),
            "action": action,
            "context": context,
            "compliant": result["compliant"],
            "details": result["details"]
        }
        self.audit_log.append(audit_entry)
        
        return result
    
    def generate_report(self):
        compliant_count = sum(1 for entry in self.audit_log if entry["compliant"])
        non_compliant_count = len(self.audit_log) - compliant_count
        
        return {
            "report_id": str(uuid.uuid4()),
            "period_start": self.audit_log[0]["timestamp"] if self.audit_log else "",
            "period_end": self.audit_log[-1]["timestamp"] if self.audit_log else "",
            "total_actions": len(self.audit_log),
            "compliant_actions": compliant_count,
            "non_compliant_actions": non_compliant_count,
            "compliance_rate": compliant_count / len(self.audit_log) if self.audit_log else 1.0
        }
    
    def execute(self, task, params):
        if task == "check_compliance":
            return self.check_compliance(
                params.get("action"),
                params.get("context")
            )
        elif task == "generate_report":
            return self.generate_report()
        else:
            raise ValueError(f"Unknown task: {task}")
