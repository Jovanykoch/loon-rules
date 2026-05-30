#!/usr/bin/env python3
from __future__ import annotations

import ipaddress
import re
from pathlib import Path

RULES_DIR = Path(__file__).resolve().parent.parent / "rules"
RULE_TYPES = {"DOMAIN", "DOMAIN-SUFFIX", "DOMAIN-KEYWORD", "IP-CIDR", "GEOIP"}
RULE_VALUE_RE = re.compile(r"^[^\s,]+$")
GEOIP_RE = re.compile(r"^[A-Z]{2}$")


def validate_rule(rule_type: str, rule_value: str) -> str | None:
    if not rule_value:
        return "rule value is empty"

    if rule_type in {"DOMAIN", "DOMAIN-SUFFIX", "DOMAIN-KEYWORD"}:
        if not RULE_VALUE_RE.fullmatch(rule_value):
            return f"invalid rule value: {rule_value}"
        return None

    if rule_type == "IP-CIDR":
        try:
            ipaddress.ip_network(rule_value, strict=False)
        except ValueError:
            return f"invalid CIDR: {rule_value}"
        return None

    if rule_type == "GEOIP":
        if not GEOIP_RE.fullmatch(rule_value):
            return f"invalid GEOIP country code: {rule_value}"
        return None

    return f"unsupported rule type: {rule_type}"


def main() -> int:
    files = sorted(RULES_DIR.glob("*.list"))
    if not files:
        print(f"No .list files found in {RULES_DIR}")
        return 1

    errors: list[str] = []

    for file_path in files:
        for line_no, raw_line in enumerate(file_path.read_text(encoding="utf-8", errors="ignore").splitlines(), start=1):
            line = raw_line.strip()
            if not line or line.startswith("#"):
                continue

            if "," not in line:
                if any(line == rule_type or line.startswith(f"{rule_type} ") for rule_type in RULE_TYPES):
                    errors.append(f"{file_path}:{line_no}: missing comma separator")
                continue

            rule_type, rule_value = (part.strip() for part in line.split(",", 1))
            if rule_type not in RULE_TYPES:
                errors.append(f"{file_path}:{line_no}: unsupported rule type: {rule_type}")
                continue

            validation_error = validate_rule(rule_type, rule_value)
            if validation_error:
                errors.append(f"{file_path}:{line_no}: {validation_error}")

    if errors:
        print("Rule format validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"All rule files are valid ({len(files)} files checked).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
