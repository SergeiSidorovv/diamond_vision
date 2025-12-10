import logging
import dns.resolver


emails = [
    "user@example.com",
    "info@gmail.com",
    "test@nonexistent-domain-xyz-12345.com",
    "abc@domainwithoutmx.com",
]


def domain_exists(domain: str) -> bool:
    """Проверяет, существует ли домен (A, AAAA или CNAME)."""
    record_types = ["A", "AAAA", "CNAME"]

    for rtype in record_types:
        try:
            dns.resolver.resolve(domain, rtype)
            return True
        except dns.resolver.NXDOMAIN:
            return False
        except Exception:
            continue

    return False


def has_mx_records(domain: str) -> bool:
    """Проверяет существование MX-записей."""
    try:
        answers = dns.resolver.resolve(domain, "MX")
        return len(answers) > 0
    except Exception:
        return False


def check_email(email: str) -> str:
    """Возвращает статус домена email-адреса."""

    if "@" not in email:
        return "некорректный email"

    domain = email.split("@")[1]

    if not domain_exists(domain):
        return "домен отсутствует"

    if has_mx_records(domain):
        return "домен валиден"
    return "MX-записи отсутствуют или некорректны"


def main():
    for email in emails:
        status = check_email(email)
        print(f"{email}: {status}")


if __name__ == "__main__":
    main()