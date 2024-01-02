# Admin panel & Subdomain finder

## Description

The "Page Checker" is a Python script designed to verify the availability and accessibility of multiple web pages or subdomains on a web server. By utilizing the `requests` library, this tool checks the existence of URLs by appending paths or subdomains to a provided base URL.

## Features

- **Multi-threaded Processing:** Employs ThreadPoolExecutor to execute multiple HTTP requests concurrently, enabling efficient checking of numerous pages simultaneously.
- **Logging:** Captures detailed information about each checked page, segregating findings into two log files (`found.log` and `not_found.log`) for future reference and analysis.
- **User-Agent Rotation:** Uses the `pyuseragents` library to randomize User-Agent headers in each request, mimicking different clients and enhancing anonymity.
- **Mode Selection:** Supports two modes of operation - `subdomains` and `links` - allowing users to check subdomains or specific paths respectively.

## Usage

### Prerequisites
- Python 3
- `colorama` library (Install using `pip install colorama`)
- `pyuseragents` library (Install using `pip install pyuseragents`)

### Running the Script

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/ava1e/apf.git
    ```

2. **Execute the Script:**

    ```bash
    python main.py <URL> <file_path> <subdomains_file> <mode: subdomains/links>
    ```

    Replace `<URL>` with the base URL, `<file_path>` with the file containing paths or links to check, `<subdomains_file>` with the file containing subdomains, and `<mode>` with either `subdomains` or `links`.

    Example:
    ```bash
    python main.py https://www.example.com links.txt subdomains.txt links
    
    python main.py example.com links.txt subdomains.txt subdomains
    ```

3. **Output:**

    The script displays the status of each checked page or subdomain. Additionally, it logs found and not found pages into separate log files and prints a `FINISHED` message upon completion.

## Notes

- Exercise caution when handling large lists of paths or subdomains to prevent excessive network requests and ensure optimal performance.
- Detailed information about each request's status is available in the generated log files (`found.log` and `not_found.log`), aiding in further analysis and review.
