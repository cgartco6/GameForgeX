import uuid
import time
import random
from datetime import datetime
from utils.payment_processor import PaymentProcessor

class PaymentsAgent:
    def __init__(self, params=None):
        self.agent_id = "payments-" + str(uuid.uuid4())
        self.params = params or {}
        self.payment_processor = PaymentProcessor()
        self.transactions = []
        print(f"Payments Agent {self.agent_id} initialized")
    
    def process_payment(self, amount, currency, recipient):
        transaction_id = str(uuid.uuid4())
        
        # Simulate payment processing
        time.sleep(1)
        
        transaction = {
            "transaction_id": transaction_id,
            "amount": amount,
            "currency": currency,
            "recipient": recipient,
            "status": "completed",
            "timestamp": datetime.now().isoformat(),
            "fee": amount * 0.02  # 2% transaction fee
        }
        self.transactions.append(transaction)
        return transaction
    
    def distribute_payments(self, payments):
        results = []
        for payment in payments:
            result = self.process_payment(
                payment["amount"],
                payment.get("currency", "ZAR"),
                payment["recipient"]
            )
            results.append(result)
        return results
    
    def execute(self, task, params):
        if task == "process_payment":
            return self.process_payment(
                params.get("amount"),
                params.get("currency", "ZAR"),
                params.get("recipient")
            )
        elif task == "distribute_payments":
            return self.distribute_payments(params.get("payments"))
        else:
            raise ValueError(f"Unknown task: {task}")
