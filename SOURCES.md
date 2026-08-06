# Fonti del progetto

> Catalogo vivo e unico di tutte le fonti per l'apprendimento dello spagnolo: quelle raccolte dall'utente nel tempo e quelle emerse da una ricerca dedicata (community, mazzi Anki, comprehensible input, tool). Tracciato, a differenza dei file grezzi che referenzia (restano locali sotto `_notes/raw-sources/`, ignorati da git). `tutor`, `kb-retriever` e `build-roadmap` lo leggono prima di ogni lezione o di ogni costruzione di roadmap: ogni unità erogata deve citare da quale voce di questo file proviene il materiale. Le voci marcate "da verificare" sono segnalazioni di ricerca non confermate in prima persona: non vanno citate come fatti accertati.

## 1. Corso strutturato

- **Assimil — "Lo spagnolo", collana Senza Sforzo (superpack mp3)** https://www.assimil.it/-1132-lo-spagnolo-collana-senza-sforzo-superpack-mp3 Corso di riferimento per la progressione grammaticale di base, metodo intuitivo con dialoghi progressivi e audio.

## 2. Libreria personale (McGraw-Hill "Practice Makes Perfect" e affini)

Catalogata in `elenco_libri_spagnolo_0220.xlsx` (13 voci reali con foto, note, ISBN, formato, stato di lettura — verificato riga per riga il 2026-07-06, non le 15-16 stimate a una prima ricognizione superficiale; file originale conservato in `_notes/raw-sources/`, locale). Undici sono digitali e fisicamente presenti, estratte da `_notes/raw-sources/libri.7z` in `_notes/raw-sources/libri-estratti/`; due sono cartacee e non hanno controparte digitale nella libreria — non indicizzabili da `doc-ingest`, vanno consultate a mano dal libro fisico.

| Titolo | Autore | Edizione | Formato | Letto? |
|---|---|---|---|---|
| Basic Spanish | Dorothy Richmond | Premium 3rd ed., McGraw-Hill, 2020 | Digitale | N |
| Spanish Pronouns and Prepositions | Dorothy Richmond | Premium 4th ed., McGraw-Hill, 2021 | Digitale — **assente dall'archivio** | N |
| Spanish Vocabulary | Dorothy Richmond | 3rd ed., McGraw-Hill, 2018 | Digitale | N |
| Spanish Verb Tenses | Dorothy Richmond | Premium 4th ed., McGraw-Hill, 2019 | Digitale | N |
| Complete Spanish All-in-One | Gilda Nissenberg | Premium 3rd ed., McGraw-Hill, 2022 | Digitale | N |
| Complete Spanish Grammar | Gilda Nissenberg | Premium 4th ed., McGraw-Hill, 2020 | Digitale | N |
| Spanish Conversation | Jean Yates | Premium 4th ed., McGraw-Hill, 2024 | Digitale | N |
| The Ultimate Spanish Review and Practice | Ronni L. Gordon, David M. Stillman | Premium 4th ed., McGraw-Hill, 2019 | Digitale | N |
| Spanish Verb Drills | Vivienne Bey, Beatrice Concheff, Jean Yates | Premium 6th ed., McGraw-Hill, 2022 | Digitale | N |
| Complete Spanish Step by Step | Barbara Bregstein | Premium 2nd ed., McGraw-Hill, 2020 | Digitale | N |
| Madrigal's Magic Key to Spanish | Margarita Madrigal | Broadway Books, 2001 | Digitale | N |
| Gramática del español lengua extranjera | Carlos Romero Dueñas, Alfredo González Hermoso | Nueva edición, edelsa, 2011 | **Cartaceo** | N |
| Contacto — Curso de español para italianos, Nivel 2 | José Pérez Navarro, Carla Polettini | Zanichelli, 2013 | **Cartaceo** | N |

