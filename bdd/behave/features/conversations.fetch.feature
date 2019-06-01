@use-contexts.many-conversations
Feature: Fetch conversations

  Scenario: conversations in a topic
    When I fetch conversations in topic "introductions"
    Then I get 2 conversations

  Scenario: conversations in an empty topic
    When I fetch conversations in topic "dev-help"
    Then I get 0 conversations

  Scenario: conversations in a topic that doesn't exist
    When I fetch conversations in topic "fnord"
    Then I get 0 conversations

  Scenario: fetch conversations after a given one
    When I fetch conversations in topic "sandbox" after test-convo-3-piyo
    Then I get 2 conversations

  Scenario: fetch conversations by date
    When I fetch conversations in topic "sandbox" since 2019-05-30T16:08:08Z
    Then I get 2 conversations
