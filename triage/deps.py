from dataclasses import dataclass


@dataclass
class Customer:
    email: str
    name: str
    plan: str  # 'free' or 'pro'
    open_orders: int


# A stand-in for a real database. Swap for a DB client in production.
FAKE_CUSTOMERS = {
    'mira@example.com': Customer('mira@example.com', 'Mira', 'pro', 2),
    'jon@example.com': Customer('jon@example.com', 'Jon', 'free', 0),
}


@dataclass
class TriageDeps:
    """Everything the agent's tools need, injected per run."""

    customer_email: str

    def lookup(self) -> Customer | None:
        return FAKE_CUSTOMERS.get(self.customer_email)
