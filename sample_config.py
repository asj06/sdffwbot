#----------------------------------- https://github.com/m4mallu/clonebot --------------------------------------------#
import os
import logging
from logging.handlers import RotatingFileHandler

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            "clonebot-ui.txt",
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):

    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "1856869634:AAHu041wTYiiONQn93lZSonbxJ5NrXxivg8")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", "5376206"))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "ec83821f3c5f1202d8be508e2c925586")

    # Generate a user session string
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "AQDF2fmqD4aEb4RbOPNMYHQrczMy_sMqWrot176DoJqFX-zWJ-P5Xm86JZ72qVJa4YC_xQTRJCYs2fDjdw1YphWYkY6wahQWBm7MYNwUCCkVDtBDoy5T4VzpBuwurKvf_1km3yVzlM8RFMXiLG_2L1lKTjOp2tB8gW5xf-ZAn7aPMN4Ec4kWNfYuw9FpqEKyCTiaEGVND7nzeMEQ8RoqZIIKu1_q899hr2V6UvgTqc9fuZRjq5F1pV2uxPjXFIgO97XUILPywS1M26bHrDRfelEJYzdo4JmPbb31WuCLuzoSbH4Itimxq3H2t9pg7VxwBxf5JDugIvpKlPewBwDWRZQYYbDWVAA")

    # Database URI
    DB_URI = os.environ.get("DATABASE_URL", "postgres://cxclkvqdcuyiye:db4f43e2c814129073ea93a295ddf4eff55f8e91a2011859cae5cb030a4c8177@ec2-54-205-248-255.compute-1.amazonaws.com:5432/dlo8c4m0l58ng")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
