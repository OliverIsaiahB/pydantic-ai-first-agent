"""Fast, offline tests: TestModel fakes the LLM but honors the schema."""

from pydantic_ai import models
from pydantic_ai.models.test import TestModel

from triage.agent import agent
from triage.deps import TriageDeps
from triage.models import TicketTriage

# Fail loudly if any test accidentally calls a real model.
models.ALLOW_MODEL_REQUESTS = False


def test_output_is_a_valid_triage():
    deps = TriageDeps(customer_email='mira@example.com')
    with agent.override(model=TestModel()):
        result = agent.run_sync('My invoice is wrong.', deps=deps)
    assert isinstance(result.output, TicketTriage)


def test_unknown_customer_still_triages():
    deps = TriageDeps(customer_email='ghost@example.com')
    with agent.override(model=TestModel()):
        result = agent.run_sync('Where is my package?', deps=deps)
    assert isinstance(result.output, TicketTriage)
