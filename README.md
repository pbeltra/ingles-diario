# 🇺🇸 Inglés diario

App sencilla para practicar inglés todos los días, hecha para Pablo.

**Abrir:** https://pbeltra.github.io/ingles-diario/

## Qué hace
- **Inicio:** si ya practicaste hoy, tu racha 🔥 y un calendario de tus días de práctica.
- **Practiqué hoy:** marca el día y envía un “HECHO” (se abre GitHub para crear el aviso) para que Ingles lo registre.
  Formato del título: `HECHO AAAA-MM-DD · <tipos> · N tarjetas`.
- **Tarjetas:** las **1000 palabras más usadas del inglés hablado**, en orden de frecuencia. Escuchas la palabra, piensas qué significa y tocas para ver el español con una frase corta.
  - Te calificas con *Lo sabía / Casi / No lo sabía*. Las que te cuestan vuelven pronto (una sola vez más en la misma sesión, unas tarjetas después) y las que sabes vuelven más tarde (repaso espaciado, sistema Leitner: 1, 2, 4, 7, 14 y 30 días).
  - **Ya la sé:** en una palabra nueva que ya conoces, la saltas y vuelve recién en 7 días.
  - **Palabras nuevas por día:** 10, 20 (por defecto), 30 o 50. Al terminar puedes seguir con 10 nuevas más.
  - **Modo “Solo oído”:** primero solo escuchas, sin ver la palabra.
- **Progreso:** cuántas de las 1000 ya viste, cuántas sabes, cuántas estás aprendiendo y una barra por grupos de frecuencia (1–100, 101–200…).

## Tus rutinas
- 5:00 AM: conversación en tu chat con Ingles.
- 11:59 AM: tarjetas rápidas en tu chat.
- 7:00 PM: vocabulario de oído en tu chat.

Tu avance se guarda solo en el navegador de tu teléfono.

## De dónde salen las palabras
- **Fuente:** SUBTLEX-US — Brysbaert, M. & New, B. (2009). *Moving beyond Kučera and Francis: A critical evaluation of current word frequency norms and the introduction of a new and improved word frequency measure for American English.* Behavior Research Methods, 41(4), 977–990. Frecuencias de 51 millones de palabras de subtítulos de películas y series de EE. UU. (inglés hablado). Licencia CC-BY-SA.
- **Página oficial:** https://www.ugent.be/pp/experimentele-psychologie/en/research/documents/subtlexus
- **Archivo usado:** https://www.lexique.org/databases/SUBTLEX-US/SUBTLEXus74286wordstextversion.tsv
- **Cómo se armó la lista:** se juntaron las formas de cada palabra en su forma base (is/are/was → *be*, went/going → *go*, things → *thing*) con *lemminflect*, sumando sus frecuencias; se quitaron contracciones (don't, I'm…), nombres propios, muletillas (uh, um) y groserías; se ordenó por frecuencia total. Como viene de subtítulos de películas, aparecen algunas palabras de cine (gun, kill, police).
- Significados, ejemplos y traducciones: escritos para esta app, en español neutro (Ecuador).

## Archivos
- `index.html` — la app.
- `words.json` — la lista maestra (orden, significado, ejemplo, nombre del audio). Para agregar una palabra, añade un objeto al final de `"words"`.
- `audio/w_<palabra>.mp3` y `audio/e_<palabra>.mp3` — voz en-US (Andrew), un poco lenta. Si falta un audio, la app usa la voz del navegador.
