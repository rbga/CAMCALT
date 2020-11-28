from pushetta import Pushetta
                  
API_KEY="dad789bb30df8263eb2ea9322201372d54f6c6c6"
CHANNEL_NAME="Testcamcalt"
p=Pushetta(API_KEY)
p.pushMessage(CHANNEL_NAME, "Alert - Motion Detected")
                