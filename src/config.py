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
NAYTON_KOKO = (500,500)
FONT = "cmr10"
HARMAA = (128, 128, 128)
SININEN = (0,0,255)
TUMMAN_SININEN = (0,0,139)
KELTAINEN = (255, 255, 0)
PUNAINEN = (255,0,0)
MUSTA = (0, 0, 0)
TEKSTI_1_PAIKKA = (10, 5)
TEKSTI_2_PAIKKA = (10, 35)
TEKSTI_3_PAIKKA = (10, 450)
