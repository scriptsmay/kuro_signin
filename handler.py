import schedule
import time

from main import sign_in

# 每天9点执行签到
schedule.every().day.at("09:00").do(sign_in)

while True:
    #schedule.run_pending()
    schedule.run_pending()

    time.sleep(1)