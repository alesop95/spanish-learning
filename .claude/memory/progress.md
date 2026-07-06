# Work-log

> Append-only, in ordine cronologico inverso.

## 2026-07-06 — Prima esecuzione di /profile e log delle sessioni

Commit: successivo a 2caee17, non ancora committato
File toccati: `LEARNER_PROFILE.md` (popolato con obiettivo, livello principiante, cadenza
3-4x/settimana, tempo variabile, nessun profilo cognitivo dichiarato, stile visivo+testuale+hands-on,
e roadmap pedagogica spa-01…spa-11), nuovo `SESSION-LOG.md` (tracciato), note di progetto aggiunte
a `.claude/skills/learn-topic/SKILL.md` e `.claude/skills/review-session/SKILL.md` per loggare data,
ora e durata reale di ogni sessione, `CLAUDE.md` (indicizza `SESSION-LOG.md`), `context/roadmap.md`
(priorità 1 chiusa, aggiunta idea a bassa priorità di un deploy pubblico leggibile di
profilo/fonti/log sessioni oltre alla semplice lettura già possibile su GitHub), `context/current-work.md`
(due criteri di definition of done spuntati).

Motivo: l'utente ha eseguito i comandi git manuali (primo commit/push) e ha chiesto di procedere
con l'onboarding reale; ha inoltre chiesto di tracciare con timestamp le sessioni per adattare la
dimensione delle unità al tempo realmente disponibile (dichiarato `variable`), e di valutare in
parallelo, a bassa priorità, un deploy pubblico dei materiali.

Non ancora eseguito: prima unità con `/learn` (definition of done ancora aperta), installazione
Anki desktop/AnkiConnect.

## 2026-07-06 — Inizializzazione del sistema di progetto e attivazione del tutor di apprendimento

Commit: 2caee17
File toccati: intera anatomia `.claude/` (dal template `E:\template-claude-developing`), pacchetto
`learning-agent` (agenti, skill, comandi, `LEARNER_PROFILE.md`, riferimento pedagogico), pacchetto
`doc-ingest` (`tools/doc-ingest.py`), `SOURCES.md`, `.gitignore`, `CLAUDE.md`, `CLAUDE.local.md`,
`_notes/{DIARIO,RESOCONTO,TEST-CHECKLIST}.md`, `.mcp.json` (anki-mcp-server).

Riorganizzazione fonti: spostati in `_notes/raw-sources/` (ignorato da git) i documenti grezzi
preesistenti (`SPAGNOLO LEARNING.docx`, `elenco_libri_spagnolo_0220.xlsx`,
`Spanish Verb Tenses (2019).pdf`, `libri.7z`); estratto `libri.7z` e i due `.rar` annidati che
conteneva, rivelando 11 PDF della collana McGraw-Hill "Practice Makes Perfect" e affini. Rimosso
`bookdata_extract.py` (script estraneo, riferito a un altro progetto). Assorbiti in `SOURCES.md` i
quattro file `.txt` sparsi (Assimil, podcast, canale YouTube, sito DELE), poi rimossi come file
singoli. `SOURCES.md` consolida anche gli esiti di una ricerca dedicata su community (Reddit),
mazzi Anki pubblici, risorse di comprehensible input per livello CEFR/DELE, tool online gratuiti,
errori tipici italiano→spagnolo, e lo stato di manutenzione dei server MCP candidati.

Motivo: il progetto non aveva git né struttura; l'obiettivo dichiarato era allinearlo allo
standard portabile e trasformarlo in un tutor Claude Code guidato, con roadmap tracciata e
riferimento sistematico a tutte le fonti raccolte. Segue la sezione 10 di
`.claude/PROJECT-SYSTEM.md` (inizializzazione), non la 11, non essendoci storia git preesistente.

Decisioni prese in sessione (dettaglio in `memory/decisions.md`): knowledge base `doc-ingest` ora
con upgrade path a `knowledge-mcp`; spaced repetition `ankimcp/anki-mcp-server`; vault Obsidian
dedicato `vault-spagnolo/` (locale); repository GitHub pubblico
`github.com/alesop95/spanish-learning` con identità `github-personal`.

Non ancora eseguito in questa sessione, a carico dell'utente: primo commit e push, `/profile`
reale, installazione Anki desktop + AnkiConnect, verifica del comando esatto di
`ankimcp/anki-mcp-server`, apertura del vault Obsidian.
