# Created by khizi at 9/21/2022
Feature: Test scenario for product quick view

  Scenario: user can see close quick view
    When hover over a product
    Then click quick view
    Then close quick view by clicking on X


  Scenario: user can add product
    When hover over a product
    Then click quick view
    Then add product to cart
    Then added product text showen

