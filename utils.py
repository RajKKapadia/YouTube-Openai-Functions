def generate_messages(messages: list, query: str) -> list:
    formated_messages = [
        {
            'role': 'system',
            'content': 'You are a helpful assistant.'
        }
    ]
    for m in messages:
        formated_messages.append({
            'role': 'user',
            'content': m['query']
        })
        formated_messages.append({
            'role': 'system',
            'content': m['response']
        })
    formated_messages.append(
        {
            'role': 'user',
            'content': query
        }
    )
    return formated_messages
