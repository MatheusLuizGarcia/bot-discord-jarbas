from responses import get_response
import os
from dotenv import load_dotenv

split = '!pesquisa bolo de cenoura'.split(" ",1)

command = split[0]
query = split[1]

print(command)
print(query)

# load_dotenv()

# print(os.getenv('DISCORD_TOKEN'))

# print(get_response('pesquisa discord'))