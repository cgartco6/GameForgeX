class PaymentProcessor:
    def __init__(self):
        # In a real implementation, this would connect to payment gateways
        self.currencies = ["ZAR", "USD", "EUR", "GBP"]
        print("Payment Processor initialized")
    
    def validate_currency(self, currency):
        return currency in self.currencies
    
    def validate_amount(self, amount):
        return amount > 0
    
    def can_process(self, amount, currency, recipient):
        return (
            self.validate_currency(currency) and 
            self.validate_amount(amount) and 
            bool(recipient)
