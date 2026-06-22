# test_payment.py
from unittest.mock import Mock
from payment import PaymentProcessor, IDatabase, IEmailService

def test_payment_updates_status_and_sends_email():
    """Kịch bản kiểm thử: Xác nhận luồng thanh toán thành công."""
    # Khởi tạo Mock tuân thủ Interface
    mock_db = Mock(spec=IDatabase)
    mock_email = Mock(spec=IEmailService)
    
    # Khởi tạo processor với các mock
    processor = PaymentProcessor(mock_db, mock_email)
    
    # Thực thi test
    result = processor.process(order_id=123, amount=500)
    
    # Kiểm chứng (Assertions)
    assert result is True
    mock_db.update_status.assert_called_with(123, "PAID")
    assert mock_email.send.called is True

def test_mock_behavior_expectation():
    """Kịch bản kiểm thử: Kiểm chứng hành vi tương tác qua Mock (Mục 3.3)."""
    # Khởi tạo Mock từ Interface
    mock_db = Mock(spec=IDatabase)
    mock_email = Mock(spec=IEmailService)
    
    # Thiết lập đối tượng kiểm thử
    processor = PaymentProcessor(mock_db, mock_email)
    
    # Hành động: Gọi phương thức
    processor.process(order_id=999, amount=100)
    
    # Kỳ vọng: Phương thức update_status phải được gọi đúng 1 lần với tham số cụ thể
    mock_db.update_status.assert_called_once_with(999, "PAID")
    assert mock_email.send.called is True