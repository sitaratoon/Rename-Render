# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "18946488")

API_HASH = os.environ.get("API_HASH", "c163d4e28e63196c3806cf3b9b2885de")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7425999899:AAGuAV6Oh7w_QsHuItN8PkxXDgqBWTFbfAk") 

FORCE_SUB = os.environ.get("FORCE_SUB", "sitaratoons") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "Sitaratoons_Rename_bot")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://ajay393798:ijwrgGv5P4sIP54h@cluster0.eqraqbm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6692613520').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
