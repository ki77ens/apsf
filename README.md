# Page Checker

This script checks the status of multiple pages by sending HTTP requests to the provided URL concatenated with paths from a file. It utilizes the `requests` library to send GET requests and check the status code of each page.

## Usage

### Prerequisites
- Python 3
- `colorama` library (Install using `pip install colorama`)

### How to Use

1. **Clone the repository or download the script:**

    ```bash
    git clone https://github.com/ava1e/page_checker.git
    ```

2. **Run the script:**

    ```bash
    python main.py <URL> <file_path>
    ```

    Replace `<URL>` with the base URL to which you want to append paths, and `<file_path>` with the path to the file containing paths to check.

    Example:
    ```bash
    python main.py https://example.com wordlist.txt
    ```

3. **Output:**

    The script will output the status of each checked page.
    - `[ + ] PAGE FOUND - <URL>/<path>` indicates that the page exists.
    - `[ - ] PAGE NOT FOUND - <URL>/<path>` indicates that the page does not exist.
    - `FINISHED` indicates the completion of checking.

## Notes
- The script checks each path in the provided file and concatenates it to the URL to form the request.
- It evaluates the HTTP status code received from the server to determine the existence of the page.
- If the status code is not 301 (Moved Permanently) or 404 (Not Found), it considers the page to exist.
- Make sure to handle large lists of paths cautiously to avoid excessive network requests.

