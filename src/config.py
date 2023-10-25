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
SYVYYS = os.getenv("SYVYYS") or 8
SYVYYS_KELT = 4
SYVYYS_PUN = 7
NAYTON_KOKO = (1000,1000)
LAUTA_X = 150
LAUTA_Y = 200
LEVEYS = 700
KORKEUS = 600
REUNA = 150
HALKASIJA = 98
LISA_X = REUNA-HALKASIJA/2
FONT = "FreeSerif"
HARMAA = (128, 128, 128)
SININEN = (0,0,255)
TUMMAN_SININEN = (0,0,139)
KELTAINEN = (255, 255, 0)
PUNAINEN = (255,0,0)
MUSTA = (0, 0, 0)
TEKSTI_1_PAIKKA = (25, 5)
TEKSTI_2_PAIKKA = (25, 35)
TEKSTI_3_PAIKKA = (25, LAUTA_Y+KORKEUS+25)
VALITSE = "Valitse sarake."
