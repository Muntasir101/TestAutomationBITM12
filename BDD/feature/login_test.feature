Feature: Login - Demo Opencart
  Scenario: Login functional test with valid data
    Given I launched firefox
    When I open login page
    And I enter email
    And I enter password
    And I click login
    Then Login successful