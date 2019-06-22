@use-contexts.minimal
Feature: Create conversations

  Scenario: title is required
    Given I'm authenticated as test-user-1-justin
    When I start a conversation without title
    Then It fails, telling me I must provide a title

  Scenario: text is required
    Given I'm authenticated as test-user-1-justin
    When I start a conversation without text
    Then It fails, telling me I must provide text

  Scenario: topics required
    Given I'm authenticated as test-user-1-justin
    When I start a conversation without topics
    Then It fails, telling me I must provide topics

  Scenario: Anonymous posting fails
    Given I'm not authenticated
    When I start a conversation
    Then It fails, telling me I must log in

  Scenario: Identified posting
    Given I'm authenticated as test-user-1-justin
    When I start a conversation
    Then My new post is created
    And The author id is "test-user-1-justin"
    And The author display name is "Justin Test"
