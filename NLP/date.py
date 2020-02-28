from datetime import datetime

today = datetime(year=2020,month=3,day=1)
print(f"{today:%B %d,%Y}")