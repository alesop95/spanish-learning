# spanish-learning

Tutor di apprendimento guidato dello spagnolo per un italofono adulto, costruito su Claude Code: roadmap pedagogica tracciata, ripasso a intervalli via Anki, una base di conoscenza locale sui libri e i materiali personali dell'utente, e un catalogo di fonti citato a ogni lezione. Non è un'applicazione software: è un sistema di agenti, script e documenti che insieme orchestrano lo studio.

---

## Architettura in breve

Il sistema segue lo standard di progetto descritto in `.claude/PROJECT-SYSTEM.md` e attiva sopra di esso il pacchetto `learning-agent`, documentato per esteso in `.claude/context/learning-agent-reference.md`. Tre livelli disaccoppiati compongono il tutor: la base di conoscenza, oggi la cache locale prodotta da `doc-ingest`, senza recupero semantico vero; il motore di memoria dell'apprendimento, `ankimcp/anki-mcp-server` una volta collegato; il livello di orchestrazione, cioè tre agenti (*tutor*, *kb-retriever*, *examiner*) e tre coppie skill più comando (`/profile`, `/learn`, `/review`) dentro `.claude/`. `CLAUDE.md` è l'indice tecnico per chi lavora al progetto; questo file è per chi lo scopre per la prima volta o vuole solo sapere come usarlo.

---

## Primo avvio

La prima cosa da fare in un progetto nuovo, o quando si vuole cambiare obiettivo o livello dichiarato, è l'onboarding del profilo di apprendimento.

```
/profile
```

Il comando raccoglie obiettivo, categoria del topic, livello di partenza, tempo disponibile per sessione, cadenza, un profilo cognitivo opt-in per adattare ritmo e formato, e le preferenze di stile, poi costruisce la roadmap pedagogica dentro `LEARNER_PROFILE.md`. Rilanciarlo in seguito aggiorna solo i campi cambiati, senza toccare i progressi già registrati.

---

## Il ciclo di studio

Le due entry point quotidiane sono `/learn` per erogare la prossima unità e `/review` per il ripasso.

```
/learn
/review
```

`/learn` verifica la roadmap in `LEARNER_PROFILE.md`, recupera dalla base di conoscenza solo gli estratti pertinenti al modulo corrente tramite il subagent `kb-retriever`, eroga la lezione secondo il template pedagogico per una lingua straniera (esposizione in contesto più produzione immediata, mai vocaboli isolati), e chiude sempre con una verifica di richiamo attivo del subagent `examiner` prima di segnare il modulo completato. `/review` interroga Anki per le carte dovute quando è collegato, o si basa sui moduli già erogati quando non lo è; per lo spagnolo offre anche un ripasso derivato da una conversazione libera, da cui vengono estratti gli errori commessi. Ogni sessione chiede quanto tempo è disponibile in quel momento, perché `session_minutes` in `LEARNER_PROFILE.md` è dichiarato variabile, e registra data, ora, durata reale e modulo coperto in `SESSION-LOG.md`: è la base con cui adattare la dimensione delle unità future al tempo che si ha davvero, non a una media presunta.

---

## La base di conoscenza locale

