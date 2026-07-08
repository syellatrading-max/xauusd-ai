from discord_webhook import DiscordWebhook
from config import DISCORD_WEBHOOK

def send_signal(signal):

    message = f"""
🚨 AI XAUUSD SIGNAL

Signal : {signal['signal']}

Entry : {signal['entry']}

Stop Loss : {signal['sl']}

Take Profit : {signal['tp']}
"""

    webhook = DiscordWebhook(
        url=DISCORD_WEBHOOK,
        content=message
    )

    webhook.execute()
