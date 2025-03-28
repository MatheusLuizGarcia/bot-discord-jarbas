from random import choice
from query_google import google_search_summary

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()
    command: str = lowered.split(" ", 1)
    print(lowered)
    match command[0]:
        case '':
            return 'Você não disse nada...'
        case '!alo' | '!alô':
            return 'alo!!!'
        case '!coinflip' | '!caraoucoroa':
            return choice(['cara','coroa'])
        case '!pesquisa':
            search: str = command[1] if len(command) > 1 else ''
            if search != '':
                return google_search_summary(search)
            else:
                return 'Informe algo para pesquisar!'
        case _:
            raise NotImplementedError('Chamada não implementada ainda!')