I libri e i documenti personali vivono fuori da git, in `_notes/raw-sources/` (compreso quanto estratto dall'archivio `libri.7z`), e vengono indicizzati in una cache Markdown a costo zero da `tools/doc-ingest.py`, senza alcuna chiamata a un modello linguistico.

```
python tools/doc-ingest.py "_notes/raw-sources"
```

Il comando cammina la cartella sorgente, converte ogni documento supportato[^1] in Markdown, e scrive il risultato sotto `_notes/.tmp-doc-cache/`, mantenendo un manifest a impronta di contenuto che evita di riconvertire i file invariati. Il file `_notes/.tmp-doc-cache/_INDEX.md` è il punto di ingresso: titolo, struttura a intestazioni e conteggi per ciascun documento, così che `kb-retriever` sappia cosa aprire senza leggere l'intero corpus. Quando un documento risulta scansionato senza testo estraibile, come è successo per un volume di questa libreria, il flag `--ocr` attiva un fallback via riconoscimento ottico dei caratteri[^2], che in questo progetto richiede anche il pacchetto lingua spagnola di Tesseract oltre a quello inglese installato di default: se `spa.traineddata` non è nella cartella di sistema, va indicata una cartella alternativa con la variabile d'ambiente `TESSDATA_PREFIX` prima di lanciare il comando.

```
python tools/doc-ingest.py "_notes/raw-sources" --ocr
```

Rilanciare l'ingestione dopo aver aggiunto nuovi documenti alla cartella sorgente è sufficiente: solo i file nuovi o modificati vengono riconvertiti.

---

## Spaced repetition con Anki

Il ripasso a intervalli usa `ankimcp/anki-mcp-server`, configurato in `.mcp.json` con il comando verificato contro la documentazione ufficiale del progetto. Prima di poterlo usare vanno installati, sulla macchina, Anki desktop e l'estensione AnkiConnect[^3], ed entrambi vanno avviati prima di far partire il server MCP, che si limita a fare da proxy verso l'istanza locale di Anki. Nessuna chiave di accesso è richiesta in modalità locale. Una volta collegato, `LEARNER_PROFILE.md` va aggiornato nel campo `anki_mcp` col nome del server, e `/review` inizia a interrogare direttamente le carte dovute invece di basarsi solo sui moduli tracciati nel profilo.

---

## Il mazzo dei falsi amici italiano-spagnolo

Nessun mazzo pubblico copre in modo dedicato le interferenze tra italiano e spagnolo, quindi il mazzo si genera in locale da una lista curata.

```
python tools/generate-falsos-amigos-deck.py
```

Il comando produce `_notes/anki-decks/falsos-amigos-it-es.apkg`, un file non tracciato in git perché derivato: la fonte di verità resta la lista dentro lo script, che si estende aggiungendo voci lì e rilanciando il comando. Il file si importa in Anki da *File, Importa*, e porta con sé i tag `falso-amico` e `interferenza-grammaticale` per filtrare il ripasso.

---

## Il vault Obsidian

Un vault Obsidian dedicato vive in `vault-spagnolo/`, locale e non tracciato in git, pensato per note libere di vocabolario, grammatica, falsi amici ed esiti delle sessioni, complementare alle carte di Anki e al catalogo di `SOURCES.md`. È raggiungibile dagli account Claude Code di questa macchina tramite il server MCP `obsidian-vaults`, la cui configurazione include il percorso del vault; la prima apertura va fatta manualmente da Obsidian, puntandolo sulla cartella.

---

## Le fonti

`SOURCES.md` è il catalogo unico e vivo di tutte le fonti del progetto: il corso strutturato, la libreria personale con lo stato di lettura, i canali e i podcast già in uso, le risorse di comprensione guidata per livello, i mazzi Anki pubblici valutati, gli strumenti online gratuiti, gli errori tipici italiano-spagnolo, e lo stato di manutenzione dei server MCP candidati. Il tutor lo legge sempre prima di erogare una lezione e cita da quale voce proviene il materiale: non è un documento di consultazione occasionale, è la base con cui ogni unità si àncora a una fonte reale invece che a conoscenza generica.

---

## Stato del progetto

- [x] Allineamento allo standard di progetto e attivazione del pacchetto `learning-agent`
- [x] Base di conoscenza locale (`doc-ingest`, con fallback OCR) sull'intero corpus disponibile
- [x] Primo profilo learner e roadmap pedagogica (`spa-01`...`spa-11`)
- [x] Mazzo Anki dei falsi amici italiano-spagnolo generato
- [ ] Anki desktop e AnkiConnect installati e collegati dal vivo
- [ ] Prima unità erogata con `/learn`
- [ ] Recupero di "Spanish Pronouns and Prepositions", unico titolo digitale catalogato ma assente dall'archivio

---

## Riferimenti

- `CLAUDE.md`, indice tecnico di progetto per chi ci lavora
- `.claude/PROJECT-SYSTEM.md`, lo standard di sistema di progetto adottato
- `.claude/context/learning-agent-reference.md`, il documento di riferimento pedagogico e architetturale del pacchetto `learning-agent`
- `SOURCES.md`, il catalogo delle fonti
- `LEARNER_PROFILE.md` e `SESSION-LOG.md`, lo stato dell'apprendimento e il log delle sessioni

[^1]: `.pdf`, `.docx`, `.pptx`, `.xlsx`, `.html`.
[^2]: *OCR*, Optical Character Recognition: estrazione del testo da un'immagine di pagina scansionata, invece che dal testo nativo del file.
[^3]: Plugin Anki con identificativo 2055492159, che espone un'interfaccia locale con cui strumenti esterni possono leggere e modificare mazzi e carte.
