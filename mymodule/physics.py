EARTH_GRAVITY = 9.80665  # normální pozemské tíhové zrychlení (m/s^2)
MOON_GRAVITY = 1.625  # měsíční gravitace (m/s^2)
SPEED_OF_LIGHT = 299792458  # rychlost světla ve vakuu (m/s)
SPEED_OF_SOUND = 343  # rychlost zvuku při teplotě 20 °C v suchém vzduchu (m/s)


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

