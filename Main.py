from instagrapi import Client
import time

# Instagram login
cl = Client()
cl.login("xus.a3", "sasuke1")

print("🤖 Auto-reply bot started...")

# Loop to check messages
while True:
    inbox = cl.direct_threads(amount=5)
    for thread in inbox:
        last_msg = thread.messages[0].text
        sender = thread.users[0].username

        if sender != "xus.a3":  # apne aap ko reply na kare
            reply = "Sasuke is offline right now, will reply later."
            cl.direct_send(reply, thread.users[0].pk)
            print(f"✅ Auto-replied to {sender}")

    time.sleep(30)  # har 30 sec baad check kare
