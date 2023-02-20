
# Duelo épico

Esta es una historia de una de esas gestas que merecen ser narradas. Una justa medieval entre las dos mejores unidades a caballo del juego: El paladín y el leitis. Vamos a ver paso a paso cómo sería esta cruenta batalla a través de datos y veremos quien se llevaría el trofeo de monedas de oro, los bitcoins de la época. 


![Image text](/imagenes/u_leitis.png)
![Image text](/imagenes/u_paladin.png)




[recursos necesarios](https://public.tableau.com/app/profile/rub.n3099/viz/AgeOfEmpiresdasghpvsl1/Hoja11?publish=yes)


Lo primero que podemos observar es que la cantidad de recursos que se necesitan para la creación de cada unidad es distinto. Siendo el paladín el más caro en cuanto a oro, hace más dificil masificar la unidad en grandes cantidades y tener una limitación en lategame. Pero vamos a seguir investigando si merece la pena


[primeras diferencias](https://public.tableau.com/app/profile/rub.n3099/viz/AgeOfEmpiresdasghpvsl2/Hoja11?publish=yes)

En este gráfico empezamos a dislumbrar las diferencias entre las dos unidades. La defensa es mucho menor en el leitis. Aunque el ataque es muy parecido, la vida es mayor en el paladín. Sólo en la velocidad el leitis obtiene una pequeña ventaja, que haría que si hubiese una persecución en la que el paladín tuviera menos vida y no pudiese encararla, la huida no sería una opción. Al contrario, el leitis siempre puede huir del paladín. Siendo eso una gran ventaja si se decidiese no encarar la pelea.


[posibilidades de huida](https://public.tableau.com/app/profile/rub.n3099/viz/AgeOfEmpiresdasghpvsl3/Hoja13?publish=yes)

Aquí vemos como tanto la linea de visión como la punteria son la mismas. La linea de visión es bastante baja, por lo que en una persecución como hemos dicho anteriormente que podria suceder, no sería dificil perder la visión del enemigo lo que haría que no se pudiese seguir. La punteria de ataque es 100, no fallan golpes.

[tiempo de recarga de ataque](https://public.tableau.com/app/profile/rub.n3099/viz/AgeOfEmpiresdasghpvsl5/Hoja14?publish=yes)


Ambas unidades tienen el mismo tiempo de recarga para volver a atacar. Vamos a hacer un pequeño programa que calcule cuanto tiempo tardaría un paladín en matar a un leitis en condición de enfrentamiento 1 vs 1 con los datos que sabemos. Esa funcion sería la siguiente:

def paleitis():

    vidal = 100
    vidap = 160
    atackl = 13
    atackp = 14
    defensal = 1
    defensap = 2
    golpes = 0

    while (vidal > 0) and (vidap > 0):
        vidal -= (atackp - defensal)
        vidap -= (atackl - defensap)
        golpes += 1
    
    temp = golpes * 1.9
    print (vidap, vidal, golpes, temp)

paleitis()


Da como resultado 72 -4 8 15,2. Siendo 72 los puntos de vida a los que se quedaría el paladín (menos de la mitad) y 8 los golpes necesarios para matarlo, lo que equivale a 15,2 segundos de batalla sabiendo que cada ataque dura 1'9 segundos. Vamos a ver cómo de interesante es eso a continuación....


[tiempo de creación](https://public.tableau.com/app/profile/rub.n3099/viz/AgeOfEmpiresdasghpvsl7/Hoja15?publish=yes)

Estos tiempos de creación hacen que como es mas barato el leitis y su tiempo sea menor, puede ser que se pueda acumular suficientes leitis para ganar a los paladines. 
Eso sería posible de averiguar creando clases en un programa de python que se fuesen sumando cada x numeros de ataque (que sería el medidor de tiempo). Sería el siguiente paso para este proyecto, que concluye con la victoría de un paladín que se tendrá que recurperar de sus heridas con una buena jarra de hidromiel



![Image text](/imagenes/age_of_empires_2_paladin_by_samo94-da3blcl.jpg)
