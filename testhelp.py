from __future__ import annotations
import argparse
import logging
import sys

#!/usr/bin/env python3
"""
Dummy script for tests: provides a small, testable function and a CLI.
Save as /home/andy/DevOps-Course-Bank-API/testhelp.py
"""


def dummy_task(name: str = "world") -> str:
    """Return a simple greeting (pure function, easy to unit-test)."""
    return f"Hello, {name}!"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Dummy script for tests")
    parser.add_argument("-n", "--name", default="world", help="Name to greet")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")
    parser.add_argument("--version", action="version", version="dummy 0.1")
    args = parser.parse_args(argv)

    logging.basicConfig(level=logging.DEBUG if args.verbose else logging.INFO, format="%(message)s")
    logging.debug("Running dummy_task with name=%s", args.name)

    print(dummy_task(args.name))
    return 0


if __name__ == "__main__":
    sys.exit(main())