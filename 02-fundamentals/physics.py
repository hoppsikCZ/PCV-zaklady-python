'''
Konstanty v Pythonu

Konstanta je vlastně speciální typ proměnné, jejíž hodnota nemůže být změněna.
V Pythonu jsou konstanty obvykle deklarovány a přiřazovány v modulu, který bývá importován do souboru aplikace.
Konstanty jsou pojmenovány velkými písmeny a jednotlivá slova jsou oddělována podtržítky.
'''

EARTH_GRAVITY = 9.80665  # normální pozemské tíhové zrychlení (m/s^2)
MOON_GRAVITY = 1.625  # měsíční gravitace (m/s^2)
SPEED_OF_LIGHT = 299792458  # rychlost světla ve vakuu (m/s)
SPEED_OF_SOUND = 343  # rychlost zvuku při teplotě 20 °C v suchém vzduchu (m/s)

''' 
Úkol:
1. Doplňte správně hodnoty uvedených konstant.
2. Doplňte physics.py o několik výpočtových funkcí (opatřené docstrings), v nichž využijete minimálně všechny výše uvedené konstanty.
Samozřejmě můžete své řešení rozšířit i o jiné fyzikální konstanty.
3. Vytvořte z tohoto souboru samostatný modul v Pythonu podle návodu, který si sami najdete na internetu.      
4. Vytvořte vlastní aplikaci myapp.py, do níž tento modul importujte. Demonstrujte v ní na jednoduchých příkladech využití vámi
připravených funkcí.  
'''

#2
def weight_on_moon(weight):
    """
    Vypočítá hmotnost na Měsíci.
    """
    return weight / EARTH_GRAVITY * MOON_GRAVITY

def percent_of_light_speed(speed):
    """
    Vypočítá procentuální rychlost světla.
    """
    return speed / SPEED_OF_LIGHT * 100

def sound_travel_distance(time):
    """
    Vypočítá vzdálenost, kterou zvuk urazí za zadaný čas.
    """
    return SPEED_OF_SOUND * time

