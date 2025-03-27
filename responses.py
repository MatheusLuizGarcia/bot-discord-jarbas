from random import choice

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()
    match lowered:
        case '':
            return 'Você não disse nada...'
        case 'alo' | 'alô':
            return 'alo!!!'
        case 'coinflip' | 'cara ou coroa':
            return choice(['cara','coroa'])
        case _:
            raise NotImplementedError('Chamada não implementada ainda!')