# Created by khizi at 9/21/2022
Feature: navigate multiple pages

  Scenario: user can click through multiple product pages by clicking < and >
   When click on product image
   Then hover over left arrow
   Then click on left arrow
   Then click on right arrow 2 times