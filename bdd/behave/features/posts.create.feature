@use-contexts.minimal
Feature: Create posts

  Scenario: conversation is required
    Given I'm authenticated as test-user-1-justin
    When I make a post without a conversation
    Then It fails, telling me I must provide a conversationId

  Scenario: text is required
    Given I'm authenticated as test-user-1-justin
    When I make a post without text
    Then It fails, telling me I must provide text

  Scenario: Anonymous posting fails
    Given I'm not authenticated
    When I make a new post
    Then It fails, telling me I must log in

  Scenario: Identified posting
    Given I'm authenticated as test-user-1-justin
    When I make a new post
    Then My new post is created
    And The author id is "test-user-1-justin"
    And The author display name is "Justin Test"
