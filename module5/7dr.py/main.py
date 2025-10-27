from email.mime.text import MIMEText
from aiosmtplib import SMTP
import asyncio

sender = 'madi.ismail2108@gmail.com'
password = 'yvrf yker vpii pskx'

receivers= [
    'masturakayumova02@gmail.com'
    ]

html = """
<h2>Mommy its me!
darsm soat 20:20mada tugaydi</h2>
<p><b>SMTP</b> orqali yuborildi.</p>
"""

message = MIMEText(html,'html')

async def send(receivers):
    mgs=MIMEText(html,'html')
    mgs['subject']='Python SMTP Test'
    mgs['from']=sender
    mgs['to']=receivers

    server = SMTP(hostname="smtp.gmail.com", port=587, start_tls=True)
    await server.connect()
    await server.login(sender, password)
    await server.send_message(mgs)
    await server.quit()

    print(f"{receivers} ga yuborildi")

async def main():
    tasks = [send(r) for r in receivers]
    await asyncio.gather(*tasks)
    
asyncio.run(main())

