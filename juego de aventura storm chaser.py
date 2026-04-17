print("ADVERTENCIA:TORNADO F5 EN CURSO")
print("Te despiertas en tu auto a la orilla de una carretera de Oklahoma")
print("Las sirenas suenan y el cielo se oscurese. Un tornado gigante se dirige hacia ti")
print("Tienes muy poco tiempo. ¿Que haces primero?")
p1 = input("Escribe ARRANCAR el auto,BUSCAR un sotano o REZAR: ").lower()
if p1 == "arrancar":
    print("\nMetes turbo. El viento empieza a sacudir tu auto")
    print("Ves que el tornado bloquea la salida principal.¿Por donde escapas?")
    p2 = input("Escribe BOSQUE,PUENTE o PRADERA: ").lower()
    if p2 == "bosque":
        print("\nLos arboles empiezan a caer como fosforos a tu alrededor")
        print("¿Que haces? ¿ACELERAR a ciegas,SALIR del carro o CUBRIRTE la cabeza?")
        p3 = input("Escribe ACELERAR,SALIR o CUBRIRTE: ").lower()
        if p3 == "acelerar":
            print("\nLograste salir del bosque justo antes de que un pino aplastara tu auto sobreviviste.FIN.")
        elif p3 == "salir":
            print("\nERROR FATAL. Una rama te golpeo y moriste")
        elif p3 == "cubrirte":
            print("\nTu auto quedo enterrado en troncos,pero estas a salvo. Un rescate vendra por ti.FIN.")
        else:
            print("El panico te gano y moriste.")
    elif p2 == "pradera":
        print("\nEstas en campo abierto. El tornado se vuelve un 'wedge' gigante detras de ti")
        print("Ves tres caminos: uno de TIERRA,ASFALTO y LODO.")
        p4 = input("Escribe TIERRA,ASFALTO o LODO: ").lower()
        if p4 == "asfalto":
            print("\nLa velocidad es maxima,dejas atras al mounstruo de viento. Acabas de escapar de el tornado.FIN.")
        elif p4 == "tierra":
            print("\nEl polvo te nubla la vista y chocas con una cerca. EL tornado te alcanzo y moriste.")
        elif p4 == "lodo":
            print("\nEl auto se atasca. Ves el embudo acercandose a ti y al tocar el lodo se disipa,te salvaste.FIN.")
        else:
            print("Te quedaste mirando el retrovisor y moriste")
    else:
        print("El puente colapso por la fuerza del viento y moriste.")
elif p1 == "buscar":
    print("\nEncuentras una vieja granja abandonada. El ruido es como el de un tren de carga")
    print("Ves una TRAMPILLA de hierro,un establo de MADERA y un camion OXIDADO")
    p5 = input("Escribe HIERRO,MADERA o OXIDADO: ").lower()
    if p5 == "hierro":
        print("\nEs un refugio anti tornados. Esta oscuro y huele a humedad")
        print("¿Que haces adentro? ¿Cerrar con CANDADO,encender la LUZ o esperar en SILENCIO?")
        p6 = input("Escribe CANDADO,LUZ o SILENCIO: ").lower()
        if p6 == "candado":
            print("\nEl tornado paso por arriba pero por el candado ni te movistes. Estas vivo.FIN.")
        elif p6 == "luz":
            print("\nLa luz atrajo a unas serpientes que vivian ahi,saliste corriedo al tornado y moriste.")
        elif p6 == "silencio":
            print("\nEscuchaste como el tornado se llevaba la casa de arriba. Estas vivo.FIN.")
        else:
            print("El miedo te paralizo y moriste")
    elif p5 == "madera":
        print("\nEl establo sale volando en segundos. Te sujetas de una viga")
        print("¿Decides SOLTARTE,AGUANTAR o GRITAR por ayuda?")
        p7 = input("Escribe SOLTARTE,AGUANTAR o GRITAR: ").lower()
        if p7 == "aguantar":
            print("La viga estaba anclada al suelo. Sobreviviste.FIN.")
        elif p7 == "soltarte":
            print("Volaste por 2 kilometros en el aire y moriste en la caida.")
        elif p7 == "gritar":
            print("nadie te escucho debido al sonido de los vientos del tornado te frustras y aceptas tu destino. Moriste.FIN")
        else:
            print("Te dio un ataque de panico y mueres por el tornado")
    else:
        ("El camion era muy ligero y el viento se llevo contigo. Moriste.FIN")
else:
    print("Te quedaste impresionado por la belleza del fenomeno y moriste.")