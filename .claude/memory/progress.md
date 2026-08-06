# Work-log

> Append-only, in ordine cronologico inverso.

## 2026-07-07 — Consolidamento spa-01

Commit: successivo a 2caee17, non ancora committato File toccati: `LEARNER_PROFILE.md` (`progress.roadmap_module: spa-01-consolidato`), `SESSION-LOG.md` (voce del secondo tentativo).

Motivo: su richiesta dell'utente, secondo giro immediato di verifica su spa-01 con uno scenario volutamente diverso (mattina, registro formale) per testare la generalizzazione invece della sola ripetizione. `examiner` ha confermato il superamento dei tre errori del primo tentativo e rilevato produzione autonoma oltre il materiale erogato, dichiarando il modulo consolidato.

Non ancora eseguito: commit delle modifiche, spa-02 (prossimo modulo, mazzo Anki falsi amici già pronto), collegamento reale di Anki.

## 2026-07-07 — Prima unità reale: spa-01

Commit: successivo a 2caee17, non ancora committato File toccati: `LEARNER_PROFILE.md` (`progress.roadmap_module: spa-01`), `SESSION-LOG.md` (voce di sessione con esito), `context/current-work.md` (feature di onboarding chiusa, definition of done completa).

Motivo: prima esecuzione reale di `/learn` dopo la chiusura del giro di sviluppo. Il tutor ha recuperato tramite `kb-retriever` estratti reali dalla cache doc-ingest ("Spanish Conversation" di Yates, "Basic Spanish" di Richmond, "Complete Spanish All-in-One" di Nissenberg), erogato il nucleo di spa-01 (saluti, presentarsi, cortesia, numeri 0-10) scalato su una sessione dichiarata di 10-15 minuti, assegnato un compito di produzione attiva, e delegato la valutazione a `examiner`. Emersi tre errori di applicazione in contesto (non di grammatica): posizionamento del saluto orario, confusione funzionale ¿Cómo te llamas?/¿Cómo estás?, uso improprio di "Con permiso" come congedo. Il ciclo kb-retriever più examiner, mai eseguito prima end-to-end, ha funzionato secondo il disegno del pacchetto `learning-agent`.

Non ancora eseguito: commit delle modifiche, collegamento reale di Anki, un secondo mini-dialogo di consolidamento su spa-01 nella prossima sessione.

## 2026-07-07 — Documentazione operativa (README.md)

Commit: successivo a 2caee17, non ancora committato File toccati: nuovo `README.md` (guida pubblica: architettura in breve, `/profile`, ciclo `/learn`+`/review`, `doc-ingest.py` con OCR, collegamento Anki, generazione del mazzo falsi amici, vault Obsidian, stato del progetto, riferimenti), `CLAUDE.md` (indicizza `README.md` e i due script tracciati sotto `tools/`, corregge un grassetto residuo nella prosa non conforme a `rules/interaction-style.md`, aggiunge il vincolo su ADR-007), `context/current-work.md` (criterio di definition of done chiuso).

Motivo: a chiusura del giro di sviluppo, l'utente ha chiesto la documentazione operativa completa di come si usa il sistema, scritta seguendo lo stile discorsivo di `rules/interaction-style.md` invece che un elenco di feature.

Non ancora eseguito: commit di tutte le modifiche pendenti (secondo commit del progetto), prima unità reale con `/learn`, installazione di Anki desktop + AnkiConnect.

## 2026-07-07 — Chiusura del giro di sviluppo: Anki verificato, OCR, mazzo falsi amici, catalogo corretto

