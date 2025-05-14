Feature: registration

  Scenario:register the user
    Given I have given payload type "generate-user-password"
    When  I send a request to register the user
    Then User should registered successfully
    And Save register user data in yaml file

  Scenario:register the user without password
    Given I have given payload type "generate-username"
    When  I send a request to register the user
    Then User should get "Missing password" as response

  Scenario Outline:valid registered users
    When I have send a request to login with valid users "<username>" and "<password>"
    Then I will get "<response_message>" message as response

  Examples:
     | username     | password   | response_message     |
      | mrobinson        | (sDNKxvX42     | Login successful     |
      |  ycarter       | z*2EYC7r^2   | Login successful     |

