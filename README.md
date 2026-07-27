# Pydantic AI | Your First Typed AI Agent

Your first real AI agent, built the type-safe way. Using Pydantic AI, the agent framework from the team behind Pydantic, you build a support-ticket triage agent whose answers are validated Python objects instead of loose strings you parse and hope over. You write static and dynamic system prompts, define a Pydantic output model that the framework validates and automatically retries when the model gets it wrong, and grow that model into enums and nested types that actively steer the LLM. Then you give the agent its first tool with injected dependencies, add token-usage visibility, write offline tests that never touch the API, and ship a small CLI that triages real tickets end to end.

Built step-by-step with [KhwajaLabs Build](https://khwajalabs.com).

## Stack
- Python
- Pydantic AI
- Pydantic
- OpenAI API
