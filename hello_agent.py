from pydantic_ai import Agent

# One model string, one instruction: a complete agent.
agent = Agent(
    'openai:gpt-5',
    system_prompt='Be concise. Answer in one short paragraph.',
)

if __name__ == '__main__':
    result = agent.run_sync('What makes a good support-ticket triage?')
    print(result.output)
