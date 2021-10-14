import config

session = config.get_session()
session.login()

session.set_relationship_bounds(enabled=True, max_followers=10000, max_following=1000)

session.story_by_tags(config.WATCH_STORY_TAGS)

session.end()
