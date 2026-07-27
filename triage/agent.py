from datetime import datetime, timezone

from pydantic_ai import Agent, RunContext

from triage.deps import TriageDeps
from triage.models import TicketTriage

SYSTEM_PROMPT = """\
You are a support-ticket triage assistant for a small e-commerce shop.
Read the customer's message and decide what it is about, how urgent it
is, and what the support team should do first.
Be factual. Never invent order numbers or account details.
"""

agent = Agent(
    'openai:gpt-5',
    system_prompt=SYSTEM_PROMPT,
    output_type=TicketTriage,
    deps_type=TriageDeps,
    retries=2,
)


@agent.system_prompt
def add_current_time() -> str:
    # Evaluated on every run, not at import time.
    now = datetime.now(timezone.utc)
    return f'The current UTC time is {now:%Y-%m-%d %H:%M}.'


@agent.tool
def customer_profile(ctx: RunContext[TriageDeps]) -> str:
    """Look up the customer who filed this ticket: plan and open orders."""
    customer = ctx.deps.lookup()
    if customer is None:
        return 'No account found for this email.'
    return (
        f'{customer.name} <{customer.email}> is on the {customer.plan} plan '
        f'with {customer.open_orders} open order(s).'
    )
