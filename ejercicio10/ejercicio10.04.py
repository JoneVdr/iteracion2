huérfanos = []
for persona in familias:
    if persona and persona.padre1 == 'HUÉRFANO' and persona.padre2 == 'HUÉRFANO' and persona.edad < 15:
        huérfanos.append(persona)
