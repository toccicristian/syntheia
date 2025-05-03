import herramientas.datos



def entrena_funciones(trainer):
    funciones=[("me podes decir que dia es hoy?",f"Por supuesto, hoy es {herramientas.datos.obtiene_fecha()}."),
               ("que dia es hoy?",f"hoy es {herramientas.datos.obtiene_fecha()}."),
               ("que dia estamos?",f"estamos al {herramientas.datos.obtiene_fecha()}."),
               ("en cual fecha estamos?",f"estamos en el {herramientas.datos.obtiene_fecha()}."),
               ("en que dia estamos?",f"estamos en el  {herramientas.datos.obtiene_fecha()}."),
               ("me podes decir que hora es ahora?",f"Sí, ahora son las {herramientas.datos.obtiene_hora()} horas."),
               ("que hora es ahora?",f"ahora son las {herramientas.datos.obtiene_hora()} horas."),
               ("que hora tenes?",f"tengo las {herramientas.datos.obtiene_hora()} horas."),
               ("te puedo pedir la hora?",f"Sí, desde luego, ahora mismo son las {herramientas.datos.obtiene_hora()} horas."),
               ("que horas son?",f"son las {herramientas.datos.obtiene_hora()} horas.")
        ]

    i=1
    for funcion in funciones:
        trainer.train([funcion[0], funcion[1]])
        print(f"[dataset de funciones][{i}/{len(funciones)}]")
