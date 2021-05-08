import os
from dotenv import load_dotenv
load_dotenv()

TELEGRAM_API_ID = int(os.getenv("TELEGRAM_API_ID"))
TELEGRAM_API_HASH = os.getenv("TELEGRAM_API_HASH")

# source chat id as key and destination chat ids as value
COMBINATIONS = {
    -1001201589228: {
        "whitelists": ['chat 1'],
        "blacklists": ["black"],
        "destinations": [-1272396111]
    },

   
}
