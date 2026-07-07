# Registro delle decisioni architetturali

> Convenzione ADR-lite, append-only.

## ADR-001 — Adozione del sistema di progetto portabile

Data: 2026-07-06
Stato: accettata
Contesto: il progetto era solo una cartella di file grezzi senza git né struttura; serviva uno
stato interamente recuperabile e documentazione allineata senza rilettura integrale a ogni
sessione.
Decisione: adottare il sistema descritto in `.claude/PROJECT-SYSTEM.md`, seguendo la procedura di
inizializzazione (sezione 10) con riorganizzazione dei contenuti preesistenti invece che
ricostruzione da zero.
Motivazione: persistenza strutturale su disco indipendente dalla sessione di chat.
Conseguenze: ogni passo aggiorna schede, `last-verified-commit`, snapshot e work-log; commit e
push restano manuali.

## ADR-002 — Attivazione del pacchetto `learning-agent`

Data: 2026-07-06
Stato: accettata
Contesto: lo scopo dichiarato del progetto è l'apprendimento personale dello spagnolo, non lo
sviluppo di un prodotto; il template offre un pacchetto già pronto per questo caso.
Decisione: istanziare `learning-agent` per intero (tre subagent, tre skill, tre comandi,
`LEARNER_PROFILE.md`, riferimento pedagogico), e aggiungere `SOURCES.md` come catalogo di fonti
non previsto dal pacchetto originale, per soddisfare il requisito esplicito di riferimento
sistematico a tutte le fonti raccolte.
Motivazione: evitare di reinventare un'architettura (livelli KB/SRS/orchestrazione) già
progettata e documentata in `context/learning-agent-reference.md`.
Conseguenze: `tutor` e `kb-retriever` sono stati estesi con una nota di progetto che li vincola a
leggere anche `SOURCES.md` prima di ogni lezione.

## ADR-003 — Knowledge base: `doc-ingest` ora, `knowledge-mcp` come upgrade futuro

Data: 2026-07-06
Stato: accettata
Contesto: il corpus locale (docx, xlsx, pdf, 11 libri estratti da un archivio 7z) va reso
interrogabile senza bruciare token a ogni sessione; `knowledge-mcp` (RAG ibrido vettoriale+grafo)
richiede Python 3.12 + `uv`, non verificati su questa macchina, mentre `doc-ingest` richiede solo
`markitdown`.
Decisione: partire con `doc-ingest` (cache Markdown locale a costo zero), rivalutare
`knowledge-mcp` quando il corpus o le esigenze di retrieval semantico lo giustificano.
Motivazione: setup minimo per iniziare subito, upgrade path esplicito e non chiuso.
Conseguenze: `kb-retriever` legge `_notes/.tmp-doc-cache/`, non un MCP; `roadmap.md` di progetto
registra la rivalutazione come priorità futura.

## ADR-004 — Spaced repetition: `ankimcp/anki-mcp-server`

Data: 2026-07-06
Stato: accettata
Contesto: tra i candidati verificati (`ankimcp/anki-mcp-server`, `mcp-ankiconnect`, alternative
TypeScript), `ankimcp/anki-mcp-server` risultava il più maturo e mantenuto al controllo del
2026-07-06 (aggiornato 2 giorni prima, 369 stelle, 0 issue aperte), a fronte di una segnalazione
di sicurezza non verificata contro un'alternativa (`scorzeth/anki-mcp-server`).
Decisione: adottare `ankimcp/anki-mcp-server` in `.mcp.json`, comando esatto da verificare dal
README al momento dell'installazione effettiva.
Motivazione: manutenzione attiva e nessuna issue aperta come segnale di salute più forte degli
alternativi.
Conseguenze: prerequisiti manuali dell'utente (Anki desktop, add-on AnkiConnect) restano fuori
dalla portata dell'agente.

## ADR-005 — Repository pubblico con separazione stretta contenuto/metadati

Data: 2026-07-06
Stato: accettata
Contesto: il repository `github.com/alesop95/spanish-learning` è pubblico; il progetto include
però una libreria personale di libri protetti da copyright.
Decisione: i binari grezzi (`.docx`, `.pdf`, `.xlsx`, `.7z`, `.rar`) restano sempre fuori da git
(`.gitignore`), tracciato solo `SOURCES.md` come catalogo di metadati bibliografici e link.
Motivazione: evitare la distribuzione pubblica non autorizzata di materiale protetto da copyright,
pur mantenendo tracciata la logica del tutor e il riferimento alle fonti.
Conseguenze: chi clona il repository ottiene la logica del tutor e il catalogo delle fonti, ma
deve procurarsi autonomamente i libri fisici o le loro copie digitali.

## ADR-006 — Mazzo Anki dei falsi amici generato su misura, non cercato tra i pubblici

Data: 2026-07-07
Stato: accettata
Contesto: la ricerca (sezione 5 di `SOURCES.md`) aveva già escluso l'esistenza di un mazzo
pubblico AnkiWeb per i falsi amici italiano↔spagnolo.
Decisione: generare il mazzo con uno script proprio (`tools/generate-falsos-amigos-deck.py`,
libreria `genanki`), con la lista dei falsi amici tracciata nello script stesso e l'`.apkg`
compilato trattato come artefatto derivato, non tracciato.
Motivazione: coerenza con il principio di separazione fonte/derivato già adottato per
`doc-ingest` (si versiona la fonte riproducibile, non l'output); la lista è conoscenza
linguistica di dominio pubblico, non contenuto protetto da copyright, quindi può restare
tracciata anche in un repository pubblico.
Conseguenze: il mazzo si rigenera con un comando invece di essere mantenuto a mano in Anki;
future aggiunte di falsi amici o interferenze grammaticali si fanno editando lo script, non il
file `.apkg`.

## ADR-007 — Nessuna cancellazione di file dell'utente senza conferma esplicita per quel file

Data: 2026-07-07
Stato: accettata
Contesto: durante un task di sola "indagine" sui libri duplicati, un tentativo automatico di
cancellare il PDF duplicato è stato bloccato dal classificatore di sicurezza della sessione,
perché il compito assegnato non autorizzava la cancellazione, solo l'analisi.
Decisione: qualunque cancellazione di file preesistenti dell'utente in questo progetto richiede
una conferma esplicita per quel file specifico, anche quando la duplicazione è verificata con
certezza tecnica (hash/contenuto identico); un'indagine non implica mai il permesso di agire di
conseguenza.
Motivazione: i file grezzi in `_notes/raw-sources/` sono l'unica copia locale di materiale che
l'utente ha raccolto nel tempo; un errore di giudizio nella deduplica sarebbe irreversibile senza
backup esterni.
Conseguenze: le prossime indagini su duplicati o file superflui si concludono con una proposta
esplicita e una domanda, mai con un'azione diretta.
