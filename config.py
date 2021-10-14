from instapy import InstaPy

INSTA_NAME = 'INSTAGRAM_LOGIN'  # Инстаграм логин аккаунта
INSTA_PASSWORD = 'INSTAGRAM_PASSWORD'  # Инстаграм пароль аккаунта

LIKE_TAGS = ['']  # Теги по которым лайкать посты
LIKE_AMOUNT = 10  # Сколько постов лайкать

FOLLOW_TYPE = 1  # 1 - по тегам, 2 - по подписчикам пользователей
FOLLOW_USER_FOLLOWERS = ['']  # Никнеймы тех, чьих подписчиков учитывать
FOLLOW_TAGS = ['']  # Теги по которым подписываться
FOLLOW_AMOUNT = 10
FOLLOW_LIKES_AMOUNT = 2  # Сколько постов лайкать тем, на кого подписываюсь

WATCH_STORY_TAGS = []  # Теги по которым смотреть сторис пользователей

COMMENTS = []  # Комментарии которые будут оставляться под постами

UNFOLLOW_AMOUNT = 2000  # Кол-во отписок (невзаимных)


def get_session():
    # headless_browser=True, сделает так, чтобы не открывалась вкладка браузера
    session = InstaPy(username=INSTA_NAME, password=INSTA_PASSWORD, headless_browser=True)
    session.set_quota_supervisor(enabled=True, peak_follows_daily=800, peak_follows_hourly=60, peak_likes_daily=900,
                                 peak_likes_hourly=50, peak_unfollows_daily=800, peak_unfollows_hourly=60,
                                 peak_comments_daily=250, peak_comments_hourly=50)

    return session
