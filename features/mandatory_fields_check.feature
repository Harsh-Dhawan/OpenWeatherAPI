Feature: OpenWeatherApi works but only with Mandatory Parameters
  Scenario Outline: validate that presence of one mandatory field "<provided_parameter>" is not enough as "<missing_parameter>" is missing
    Given Base URL for OpenWeatherApi is provided
    When GET request is made with only 1 parameter "<provided_parameter>" with value "<parameter_value>"
    Then Status code should be "<error_code>"
    Examples:
    |provided_parameter|parameter_value|missing_parameter|error_code|
    |id                |5128581        |appid            |401       |
    |appid             |2976d3cc5649f3bf135824f4016e671d |id |400   |