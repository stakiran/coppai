from datetime import datetime

import pyperclip

now = datetime.now()
formatted_date = now.strftime('%Y/%m/%d %H:%M:%S')
pyperclip.copy(formatted_date)
