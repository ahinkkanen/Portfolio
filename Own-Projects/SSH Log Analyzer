#!/usr/bin/env python3
import argparse
import re
import sys
from collections import Counter

FAILED = re.compile(r"Failed (?:password|publickey) for (?:invalid user )?(\S+) from (\S+)")
ACCEPTED = re.compile(r"Accepted (\w+) for (\S+) from (\S+)")


def analyze(lines):
    failed_by_ip = Counter()
    failed_by_user = Counter()
    accepted = []
    for line in lines:
        match = FAILED.search(line)
        if match:
            user, ip = match.groups()
            failed_by_ip[ip] += 1
            failed_by_user[user] += 1
            continue
        match = ACCEPTED.search(line)
        if match:
            method, user, ip = match.groups()
            accepted.append((user, ip, method))
    return failed_by_ip, failed_by_user, accepted


def print_table(title, counter, limit):
    print(title)
    if not counter:
        print("  none")
        return
    for name, count in counter.most_common(limit):
        print(f"  {name:<40} {count}")


def main():
    parser = argparse.ArgumentParser(
        description="Summarize failed and successful SSH logins from a log."
    )
    parser.add_argument("logfile", nargs="?", help="log file to read (default: standard input)")
    parser.add_argument("-n", "--top", type=int, default=10, help="rows per table (default: 10)")
    parser.add_argument("-t", "--threshold", type=int, default=5,
                        help="failed attempts before an IP is flagged (default: 5)")
    args = parser.parse_args()

    if not args.logfile and sys.stdin.isatty():
        parser.error("provide a log file or pipe log lines to standard input")

    try:
        if args.logfile:
            with open(args.logfile, encoding="utf-8", errors="replace") as log:
                failed_by_ip, failed_by_user, accepted = analyze(log)
        else:
            failed_by_ip, failed_by_user, accepted = analyze(sys.stdin)
    except OSError as error:
        print(f"Error: {error}", file=sys.stderr)
        return 2

    print(f"Failed logins: {sum(failed_by_ip.values())} from {len(failed_by_ip)} IP addresses")
    print(f"Successful logins: {len(accepted)}\n")

    print_table("Top IP addresses by failed attempts:", failed_by_ip, args.top)
    print()
    print_table("Top usernames tried:", failed_by_user, args.top)
    print()

    print("Successful logins:")
    if not accepted:
        print("  none")
    for user, ip, method in accepted[: args.top]:
        print(f"  {user:<20} {ip:<40} {method}")
    print()

    flagged = sorted(ip for ip, count in failed_by_ip.items() if count >= args.threshold)
    print(f"IP addresses with {args.threshold}+ failed attempts: {len(flagged)}")
    for ip in flagged:
        print(f"  {ip} ({failed_by_ip[ip]} failed)")

    suspicious = [(user, ip, method) for user, ip, method in accepted
                  if failed_by_ip[ip] >= args.threshold]
    if suspicious:
        print("\nWARNING: successful login from an IP with many failed attempts:")
        for user, ip, method in suspicious:
            print(f"  {user} from {ip} via {method} ({failed_by_ip[ip]} failed before or around it)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
