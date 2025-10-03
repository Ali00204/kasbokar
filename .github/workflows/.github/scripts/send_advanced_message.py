
import os
import requests
import json
from datetime import datetime

def send_message():
    token = os.getenv('BOT_TOKEN')
    channel = "@your_channel_username"  # آیدی کانال خود را قرار دهید
    
    # تاریخ شمسی (می‌توانید کتابخانه jalaali را اضافه کنید)
    today = datetime.now()
    persian_date = today.strftime("%Y/%m/%d")
    
    messages = [
        {
            "text": f"""
🎯 <b>پیام هوشمند مدرسه</b>

📅 تاریخ: {persian_date}
⏰ ساعت: {today.strftime("%H:%M")}

📊 <b>برنامه امروز:</b>
• ساعت ۸:۰۰ - ریاضی
• ساعت ۱۰:۰۰ - علوم
• ساعت ۱۲:۰۰ - ورزش

✅ <b>تکالیف:</b>
- حل مسائل صفحه ۴۵ ریاضی
- مطالعه فصل ۳ علوم

💡 <i>موفق باشید دانش‌آموزان عزیز!</i>
            """,
            "parse_mode": "HTML"
        },
        {
            "text": "📚 یادگیری زیباست! امروز را با نشاط شروع کنید 🌟",
            "parse_mode": "HTML"
        }
    ]
    
    for message in messages:
        url = f"https://tapi.bale.ai/bot{token}/sendMessage"
        payload = {
            "chat_id": channel,
            "text": message["text"],
            "parse_mode": message["parse_mode"]
        }
        
        response = requests.post(url, json=payload)
        print(f"Response: {response.status_code} - {response.text}")

if __name__ == "__main__":
    send_message()
