import re

def count_valid_emails(emails):
    if not isinstance(emails, (list, tuple)):
        return 0

    count = 0
    #define pattern for email
    EMAIL_REGEX = re.compile(
        r"^[a-zA-Z0-9._%+-]{1,64}" #pattern before the @ symbil
        r"@"
        r"[a-zA-Z0-9.-]{1,253}" #pattern after the @ symbol
        r"\.[a-zA-Z]{2,}$" #pattern for the domain's TLD
    )

    for email in emails:
        if isinstance(email, str) and len(email) <= 254:
            if EMAIL_REGEX.match(email):
                count += 1

    return count