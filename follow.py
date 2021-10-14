import config

session = config.get_session()
session.login()

session.set_relationship_bounds(enabled=True, max_followers=10000, max_following=1000)

if config.FOLLOW_TYPE == 2:
    session.set_user_interact(amount=config.FOLLOW_LIKES_AMOUNT, randomize=True, percentage=50, media='Photo')
    session.follow_user_followers(config.FOLLOW_USER_FOLLOWERS, amount=config.FOLLOW_AMOUNT, randomize=True, interact=True)
elif config.FOLLOW_TYPE == 1:
    session.follow_by_tags(config.FOLLOW_TAGS, amount=config.FOLLOW_AMOUNT, skip_top_posts=True, media='Photo')

session.end()
