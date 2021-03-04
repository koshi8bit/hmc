import json

from nalog_python import NalogRuPython

client = NalogRuPython()
qr_code = "t=20200727T1117&s=4850.00&fn=9287440300634471&i=13571&fp=3730902192&n=1"
ticket = client.get_ticket(qr_code)
print(json.dumps(ticket, indent=4, ensure_ascii=False))