Note di verifica (risolte il 2026-07-06, confronto diretto dei file): `Spanish Verb Tenses` esisteva in **due copie** con hash diverso (contenuto testuale identico, verificato pagina per pagina — solo una ricompressione diversa dello stesso PDF); il duplicato in `_notes/raw-sources/` è stato rimosso su conferma dell'utente, resta solo la copia dentro `libri-estratti/Practice Makes Perfect/`. Il titolo **"Spanish Pronouns and Prepositions"** (ISBN 978-1-26-046755-0, Premium 4th ed. 2021) è un libro reale del catalogo, non un titolo fantasma né incluso in un volume all-in-one: è **genuinamente assente** dall'archivio digitale `libri.7z` — da recuperare separatamente se serve per il modulo `spa-02` (falsi amici) o `spa-09` (grammatica intermedia). I due libri cartacei erano stati persi nella prima ricognizione perché letta solo a campione: **"Contacto — Curso de español para italianos"** è particolarmente rilevante, essendo un corso pensato esplicitamente per madrelingua italiani con attività DELE Nivel Intermedio incluse.

## 3. Canali, podcast e siti già in uso

- **YouTube — @easyspanish**: https://www.youtube.com/@easyspanish — vocabolario ed espressioni per la vita quotidiana.
- **Podcast Spotify**: https://open.spotify.com/show/4qkp9HXtJ0oDXUkvwGcF5B (show) e un episodio specifico https://open.spotify.com/episode/1yTlIP7JMR8bhnEic0vaVl.
- **deleahora.com/actividades** — esercizi mirati per tutti i livelli, orientati alla certificazione DELE.

## 4. Comprehensible input per livello CEFR/DELE (da ricerca)

Principio guida: la ritenzione di un item isolato non implica saperlo applicare in contesto — va sempre accompagnata da esposizione naturale, non solo da flashcard.

### A1–A2 (principiante)
- **Dreaming Spanish** — dreaming.com/spanish — libreria video graduata per ore di esposizione (0–1500+), metodo comprehensible-input nativo per lo spagnolo. Free tier ampio (migliaia di video A1–A2), Premium 8$/mese per l'intera libreria.
- **Butterfly Spanish** (YouTube, gratis) — insegnamento chiaro per principianti, spagnolo messicano rallentato.
- **Language Transfer** (podcast audio, gratis) — non puro comprehensible input, ma costruisce intuizione grammaticale per scoperta guidata; buono come ponte pre-A1/A2.
- **Free Graded Readers** — freegradedreaders.com — testi a lettura estensiva, taggati CEFR A1–C2, di pubblico dominio.
- **Inklingo** — inklingo.app/spanish/stories — storie gratuite A1–B2 con audio nativo.
- **MeloLingua** — melolingua.com — storie gratuite A1–B2 con glosse a tocco.

### A2–B1 (lower-intermediate)
- **Twilingua** (podcast, gratis con tier premium) — formato bilingue a ponte (introduzione EN, storia in spagnolo calibrata sul livello, debrief EN).
- **¡Cuéntame!** (podcast, gratis) — Marta Ruiz Yedinak, storie da base a intermedio, esplicitamente disegnate per comprehensible input.
- **Español con Juan** (YouTube, gratis) — aneddoti e interviste A1–B2.

### B1–B2 (intermedio)
- **María Español** (YouTube, gratis) — narrazione/conversazione a ritmo naturale, sottotitoli in spagnolo disponibili.
- **Why Not Spanish** (YouTube, gratis) — accento colombiano, buono per l'ascolto intermedio.
- **StoryLearning Spanish** (YouTube, gratis) — narrativo, spiegazioni in spagnolo lento.
- **Notes in Spanish — Intermediate Podcast** (gratis, notesinspanish.com) — conversazioni 100% in spagnolo su temi reali.

### B2–C2 (avanzato)
- **Radio Ambulante** (podcast, gratis, distribuito NPR) — giornalismo narrativo su America Latina, spagnolo nativo a velocità piena, accenti multipli. Riferimento per C1–C2.
- **El Hilo** (podcast, gratis) — attualità latinoamericana a velocità nativa, buono per il registro giornalistico.
- **Duolingo Spanish Podcast** (gratis) — storie vere, usato da alcuni anche a livello avanzato.
- **News in Slow Spanish — "Advanced Spanish"** (freemium) — conversazione a velocità normale, trascrizioni/quiz a pagamento, audio parzialmente gratis.

## 5. Mazzi Anki pubblici consigliati (da ricerca)

