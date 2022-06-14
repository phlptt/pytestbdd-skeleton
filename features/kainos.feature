Feature: I want to visit Kainos

  Scenario: Get in touch Kainos
    Given I visit Kainos homepage
    When I accept cookies
    When I go to get in touch
    Then I am on contact us