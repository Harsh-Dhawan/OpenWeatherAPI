Feature: OpenWeatherAPI response contains CityName
  Scenario: Validate CityName & CountryName in OpenWeatherAPI response is as expected
    Given OpenWeatherAPI response
    Then City Name should be "New York"
    and Country code is "US"