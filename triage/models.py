from enum import Enum

from pydantic import BaseModel, Field


class Category(str, Enum):
    BILLING = 'billing'
    BUG = 'bug'
    SHIPPING = 'shipping'
    HOW_TO = 'how_to'
    OTHER = 'other'


class Priority(str, Enum):
    LOW = 'low'
    MEDIUM = 'medium'
    HIGH = 'high'
    URGENT = 'urgent'


class SuggestedReply(BaseModel):
    """A draft first reply a human agent can edit and send."""

    greeting: str = Field(description='One warm sentence that names the issue.')
    body: str = Field(
        description='2-4 sentences: what we will do and what happens next.'
    )


class TicketTriage(BaseModel):
    """The triage decision for one support ticket."""

    category: Category
    priority: Priority
    summary: str = Field(
        max_length=120,
        description='One plain-English sentence a busy agent can scan.',
    )
    escalate: bool = Field(
        description='True only when a human must look at this today.'
    )
    reply: SuggestedReply
