Feature: Create conversations

  Scenario: title is required
    When I start a conversation without title
    Then It fails, telling me I must provide a title

  Scenario: text is required
    When I start a conversation without text
    Then It fails, telling me I must provide text

  Scenario: topics required
    When I start a conversation without topics
    Then It fails, telling me I must provide topics

  @use-contexts.minimal
  Scenario: Anonymous posting
    # This scenario is specific to the current prototype, and will not be part
    # of the actual product later, as we plan to require login before posting.
    # However, for now there's no auth, so we just allow posters to identify
    # themselves free-form.
    Given I'm not authenticated
    When I start a conversation
    Then My new post is created
    And The author display name is "Anonymous Coward"

  @use-contexts.minimal
  Scenario: Identified posting
    # Since there's no auth yet, this is currently faked by the test suite by
    # looking up the user in the context and passing in the correct
    # authorDisplayName.
    Given I'm authenticated as test-user-1-justin
    When I start a conversation
    Then My new post is created
    And The author display name is "Justin Test"
