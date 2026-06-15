# Guion del video — Heineken México · Ruta Planta Tecate–Otay
**Fase 3 · Inteligencia de Negocios · Equipo 4** — duración ≈ 4:21 (narración es-MX, voz clonada)

> Estructura requerida (Paso 6): problema · tipo de datos · técnica de análisis y justificación · resultados y hallazgos · recomendaciones.

---

**1 · Portada.**
Hola, somos el Equipo cuatro de Inteligencia de Negocios. En este video presentamos la Fase tres de nuestro proyecto para Heineken México: el análisis predictivo, prescriptivo y las recomendaciones para mejorar su ruta de exportación, de la Planta Tecate a Otay, California.

**2 · El problema.**
El problema que analizamos son los retrasos e incumplimiento del plan de entrega en esta ruta. Es una operación crítica que trabaja en flujo continuo, sin almacén intermedio, por lo que cualquier desviación afecta toda la cadena logística. Detectamos baja confiabilidad y falta de control sobre la priorización de las órdenes.

**3 · Las cifras del problema.**
Las cifras lo confirman. Analizamos trescientas noventa y una órdenes embarcadas entre abril y mayo de dos mil veintiséis. El sesenta y nueve por ciento se entregó con retraso, con un tiempo promedio cercano a seis días. Además, doscientas veintitrés órdenes salieron fuera de la secuencia FIFO, y los dos transportistas mostraron un desempeño muy desigual.

**4 · Tipo de datos.**
Los datos provienen de una extracción del sistema SAP, donde cada registro representa una orden de embarque. Incluyen el estatus de entrega, el tiempo de entrega y de planta, el backlog previo, el cumplimiento de FIFO y las fechas de cada orden. Son trescientos noventa y un registros de periodicidad diaria, a los que aplicamos un proceso de limpieza para garantizar su confiabilidad.

**5 · Técnica de análisis y justificación.**
Aplicamos tres tipos de análisis. El descriptivo, con un tablero de indicadores, un análisis FODA y un diagrama de Ishikawa para hallar la causa raíz. El predictivo, mediante un promedio móvil ponderado de siete días; lo elegimos porque suaviza la variación diaria, se alinea con la planeación semanal de los coordinadores y pondera cada periodo por su volumen de órdenes. Y el prescriptivo, que traduce los pronósticos en acciones concretas.

**6 · Resultados — análisis descriptivo.**
En el análisis descriptivo, el tablero muestra que de las trescientas noventa y una órdenes, doscientas setenta se entregaron tarde, setenta a tiempo y cincuenta y una quedaron pendientes. La comparación entre proveedores es reveladora: Transportes Dos Caminos promedia cuatro días de entrega, mientras que Transportes Viento llega a nueve. Esto confirma una clara oportunidad de control por proveedor.

**7 · Resultados — análisis predictivo.**
El pronóstico para la semana del dieciséis al veintidós de mayo enciende las alertas. El porcentaje de atraso se proyecta en casi noventa por ciento, muy por encima de la meta y con tendencia al alza. El tiempo de entrega se estima en cuatro punto nueve días y el backlog en tres punto cuatro órdenes. En conjunto, la ruta enfrenta tres riesgos: de confiabilidad, de eficiencia y de control operativo.

**8 · Análisis prescriptivo — simulación FIFO.**
En el análisis prescriptivo simulamos la operación bajo una disciplina FIFO estricta, respetando la capacidad de los transportistas y del muelle compartido, sobre trescientas cuarenta órdenes. El resultado es contundente: el cumplimiento de la secuencia subiría del treinta y cuatro al sesenta y seis por ciento, y la espera promedio bajaría de seis punto uno a dos punto dos días. Transportes Viento, el proveedor más lento, pasaría de nueve punto cuatro a dos punto cuatro días, casi igualando al mejor. El límite que queda es el muelle compartido, no la disciplina de secuencia.

**9 · Hallazgos clave.**
El hallazgo principal es que la problemática es sistémica: no responde a una sola causa, sino al incumplimiento de FIFO, la falta de visibilidad en tiempo real y la variabilidad entre proveedores. Incluso encontramos casos atípicos, como tres órdenes con setenta días de entrega, retenidas por calidad. Hoy la gestión es reactiva: se atienden los retrasos después de que ocurren.

**10 · Recomendaciones para la empresa.**
Por eso, recomendamos a la empresa cinco acciones. Primero, una gestión FIFO disciplinada que priorice las órdenes más antiguas. Segundo, usar el tablero de forma diaria para monitorear el backlog en tiempo real. Tercero, establecer un control por proveedor. Cuarto, ejecutar un plan de depuración del backlog acumulado. Y quinto, evolucionar de una gestión reactiva a una preventiva.

**11 · Escenario con mejora.**
Con estas acciones, el escenario mejora de forma relevante. El porcentaje de atraso bajaría de casi noventa a setenta y dos por ciento, el tiempo de entrega alcanzaría la meta de cuatro días, el backlog se reduciría a dos punto cuatro órdenes y los incumplimientos de FIFO pasarían de doscientos veintitrés a ciento cincuenta y seis. La operación pasaría de un estado crítico a uno en estabilización.

**12 · Cierre.**
En resumen, los datos revelan una ruta con retrasos sistémicos, pero también un camino claro de mejora a través del control FIFO, la visibilidad diaria y el seguimiento por proveedor. Gracias por su atención, de parte del Equipo cuatro.
