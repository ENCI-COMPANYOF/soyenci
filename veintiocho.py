def pedir_perdon():
    print("Hola, quiero pedirte disculpas...")
    nombre = input("¿Cómo te llamas? ")
    print(f"hola mi pequeña niña, {nombre}.... solo queria decir que lo lamento si no fui el mejor, solo no me gustaria perderla y lo que quiero es logra mucho contigo, no me deje con el amor en las manos... usted me importa mucho como no se imagina, no me gustaria seguir asi con usted.. vamos de poco a poco no  apresuremos las cosas y vamos lentos pero seguro mi pequeña niñaaaa TE QUIERO <3 ¿ME PERDONAS?")
    respuesta = input("¿Me perdonas? (sí/no): ")
    
    if respuesta.lower() == "sí":
        print("¡Gracias! Prometo ser mejor.")
    else:
        print("Entiendo, espero que algún día puedas perdonarme.")
if __name__ == "__main__":
    pedir_perdon()
