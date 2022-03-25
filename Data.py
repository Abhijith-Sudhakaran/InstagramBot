from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

Welcome to {}

I can download profile pictures, videos, images and reels from instagram along with post caption.
You can also authorize me to download private posts.

Use below buttons to learn more.

By @CatBotzUpdates
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("✨ 𝘽𝙤𝙩 𝙎𝙩𝙖𝙩𝙪𝙨 𝙖𝙣𝙙 𝙐𝙥𝙙𝙖𝙩𝙚𝙨", url="https://t.me/CatBotzUpdates")],
        [
            InlineKeyboardButton("𝙃𝙚𝙡𝙥❔", callback_data="help"),
            InlineKeyboardButton("🎪 𝘼𝙗𝙤𝙪𝙩", callback_data="about")
        ],
        [InlineKeyboardButton("♥ 𝘾𝙧𝙚𝙖𝙩𝙤𝙧", url="https://t.me/Telecat_X")],
    ]

    # Help Message
    HELP = """
1) **Images, Videos and Reels**
Send the link here to get the post contents including caption.

2) **Profile Pictures**
Use the command `/profile_pic` or `/dp` along with instagram username to get its profile picture.
Example : `/dp 𝙐𝙨𝙚𝙧𝙣𝙖𝙢𝙚`

3) **Private Posts**
Authorize the bot to download private posts. Use /auth

**Note** : Stories and IGTV are not supported.

Use /auth to authorize and /unauth to unauthorize.
"""

    # About Message
    ABOUT = """
**About This Bot** 

A telegram bot to download instagram content by @CatBotzUpdates

Source Code : [Click Here](https://github.com/Abhijith-Sudhakaran)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @Telecat_X

𝙄𝙣𝙨𝙩𝙖𝙜𝙧𝙖𝙢 : [Follow Me](https://instagram.com/hypercat_ext)
    """
