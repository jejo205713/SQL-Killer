# SQL Injection Testing Script

This script is designed to test web applications for SQL injection vulnerabilities by submitting a range of payloads to the target URL. It logs responses and identifies potential vulnerabilities.

---

## Features

- **Automated Testing**: Submits a predefined list of SQL injection payloads.
- **Customizable Target**: Allows the user to specify the target URL.
- **Comprehensive Payloads**: Includes a wide variety of SQL injection payloads for extensive testing.
- **Result Logging**: Logs responses to a file for analysis.

---

## Requirements

- **Python 3.x**
- **`requests` Library**: Install using `pip install requests`.

---

## How to Use

1. Clone this repository:

    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Run the script:

    ```bash
    python sql_injection_tester.py
    ```

3. Enter the target URL when prompted.

4. Analyze the log file (`sql_injection_test_results.log`) generated in the script directory.

---

## Payloads

This script uses a comprehensive list of payloads targeting various SQL injection techniques, including:

- Single quotes (`'`)
- Double quotes (`"`)
- Logical operations (`OR`, `AND`)
- Inline comments (`--`, `/*`)
- UNION-based payloads
- Boolean-based payloads

For the full list of payloads, see the [payloads.py](payloads.py) file.

---

## Example

```bash
Enter the target URL: https://example.com/login
Testing payload: ' or 1=1--
Potential vulnerability detected with payload: ' or 1=1--
