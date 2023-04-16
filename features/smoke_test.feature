Feature: OpenWeatherAPI is always up and running
  @SmokeTest @High
  Scenario: Smoke Test OpenWeatherAPI to Validate Service is up
    Given OpenWeatherApi response
    Then Response Code shall be 200
    and response is not empty