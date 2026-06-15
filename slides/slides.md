---
theme: default
title: Heineken México · Ruta Planta Tecate-Otay
class: hk-cover
fonts:
  sans: Inter
transition: fade
---

# Ruta Planta Tecate-Otay <span class="hk-star">★</span>

<div style="font-size:1.4rem;margin-top:.3rem">Análisis predictivo, prescriptivo y recomendaciones</div>
<div class="sub" style="font-size:1.1rem;margin-top:.15rem">Heineken México · Inteligencia de Negocios (AD5110) · Fase 3</div>

<div class="team">
  <div>Abel Jesús Delgado Gutiérrez <span>A01400047</span></div>
  <div>Stephania Diaz Lorenzo <span>A00397831</span></div>
  <div>Jorge Enrique Figueroa Garza <span>A00810006</span></div>
  <div>Jessica Estrada Ramírez <span>A00511956</span></div>
  <div>Luis Humberto Estrada Vigil <span>A01794287</span></div>
  <div>Alejandro Vazquez Reyes <span>A01795577</span></div>
</div>

<div class="sub" style="position:absolute;bottom:1.6rem;font-size:.92rem">Grupo 4 · Prof. Dr. Jose Alberto Chavez Luna · Mtra. Jessica Fernandez Garza · 15 jun 2026</div>

<img src="/logo_heineken.png" style="position:absolute;top:2rem;right:2.5rem;height:64px;background:#fff;padding:6px 10px;border-radius:8px"/>

---

# El problema

<div class="lg" style="margin-top:.6rem">

La operación de exportación de la ruta **Planta Tecate a Otay** presenta **retrasos e incumplimiento del plan de entrega**.

- Ruta **crítica**: trabaja en **flujo continuo**, sin almacén intermedio.
- Cualquier desviación impacta la continuidad de la cadena logística.
- Se identifica **baja confiabilidad** y **falta de control** sobre la priorización de órdenes.

</div>


---

# Las cifras del problema

<div class="kpi-row" style="margin-top:1.5rem">
  <div class="kpi"><div class="v">391</div><div class="l">órdenes analizadas<br>(6 abr a 15 may 2026)</div></div>
  <div class="kpi"><div class="v bad">69.1%</div><div class="l">órdenes con retraso<br>(270 en "Delay")</div></div>
  <div class="kpi"><div class="v bad">~6 días</div><div class="l">tiempo promedio<br>de entrega</div></div>
  <div class="kpi"><div class="v bad">223</div><div class="l">órdenes fuera de<br>secuencia FIFO</div></div>
</div>

<div class="lg" style="margin-top:1.6rem">

Además, un **desempeño desigual** entre los dos transportistas de la ruta: **Transportes 2 Caminos** y **Transportes Viento**.

</div>


---

# Tipo de datos utilizados

<div class="lg">

Extracción del sistema **SAP**. Cada registro es **una orden de embarque**.

</div>

<div class="grid grid-cols-2 gap-6" style="margin-top:.8rem;font-size:1.12rem">
<div>

**Variables principales**
- Estatus de entrega (On-Time, Delay, Pendiente)
- Tiempo de entrega (días) y tiempo en planta (horas)
- Backlog previo y cumplimiento FIFO
- SKU, tarimas y fechas de embarque y entrega

</div>
<div>

**Características**
- **391 registros**, periodicidad **diaria**
- Variables numéricas y categóricas
- **Limpieza**: registros incompletos eliminados, fechas homogeneizadas y valores validados

</div>
</div>


---

# Técnica de análisis y justificación

<div class="grid grid-cols-3 gap-4" style="margin-top:.8rem">
<div class="kpi">
<div class="l" style="font-size:.95rem"><b style="color:var(--hk-green-dark)">Descriptivo</b><br><br>Dashboard operativo con KPIs (tiempo y backlog), FODA y diagrama de Ishikawa para hallar la causa raíz.</div>
</div>
<div class="kpi">
<div class="l" style="font-size:.95rem"><b style="color:var(--hk-green-dark)">Predictivo</b><br><br><b>Promedio móvil ponderado de 7 días.</b> Suaviza la variación diaria, se alinea a la planeación semanal y pondera por volumen de órdenes.</div>
</div>
<div class="kpi">
<div class="l" style="font-size:.95rem"><b style="color:var(--hk-green-dark)">Prescriptivo</b><br><br><b>Simulación de escenarios</b> aplicada a la secuencia FIFO: compara la operación real contra un escenario con disciplina FIFO para cuantificar la mejora.</div>
</div>
</div>

<div style="margin-top:1.3rem;font-size:1.1rem">

**¿Por qué promedio móvil de 7 días?** Los coordinadores planean por semana. El horizonte de 7 días anticipa tendencias sin que un día atípico distorsione el pronóstico.

</div>


---
layout: center
---

# Resultados: análisis descriptivo

<div style="text-align:center">
<img src="/dashboard.png" class="fig" style="max-height:340px;display:inline-block"/>
</div>

<div style="margin-top:.8rem;font-size:1.05rem;text-align:center">
<b>270</b> Delay · <b>70</b> On-Time · <b>51</b> pendientes &nbsp;|&nbsp; 2 Caminos: <b>4 días</b> / backlog 3 &nbsp;·&nbsp; Viento: <b>9 días</b> / backlog 5
</div>


