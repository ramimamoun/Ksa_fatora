from fatoora import Fatoora
from datetime import datetime

# fatoora_obj = Fatoora(
#     seller_name="Awiteb",
#     tax_number=1234567891, # or "1234567891"
#     invoice_date=1635872693.3186214, # timestamp or datetime object, or string ISO 8601 Zulu format
#     total_amount=100, # or 100.0, 100.00, "100.0", "100.00"
#     tax_amount=15, # or 15.0, 15.00, "15.0", "15.00"
# )
#
# print(fatoora_obj.base64)
x = datetime.now()
# print(x)
fatoora_obj = Fatoora(
    seller_name="rami",
    tax_number=123456789111111,
    invoice_date=x,
    total_amount=100,
    tax_amount=15,
)

fatoora_obj.qrcode("qr_code.png")

# fatoora_obj = Fatoora(
#     seller_name="Awiteb",
#     tax_number=1234567891,
#     invoice_date=1635872693.3186214,
#     total_amount=100,
#     tax_amount=15,
#     qrcode_url="https://example.com"
# )
#
# fatoora_obj.qrcode("qr_code_with_url.png")