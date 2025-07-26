import os
from dotenv import load_dotenv

load_dotenv()

PRIVATE_KEY = os.getenv("PRIVATE_KEY")
FOLLOWED_WALLET = os.getenv("FOLLOWED_WALLET")
AMOUNT = os.getenv("AMOUNT_PER_TRADE")

print("🤖 CopyTrader 启动")
print(f"📡 正在跟随地址：{FOLLOWED_WALLET}")
print(f"💰 每笔交易投入：{AMOUNT} SOL")


