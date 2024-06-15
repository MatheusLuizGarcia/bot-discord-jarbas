from random import choice

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()
    if lowered == '':
        return 'Você não disse nada...'
    elif 'alo' in lowered or 'alô' in lowered:
        return 'alo!!!'
    elif 'coinflip' in lowered or 'cara ou coroa' in lowered:
        return choice(['cara','coroa'])

    # raise NotImplementedError('Chamada não implementada ainda!')