Feature: OpenWeatherApi returns multiple predictions at difference of 4 hours
  Scenario: OpenWeatherApi returns 40 Prediction
    Given OpenWeatherApi response
    When We count number of predictions in response
    Then Number of predictions should be 40