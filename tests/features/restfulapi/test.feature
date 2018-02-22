Feature: Test feature

  Background: Set base url and headers
    Given I set base URL to "context.base_url"
    And I set "Accept" header to "application/json"

  @test
  Scenario: Test scenario to get hello world
    When I make a GET request to "blueprint/helloworld"
    Then the response status code should equal 200
    And the response status message should equal "OK"
    And the response header "Content-Type" should equal "application/json"
    And the response parameter "hello" should equal "world"
