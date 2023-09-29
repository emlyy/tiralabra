import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass

RIVIT = int(6)
SARAKKEET = int(7)
JARJESTYS = [3,4,2,5,1,6,0]
SYVYYS = 5