Da importare in Anki e gestire tramite `ankimcp/anki-mcp-server` una volta collegato. Nota di metodo dalla community (aggregata, non uno studio verificato): lo *sentence mining* con frasi reali batte le liste di parole isolate, seguendo la regola **i+1** (un solo elemento sconosciuto per card).

- **"9000 Spanish sentences – difficulty sorted with native audio"** ankiweb.net/shared/info/1713698257 — ~9263 card cloze, audio nativo (Spagna centrale), frasi ordinate per rarità lessicale, ogni parola nuova introdotta una sola volta. Scelta primaria per il sentence mining, citata ricorrentemente come la più curata del gruppo.
- **"New Spanish Top 5000 Vocabulary"** — ankiweb.net/shared/info/2072103552 — top 5000 parole da *A Frequency Dictionary of Spanish* (Davies, 2017), con audio ed esempi. Utile per un italiano per saltare rapidamente i cognati evidenti e concentrarsi sul resto. Da verificare: esistono varianti quasi duplicate dello stesso mazzo (id 241428882, 1584072412, 1441686989) di autori diversi — sceglierne una sola, controllando la data di ultimo aggiornamento su AnkiWeb prima di scaricare.
- **"Ultimate Spanish Conjugation (Lisardo's KOFI Method)"** — ankiweb.net/shared/info/638411848 — ~4240 forme su ~70 verbi, include tutto il congiuntivo; orientato a intermedio/avanzato.
- **"500 Spanish verb conjugations by frequency"** — ankiweb.net/shared/info/1916926156 — 493 verbi in sottomazzi per modo, taggati per filtro; più efficiente del precedente come daily-driver.
- **Nessun mazzo dedicato ai falsi amici italiano↔spagnolo trovato**: da costruire su misura (vedi sezione 7), non esiste un deck pronto su AnkiWeb per questa coppia di lingue.

## 6. Tool online gratuiti (da ricerca)

- **Coniugazione**: Conjuguemos (conjuguemos.com) — tutti i tempi/modi, quiz e giochi; Live Lingua Conjugation (livelingua.com/conjugation) — 600+ verbi; pigQuiz (pigquiz.com) — quiz di coniugazione personalizzabili.
- **Dizionari**: SpanishDict (spanishdict.com) — il più adatto a principiante/intermedio, coniugatore integrato; WordReference (wordreference.com) — ottimo per uso idiomatico via i forum; RAE (rae.es) — autorevole ma solo in spagnolo, per livelli avanzati.
- **Corpora di frequenza**: doozan/spanish_data (github.com/doozan/spanish_data, CC-BY-4.0) — lemma+frequenza+POS da Wiktionary/Tatoeba/hermitdave; Corpus del Español (corpusdelespanol.org/resources.asp) — corpus da 10 miliardi di parole.
- **Correzione scritta**: LangCorrect (langcorrect.com) — community di correzione tandem, successore di Lang-8, supporta lo spagnolo; LanguageTool (languagetool.org) — grammatica/ortografia, tier gratuito.
- **Tandem/scambio linguistico**: Tandem (tandem.net) — tier gratuito, ~10M utenti; HelloTalk — tier gratuito base, paywall solo oltre 3 lingue simultanee; Speaky (speaky.com) — gratis, community più piccola.

## 7. Errori tipici italiano→spagnolo e falsi amici (da ricerca)

