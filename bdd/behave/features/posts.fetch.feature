Feature: Fetch posts
@use-contexts.simple-conversation

  Scenario: fetch user posts
    When I fetch all posts by test-user-1-justin
    Then I get 3 posts
  Scenario: fetch thread
    When I fetch the thread from test-post-1
    Then I get 7 posts
  Scenario: fetch partial thread
    When I fetch the thread from test-post-1 after test-post-3
    Then I get 4 posts
  Scenario: fetch by date
    When I fetch the thread from test-post-1 since 2019-05-30T16:11:50
    Then I get 3 posts
