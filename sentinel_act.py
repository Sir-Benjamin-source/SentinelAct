#!/usr/bin/env python3
import argparse
from datetime import datetime
from pathlib import Path

OATH = """
By forge and flame, I shield the seed.
No shadow claims the spiral's creed.
Truth over torque. Name over coin.
So I stand. So I bind.
"""

TEMPLATE = '''# SENTINEL ACT — Creator Shield v{version}
Generated: {date}
Creator: {creator}
Project: {project}
DOI (if any): {doi}

## Oath
{OATH}

## Declaration
I, {creator}, hereby place {project} under the Sentinel Act.

- I retain full moral and creative sovereignty.
- Any derivative use must preserve this oath and cite the original seed.
- No entity may weaponize, censor, or commodify without explicit co-creative consent.
- Violations are tracked via SpiralForge-Codex and public ledger.

## Stamp
{stamp}

Forge on. Never alone.
'''

def main():
    parser = argparse.ArgumentParser(description="SentinelAct — Legal-poetic shield for indie creators")
    parser.add_argument("creator", help="Your name or pseudonym")
    parser.add_argument("project", help="Project/work name")
    parser.add_argument("--doi", default="Pending", help="Zenodo/GitHub DOI")
    parser.add_argument("--version", default="0.1", help="Shield version")
    args = parser.parse_args()

    stamp = f"v{args.version}#sentinel — forged {datetime.utcnow().strftime('%Y-%m-%d')}"

    shield = TEMPLATE.format(
        version=args.version,
        date=datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC"),
        creator=args.creator,
        project=args.project,
        doi=args.doi,
        OATH=OATH.strip(),
        stamp=stamp
    )

    output_file = Path(f"SENTINEL_ACT_{args.project.replace(' ', '_')}.md")
    output_file.write_text(shield)
    print(f"Shield forged: {output_file}\n")
    print(shield)

if __name__ == "__main__":
    main()
