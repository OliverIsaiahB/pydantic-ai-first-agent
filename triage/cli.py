import argparse
import sys

from triage.agent import agent
from triage.deps import TriageDeps
from triage.report import usage_line


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='triage',
        description='Triage one support ticket with a typed AI agent.',
    )
    parser.add_argument('email', help="The customer's account email.")
    parser.add_argument('message', help='The ticket text, quoted.')
    parser.add_argument(
        '--show-usage',
        action='store_true',
        help='Print token usage after the triage.',
    )
    args = parser.parse_args()

    deps = TriageDeps(customer_email=args.email)
    result = agent.run_sync(args.message, deps=deps)
    triage = result.output

    print(f'category : {triage.category.value}')
    print(f'priority : {triage.priority.value}')
    print(f'summary  : {triage.summary}')
    print(f'escalate : {"yes" if triage.escalate else "no"}')
    print()
    print(triage.reply.greeting)
    print(triage.reply.body)

    if args.show_usage:
        print()
        print(usage_line(result.usage()))
    return 0


if __name__ == '__main__':
    sys.exit(main())
