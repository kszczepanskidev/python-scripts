from requests import get
from calendar import month_abbr, month_name

year = 2024
month = 5

_month_name = month_name[month]
_month_abbr = month_abbr[month]

urls = [
    f"https://images.cordial.com/102/1200x670/{_month_abbr}{year}_16x9_Multi.png",
    f"https://images.cordial.com/102/600x693/{_month_abbr}{year}_Hero_Existing.png",
    f"https://images.cordial.com/102/600x693/{_month_abbr}{year}_Hero.png",
    f"https://images.cordial.com/102/600x585/{_month_abbr}{year}_Games_Img.png",
    f"https://images.cordial.com/102/600x585/{_month_abbr}{year}_Games_Img_V2.png",
    f"https://images.cordial.com/102/600x585/{_month_abbr}{year}_Games_Img_alt.png",
    f"https://images.cordial.com/102/600x703/{_month_abbr}{year}_8Hero_Pause_DE.png",
    f"https://images.cordial.com/102/600x703/{_month_abbr}{year}_8Hero_Pause_UK.png",
    f"https://images.cordial.com/102/600x608/{_month_abbr}{year}_Games_Reminder.png",
    f"https://images.cordial.com/102/600x703/wk3_{_month_abbr}{year}_8Hero_Pause_DE.jpg",
    f"https://images.cordial.com/102/600x703/wk3_{_month_abbr}{year}_8Hero_Pause_UK.jpg",
    f"https://images.cordial.com/102/600x703/{_month_abbr}{year}_6Hero_Pause_DE.png",
    f"https://images.cordial.com/102/600x703/{_month_abbr}{year}_6Hero_Pause_UK.png",
    f"https://images.cordial.com/102/600x692/{_month_abbr}{year}_Hero_Existing.png",
    f"https://images.cordial.com/102/600x692/{_month_abbr}{year}_Hero.png",
    f"https://images.cordial.com/102/1200x670/{_month_name}{year}_16x9_Multi.png",
    f"https://images.cordial.com/102/600x693/{_month_name}{year}_Hero_Existing.png",
    f"https://images.cordial.com/102/600x693/{_month_name}{year}_Hero.png",
    f"https://images.cordial.com/102/600x585/{_month_name}{year}_Games_Img.png",
    f"https://images.cordial.com/102/600x585/{_month_name}{year}_Games_Img_V2.png",
    f"https://images.cordial.com/102/600x585/{_month_name}{year}_Games_Img_alt.png",
    f"https://images.cordial.com/102/600x703/{_month_name}{year}_8Hero_Pause_DE.png",
    f"https://images.cordial.com/102/600x703/{_month_name}{year}_8Hero_Pause_UK.png",
    f"https://images.cordial.com/102/600x608/{_month_name}{year}_Games_Reminder.png",
    f"https://images.cordial.com/102/600x703/wk3_{_month_name}{year}_8Hero_Pause_DE.jpg",
    f"https://images.cordial.com/102/600x703/wk3_{_month_name}{year}_8Hero_Pause_UK.jpg",
    f"https://images.cordial.com/102/600x703/{_month_name}{year}_6Hero_Pause_DE.png",
    f"https://images.cordial.com/102/600x703/{_month_name}{year}_6Hero_Pause_UK.png",
    f"https://images.cordial.com/102/600x692/{_month_name}{year}_Hero_Existing.png",
    f"https://images.cordial.com/102/600x692/{_month_name}{year}_Hero.png",
    f"https://images.cordial.com/102/600x592/{_month_name}{year}_Hero_launch.png",
]

for url in urls:
    r = get(url)
    if ("404 Not Found" not in r.text):
        print(url)
