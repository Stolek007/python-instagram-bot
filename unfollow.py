import config

session = config.get_session()
session.login()

session.unfollow_users(amount=config.UNFOLLOW_AMOUNT, nonFollowers=True, style="LIFO")

session.end()
