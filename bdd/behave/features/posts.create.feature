Feature: Create posts

  Scenario: data is required
    When I make a new post with no title and which is not a reply
    Then It fails, telling me I must provide more data

  Scenario: Anonymous posting
    # This scenario is specific to the current prototype, and will not be part
    # of the actual product later, as we plan to require login before posting.
    # However, for now there's no auth, so we just allow posters to identify
    # themselves free-form.
    When I make a new post and don't provide an author name
    Then My new post is created
    And The author display name is "Anonymous Coward"

  @use-contexts.simple-conversation
  Scenario: Identified posting
    # Since there's no auth yet, this is currently faked by the test suite by
    # looking up the user in the context and passing in the correct
    # authorDisplayName.
    Given I'm authenticated as test-user-2-bob
    When I make a new post
    Then My new post is created
    And The author display name is "Bob Yorankel"
