from pathlib import Path

SOURCE_DIR = Path("sources")
RULE_DIR = Path("rules")

RULE_DIR.mkdir(exist_ok=True)

for source_file in SOURCE_DIR.glob("*.txt"):
    rule_name = source_file.stem
    output_file = RULE_DIR / f"{rule_name}.list"

    domains = set()

    for line in source_file.read_text(
        encoding="utf-8"
    ).splitlines():

        line = line.strip()

        # Skip empty lines
        if not line:
            continue

        # Skip comments
        if line.startswith("#"):
            continue

        domains.add(line.lower())

    with output_file.open(
        "w",
        encoding="utf-8"
    ) as f:

        for domain in sorted(domains):
            f.write(
                f"DOMAIN-SUFFIX,{domain}\n"
            )

    print(
        f"Generated {output_file}"
    )