---

# Resultados: análisis predictivo

<div class="kpi-row" style="margin-top:.3rem;justify-content:space-between">
  <div class="kpi"><div class="v bad">89.7%</div><div class="l">pronóstico de atraso<br>(meta 63.5% · al alza)</div></div>
  <div class="kpi"><div class="v bad">4.92 días</div><div class="l">tiempo de entrega<br>(meta 4.0)</div></div>
  <div class="kpi"><div class="v bad">3.43</div><div class="l">backlog promedio<br>(meta 2.0)</div></div>
</div>

<div class="grid grid-cols-3 gap-2" style="margin-top:.7rem">
<img src="/fc_atraso.png" class="fig"/>
<img src="/fc_tiempo.png" class="fig"/>
<img src="/fc_backlog.png" class="fig"/>
</div>

<div style="margin-top:.6rem;font-size:.95rem">Tres riesgos simultáneos: <b>confiabilidad</b>, <b>eficiencia</b> y <b>control operativo</b>.</div>


---

# Análisis prescriptivo: simulación de escenarios FIFO

<div style="font-size:1.05rem;margin:.3rem 0 .7rem">

**Simulación de escenarios** sobre la secuencia FIFO: se compara la operación **real** contra un **escenario simulado** con disciplina FIFO estricta, respetando la capacidad diaria de cada transportista, sobre **340 órdenes**.

</div>

<table class="cmp">
<tr><th>Indicador</th><th>Real</th><th>Simulado (FIFO)</th><th>Mejora</th></tr>
<tr><td>Cumplimiento de secuencia FIFO</td><td class="bad">34.4%</td><td class="good">65.6%</td><td class="good">+31.2 pts</td></tr>
<tr><td>Tiempo de espera promedio</td><td class="bad">6.13 días</td><td class="good">2.15 días</td><td class="good">−64.9%</td></tr>
<tr><td>Espera promedio (Transportes 2 Caminos)</td><td class="bad">3.96 días</td><td class="good">1.99 días</td><td class="good">−49.9%</td></tr>
<tr><td>Espera promedio (Transportes Viento)</td><td class="bad">9.39 días</td><td class="good">2.40 días</td><td class="good">−74.5%</td></tr>
</table>

<div style="margin-top:.7rem;font-size:1rem">Con la disciplina FIFO, el proveedor más lento (Transportes Viento) casi iguala al mejor.</div>


---

# Hallazgos clave

<div class="lg" style="margin-top:.8rem">

- La problemática es **sistémica**: no responde a una sola causa.
- Raíces principales: **incumplimiento de FIFO**, **falta de visibilidad en tiempo real** y **variabilidad entre proveedores**.
- Casos **atípicos**: 3 órdenes con 70 días de entrega, retenidas por calidad en planta.
- Hoy la gestión es **reactiva**: se atienden los retrasos *después* de que ocurren.

</div>


---

# Recomendaciones para la empresa

<div class="lg2" style="margin-top:.5rem">

1. **Gestión FIFO disciplinada**: priorizar la entrega de órdenes más antiguas.
2. **Uso diario del dashboard**: monitorear backlog y estatus en tiempo real.
3. **Control y seguimiento por proveedor**: estandarizar el desempeño de los transportistas.
4. **Plan de depuración del backlog** acumulado.
5. **De gestión reactiva a preventiva**: anticipar los retrasos antes de que ocurran.

</div>


---

# Escenario con mejora

<table class="cmp" style="margin-top:1rem">
<tr><th>Indicador</th><th>Pronóstico actual</th><th>Meta</th><th>Con mejora</th></tr>
<tr><td>Porcentaje de atraso</td><td class="bad">89.7%</td><td>63.5%</td><td class="good">71.8%</td></tr>
<tr><td>Tiempo promedio de entrega</td><td class="bad">4.92 días</td><td>4.0 días</td><td class="good">4.0 días</td></tr>
<tr><td>Backlog promedio</td><td class="bad">3.43</td><td>2.0</td><td class="good">2.4</td></tr>
<tr><td>Órdenes fuera de FIFO</td><td class="bad">223</td><td>↓ 30%</td><td class="good">156</td></tr>
</table>

<div style="margin-top:1.1rem;font-size:1.05rem">La operación pasaría de un estado <b>crítico</b> a uno <b>en estabilización</b>.</div>


---
class: hk-cover
---

# Gracias <span class="hk-star">★</span>

<div style="font-size:1.3rem;margin-top:.6rem">Control FIFO · visibilidad diaria · seguimiento por proveedor</div>
<div class="sub" style="font-size:1.1rem;margin-top:1.2rem">Equipo 4 · Inteligencia de Negocios · Heineken México</div>

<div style="margin-top:1.4rem"><a href="guion.html" style="color:#fff;font-size:1rem;text-decoration:underline">📄 Guion completo de la narración</a></div>

<img src="/logo_heineken.png" style="position:absolute;top:2rem;right:2.5rem;height:64px;background:#fff;padding:6px 10px;border-radius:8px"/>
