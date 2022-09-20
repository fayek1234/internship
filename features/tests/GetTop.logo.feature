# Created by khizi at 9/19/2022
Feature: Test Scenario for GetTop logo

    Scenario: Verify that GetTop logo is clickable and takes to the home page
    Given open GetTop page
    When click the logo sign
    Then  verify logo is clickable