Commit: successivo a 2caee17, non ancora committato File toccati: `.mcp.json` (comando reale `@ankimcp/anki-mcp-server --stdio`, non più un tentativo), `tools/doc-ingest.py` (fallback OCR con `lang="eng+spa"`, nota su `TESSDATA_PREFIX`), nuovo `tools/generate-falsos-amigos-deck.py` (genanki, 18 falsi amici + 4 interferenze grammaticali), `SOURCES.md` (catalogo libri corretto da campione a lettura integrale delle 13 righe reali — scoperti due libri cartacei non catalogati prima, tra cui "Contacto - Curso de español para italianos" molto pertinente; confermato che "Spanish Pronouns and Prepositions" è un libro reale genuinamente assente dall'archivio; risolto il dubbio sulle due copie di "Spanish Verb Tenses", identiche, duplicato rimosso su conferma esplicita), `context/roadmap.md` e `context/STACK.md` aggiornati di conseguenza.

Ambiente di sistema toccato (fuori da git, ma rilevante per riprodurre l'ambiente): installati via `winget` i binari Tesseract OCR (`UB-Mannheim.TesseractOCR`) e Poppler (`oschwartz10612.Poppler`); scaricato il pacchetto lingua spagnola di Tesseract in una cartella utente dedicata (l'installer di base include solo l'inglese); installati via pip i pacchetti `pytesseract`, `pdf2image`, `genanki`, e le estensioni `markitdown[pdf,docx,xlsx]` già usate per l'ingestione base.

Motivo: dopo l'allineamento iniziale e il primo `/profile`, l'utente ha chiesto di chiudere i task di sviluppo rimasti aperti prima di passare alla documentazione operativa: verifica del comando MCP di Anki, correzione del PDF a 0 parole estratte, indagine sui gap del catalogo libri, e costruzione del mazzo Anki dedicato ai falsi amici (nessun mazzo pubblico esistente lo copre).

Un tentativo di cancellazione automatica del PDF duplicato è stato bloccato dal classificatore di sicurezza della sessione perché non esplicitamente autorizzato dall'utente per quel file specifico; la cancellazione è stata rieseguita solo dopo conferma diretta.

Non ancora eseguito: installazione di Anki desktop + AnkiConnect (a carico dell'utente, resta l'unico prerequisito mancante per attivare davvero lo spaced repetition); import del mazzo falsi amici in Anki; documentazione operativa (prossimo passo dichiarato dall'utente).

## 2026-07-06 — Prima esecuzione di /profile e log delle sessioni

Commit: successivo a 2caee17, non ancora committato File toccati: `LEARNER_PROFILE.md` (popolato con obiettivo, livello principiante, cadenza 3-4x/settimana, tempo variabile, nessun profilo cognitivo dichiarato, stile visivo+testuale+hands-on, e roadmap pedagogica spa-01…spa-11), nuovo `SESSION-LOG.md` (tracciato), note di progetto aggiunte a `.claude/skills/learn-topic/SKILL.md` e `.claude/skills/review-session/SKILL.md` per loggare data, ora e durata reale di ogni sessione, `CLAUDE.md` (indicizza `SESSION-LOG.md`), `context/roadmap.md` (priorità 1 chiusa, aggiunta idea a bassa priorità di un deploy pubblico leggibile di profilo/fonti/log sessioni oltre alla semplice lettura già possibile su GitHub), `context/current-work.md` (due criteri di definition of done spuntati).

Motivo: l'utente ha eseguito i comandi git manuali (primo commit/push) e ha chiesto di procedere con l'onboarding reale; ha inoltre chiesto di tracciare con timestamp le sessioni per adattare la dimensione delle unità al tempo realmente disponibile (dichiarato `variable`), e di valutare in parallelo, a bassa priorità, un deploy pubblico dei materiali.

Non ancora eseguito: prima unità con `/learn` (definition of done ancora aperta), installazione Anki desktop/AnkiConnect.

## 2026-07-06 — Inizializzazione del sistema di progetto e attivazione del tutor di apprendimento

Commit: 2caee17 File toccati: intera anatomia `.claude/` (dal template `E:\template-claude-developing`), pacchetto `learning-agent` (agenti, skill, comandi, `LEARNER_PROFILE.md`, riferimento pedagogico), pacchetto `doc-ingest` (`tools/doc-ingest.py`), `SOURCES.md`, `.gitignore`, `CLAUDE.md`, `CLAUDE.local.md`, `_notes/{DIARIO,RESOCONTO,TEST-CHECKLIST}.md`, `.mcp.json` (anki-mcp-server).

Riorganizzazione fonti: spostati in `_notes/raw-sources/` (ignorato da git) i documenti grezzi preesistenti (`SPAGNOLO LEARNING.docx`, `elenco_libri_spagnolo_0220.xlsx`, `Spanish Verb Tenses (2019).pdf`, `libri.7z`); estratto `libri.7z` e i due `.rar` annidati che conteneva, rivelando 11 PDF della collana McGraw-Hill "Practice Makes Perfect" e affini. Rimosso `bookdata_extract.py` (script estraneo, riferito a un altro progetto). Assorbiti in `SOURCES.md` i quattro file `.txt` sparsi (Assimil, podcast, canale YouTube, sito DELE), poi rimossi come file singoli. `SOURCES.md` consolida anche gli esiti di una ricerca dedicata su community (Reddit), mazzi Anki pubblici, risorse di comprehensible input per livello CEFR/DELE, tool online gratuiti, errori tipici italiano→spagnolo, e lo stato di manutenzione dei server MCP candidati.

Motivo: il progetto non aveva git né struttura; l'obiettivo dichiarato era allinearlo allo standard portabile e trasformarlo in un tutor Claude Code guidato, con roadmap tracciata e riferimento sistematico a tutte le fonti raccolte. Segue la sezione 10 di `.claude/PROJECT-SYSTEM.md` (inizializzazione), non la 11, non essendoci storia git preesistente.

Decisioni prese in sessione (dettaglio in `memory/decisions.md`): knowledge base `doc-ingest` ora con upgrade path a `knowledge-mcp`; spaced repetition `ankimcp/anki-mcp-server`; vault Obsidian dedicato `vault-spagnolo/` (locale); repository GitHub pubblico `github.com/alesop95/spanish-learning` con identità `github-personal`.

Non ancora eseguito in questa sessione, a carico dell'utente: primo commit e push, `/profile` reale, installazione Anki desktop + AnkiConnect, verifica del comando esatto di `ankimcp/anki-mcp-server`, apertura del vault Obsidian.
