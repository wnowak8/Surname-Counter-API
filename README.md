# Surname Information API

This API provides endpoints to retrieve information about surnames based on gender. It utilizes the Flask framework to handle HTTP requests.

## Requirements

- Python 3.x
- [https://github.com/wnowak8/Surname-Counter-API/blob/main/requirements.txt]() (install using `pip install -r requirements.txt`)

## Source

[Ministerstwo cyfryzacji - gov.pl](https://dane.gov.pl/pl/dataset/568,nazwiska-wystepujace-w-rejestrze-pesel)

## Usage

1. Ensure you have the necessary dependencies installed.

2. Navigate to the directory containing the docker-compose.yml file.

3. Open a terminal and execute the following command to start the container:

```bash
docker-compose up -d
```

This command will build the container based on the Dockerfile and run it in the background (-d).
Once the command is executed, the container will be running, and the API will be accessible at http://localhost:5000.
You can now use the API by connecting to http://localhost:5000 from any HTTP client or web browser.

4. Use an HTTP client (e.g., cURL, Postman) to send POST requests to the `/surname` endpoint with the following JSON payload:
```bash
{
"gender": "F", // 'F/f' for female, 'M/m' for male
"surname": "Smith"
}
```
5. The API will return a JSON response with information about the provided surname based on the specified gender.

6. You can also access the root endpoint `http://localhost:5000/` to receive a welcome message.

## Endpoints

- `GET /`: Returns a welcome message to check if server is running.

- `POST /surname`: Retrieves information about a surname based on gender. Requires a JSON payload with the "gender" and "surname" fields.

## Functionality

The API utilizes the following function:

- `get_surname_info(gender: str, surname: str) -> str`: Retrieves information about the given surname and gender.

## GitHub Actions

This project utilizes three GitHub actions to automate various tasks within the repository. Below is a brief description of each action:

### Continuous Integration (CI)

The Continuous Integration (CI) action runs whenever changes are made to the repository. It employs tools such as code linters, unit tests, and static analyzers to validate code correctness and project quality. If any issues are detected, the CI action provides relevant feedback, allowing for quick issue resolution.

### Docker Image Build

The Docker Image Build action is responsible for automatically building a Docker image based on the Dockerfile in the project. The image is built whenever changes are made to the Dockerfile or the source code. This ensures an up-to-date image of the application that can be deployed to production servers or other environments.

### Unit Tests

The Unit Tests action performs automated unit testing of the application. After each push to the main branch or the opening of a pull request to the main branch, this action executes a set of tests that verify their individual correctness. Unit tests help ensure that individual components of the application work as intended and can catch any bugs introduced during development.

### Functional Tests

The Functional Tests action performs functional testing of the application. After each push to the main branch or the opening of a pull request to the main branch, this action executes a set of tests that verify the correct functionality of the application. Functional tests ensure that the application meets specified requirements and functions as expected.

## License

This API is licensed under the MIT License. See the [LICENSE](https://opensource.org/license/mit/) file for details.