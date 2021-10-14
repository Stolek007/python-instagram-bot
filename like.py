import config

session = config.get_session()
session.login()

session.set_relationship_bounds(enabled=True, max_followers=10000, max_following=1000)

session.set_user_interact(amount=3, randomize=True, percentage=100, media='Photo')
session.like_by_tags(config.LIKE_TAGS, amount=config.LIKE_AMOUNT)
session.set_do_comment(True, percentage=50)
session.set_comments(config.COMMENTS)

session.end()
