# payment.py

class IDatabase:
    """Interface định nghĩa hợp đồng cho Database."""
    def update_status(self, order_id, status):
        raise NotImplementedError

class IEmailService:
    """Interface định nghĩa hợp đồng cho dịch vụ Email."""
    def send(self, recipient, message):
        raise NotImplementedError

class PaymentProcessor:
    """Lớp xử lý thanh toán với Dependency Injection."""
    def __init__(self, database: IDatabase, email_service: IEmailService):
        self.database = database
        self.email_service = email_service

    def process(self, order_id: int, amount: float) -> bool:
        if amount <= 0:
            return False
        
        # Thực thi logic qua các Interface (Seam)
        self.database.update_status(order_id, "PAID")
        self.email_service.send("customer@example.com", f"Order {order_id} paid.")
        return True