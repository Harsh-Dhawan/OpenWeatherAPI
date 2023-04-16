Feature: openWeatherApi returns Current & feels like Temperature
  Scenario: Validate values for Current & feels like Temperature are within valid range
    Given OpenWeatherAPI response
    Then Current Temperature should be between "200" and "300"
    and feels like Temperature should be +-"20" than Current temperature