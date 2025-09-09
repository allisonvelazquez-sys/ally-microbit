import xgo
import ai
import time

# Inicializamos el XGO y la AI-Lens
xgo.init()
ai.init()

# Activamos el modo de detección de pelotas en la AI-Lens
ai.switch_function("Ball")

print("LOG: XGO listo para seguir la pelota. ¡Mueve una pelota frente a la lente!")

while True:
    # Obtenemos los datos de la pelota
    ball_data = ai.get_ball_data()

    # Si se detecta una pelota
    if ball_data:
        # Extraemos la posición X de la pelota
        x_pos = ball_data.get("x")
        
        # Definimos el centro de la pantalla (aproximadamente)
        center_x = 160 # El rango de la lente es de 0 a 320 en X

        # Si la pelota está a la izquierda del centro
        if x_pos < center_x - 20: # Usamos un pequeño "rango muerto" para que no gire todo el tiempo
            xgo.turn_left(20) # Gira a la izquierda
            print(f"LOG: Pelota a la izquierda (X={x_pos}), girando izquierda.")
        # Si la pelota está a la derecha del centro
        elif x_pos > center_x + 20:
            xgo.turn_right(20) # Gira a la derecha
            print(f"LOG: Pelota a la derecha (X={x_pos}), girando derecha.")
        # Si la pelota está en el centro
        else:
            xgo.stop() # Se detiene si está centrada
            print(f"LOG: Pelota en el centro (X={x_pos}), deteniendo giro.")
    else:
        # Si no se detecta ninguna pelota, el robot busca girando lentamente
        xgo.turn_left(10) # Gira suavemente para buscar
        print("LOG: No se detecta pelota, buscando...")
    
    time.sleep(0.1) # Pequeña pausa para no sobrecargar el robotdef on_forever(): 
    pass
basic.forever(on_forever)