Un italiano parte avvantaggiato (lingue romanze vicine), ma la vicinanza stessa è la "trappola": genera interferenza negativa più che per un anglofono. Falsi amici citati ricorrentemente in più fonti (Burbuja del Español, Valenlingua, LearnAmo, Babbel Magazine): *burro* (IT burro / ES asino), *guardare* vs *guardar* (guardare / custodire), *salire* vs *salir* (salire / uscire), *pronto* (pronto / presto), *carta* (carta / lettera), *officina* vs *oficina* (officina / ufficio), *loro* (loro / pappagallo). Interferenze grammaticali/pronuncia segnalate (fonti pedagogiche, non Reddit): uso del congiuntivo diverso e più esteso in spagnolo, confusione *por*/*para*, sovrapposizione tra *pretérito indefinido* e *pretérito perfecto compuesto* per abitudine dal passato prossimo italiano, pronuncia della "r" vibrante e della "j" spagnola. Questa lista alimenta direttamente il modulo dedicato ai falsi amici nella roadmap pedagogica (vedi `LEARNER_PROFILE.md`).

**Mazzo Anki generato**: dato che nessun mazzo pubblico copre questa coppia di lingue (sezione 5), il mazzo è stato costruito su misura in `tools/generate-falsos-amigos-deck.py` (18 falsi amici lessicali + 4 interferenze grammaticali, tag `falso-amico` / `interferenza-grammaticale` / `spa-02`). Si rigenera con `python tools/generate-falsos-amigos-deck.py`, output in `_notes/anki-decks/falsos-amigos-it-es.apkg` (locale, non tracciato: la fonte di verità è la lista nello script, tracciata). Da importare in Anki una volta installato.

## 8. Note di metodologia dalla community (da ricerca, aggregata — non verificata in prima persona)

Critica ricorrente a Duolingo/app mainstream usate da sole: costruiscono riconoscimento passivo, non produzione attiva; la community raccomanda di affiancare **Language Transfer** per la logica grammaticale e conversazione reale (italki o equivalente) per la produzione. Nota di aggiornamento: Duolingo ha aggiunto funzioni AI/video-call nel 2024-2025 che attenuano parzialmente questa critica storica. Sullo spaced repetition, consenso community per il cloze su frasi reali rispetto a coppie L1↔L2 isolate, e per il mining personale di frasi da contenuti di immersione (es. pipeline Language Reactor + Netflix) rispetto ai soli mazzi predefiniti.

## 9. Skill e MCP per il language learning (da ricerca, verificati via repository)

- **m98/fluent** (github.com/m98/fluent, MIT, 231 stelle) — spaced repetition SM-2 locale con supporto esplicito allo spagnolo, incluso materiale di preparazione DELE. Il candidato più maturo trovato per un'integrazione futura oltre ad Anki.
- **hamsamilton/lang-tutor** (github.com/hamsamilton/lang-tutor, MIT, 9 stelle) — correzioni di grammatica/idiomi in tempo reale, guida dedicata allo spagnolo (ser/estar, indefinido/imperfetto, congiuntivo). Progetto piccolo, da tenere d'occhio più che da adottare subito.
- Voci "Polyglot" e "Spanish Learning Assistant" su mcpmarket.com: trovate solo per snippet di ricerca, non verificate via fetch diretto — da NON considerare finché non ispezionate a mano.

## 10. Stato dei server MCP candidati (verificato al 2026-07-06)

- **ankimcp/anki-mcp-server** — il più maturo (aggiornato 2 giorni prima della verifica, 369 stelle, 0 issue aperte, MIT) — scelto per questo progetto. Comando verificato il 2026-07-06 contro README GitHub e ankimcp.ai (non più un tentativo): pacchetto npm `@ankimcp/anki-mcp-server`, flag `--stdio` obbligatorio per l'integrazione MCP standard (altrimenti apre un server HTTP sulla porta 3000), configurato in `.mcp.json`. Nessuna API key richiesta in modalità locale; richiede Node.js 22.12.0+, Anki desktop già avviato e l'add-on AnkiConnect (porta 8765 di default) prima di avviare il server MCP. Limite noto: `updateNoteFields` fallisce silenziosamente se la nota è aperta nel browser di Anki.
- **olafgeibig/knowledge-mcp** — sano ma rilasci più lenti (ultimo a 5 mesi dalla verifica); candidato per un eventuale upgrade da `doc-ingest` a RAG vero.
- **nkapila6/mcp-local-rag** — il più aggiornato tra le alternative RAG locali (giugno 2026), pensato più per ricerca web locale che per un corpus di libri personali.
- **patakuti/Local Knowledge RAG MCP** — dettagli non verificabili con fetch diretto al momento del controllo; dipende da PostgreSQL+pgvector, il che contraddice il posizionamento "100% locale e semplice" — da verificare a mano prima di un'eventuale adozione.
- **scorzeth/anki-mcp-server** — una scansione di terze parti (AgentSeal, non verificata direttamente) segnala un problema di sicurezza critico/alto; trattare come segnalazione non confermata, ma è comunque un motivo in più per preferire `ankimcp/anki-mcp-server`.
