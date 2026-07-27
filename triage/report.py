def usage_line(usage) -> str:
    """One log-friendly line: tokens in, tokens out, model requests."""
    return (
        f'usage: {usage.input_tokens} in / {usage.output_tokens} out '
        f'across {usage.requests} request(s)'
    )
