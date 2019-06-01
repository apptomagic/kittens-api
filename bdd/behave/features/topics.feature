Feature: browse topics

# This is completely interim; currently the topics are hardcoded, so we just
# test that the protocol / server works correctly.
# topics = [
#   'chat',
#   'introductions',
#   'meta',
#   'roadmap',
#   'bugs',
#   'suggestions',
#   'help',
#   'dev-help',
#   'announcements',
#   'documentation',
#   'web',
#   'sandbox',
# ]

# related = [
#   ('bugs', 'suggestions'),
#   ('chat', 'introductions'),
#   ('roadmap', 'announcements'),
#   ('help', 'bugs'),
#   ('help', 'documentation'),
#   ('dev-help', 'documentation'),
#   ('documentation', 'web'),
# ]

  Scenario: get all topics
    When I fetch all topics
    Then I get 12 topics
  Scenario: get related
    When I fetch topics related to "documentation"
    Then I get 3 topics
