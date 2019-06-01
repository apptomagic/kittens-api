@use-contexts.simple-conversation
Feature: Fetch posts

  Scenario: fetch user posts
    When I fetch all posts by test-user-1-justin
    Then I get 3 posts
  Scenario: fetch thread
    When I fetch the thread from test-post-1
    Then I get 7 posts
  Scenario: fetch partial thread
    When I fetch the thread from test-post-1 after test-post-3
    Then I get 4 posts
  Scenario: fetch thread by date
    When I fetch the thread from test-post-1 since 2019-05-30T16:09:09Z
    Then I get 3 posts
  Scenario: fetch conversation thread
    When I fetch the conversation thread from test-convo-1-foo
    Then I get 7 posts
  Scenario: fetch partial conversation thread
    When I fetch the conversation thread from test-convo-1-foo after test-post-3
    Then I get 4 posts
  Scenario: fetch conversation thread by date
    When I fetch the conversation thread from test-convo-1-foo since 2019-05-30T16:09:09Z
    Then I get 3 posts
