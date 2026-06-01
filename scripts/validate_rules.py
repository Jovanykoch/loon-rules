from pathlib import Path

RULE_DIR = Path("rules")

ALLOWED_TYPES = {
    "DOMAIN-SUFFIX",
}

errors = []

for rule_file in RULE_DIR.glob("*.list"):

    seen = set()

    for line_no, line in enumerate(
        rule_file.read_text(
            encoding="utf-8"
        ).splitlines(),
        start=1
    ):

        line = line.strip()

        if not line:
            continue

        if line in seen:
            errors.append(
                f"{rule_file}:{line_no} "
                f"duplicate rule"
            )

        seen.add(line)

        parts = line.split(",", 1)

        if len(parts) != 2:
            errors.append(
                f"{rule_file}:{line_no} "
                f"invalid format"
            )
            continue

        rule_type = parts[0]

        if rule_type not in ALLOWED_TYPES:
            errors.append(
                f"{rule_file}:{line_no} "
                f"unsupported type"
            )

if errors:
    print("\n".join(errors))
    raise SystemExit(1)

print("All rules validated")