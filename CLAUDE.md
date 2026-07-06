# spanish-learning

> Istruzioni di team, versionate. Questo file è l'indice del progetto: indicizza i soli file
> satellite tracciati e descrive la procedura di ripresa. Le preferenze personali vivono in
> `CLAUDE.local.md`, ignorato da git, non qui.

## Cos'è questo progetto

Un tutor Claude Code che guida l'apprendimento personale dello spagnolo (L2, italofono adulto)
con una roadmap pedagogica tracciata, spaced repetition via Anki, una knowledge base locale sui
libri e materiali personali dell'utente, e riferimento sistematico a tutte le fonti raccolte
(personali e di ricerca) in `SOURCES.md`. Non è un progetto software: la maggior parte
dell'attività sono lezioni, ripassi e aggiornamenti dello stato di apprendimento, non codice.

## Procedura di ripresa in una sessione nuova

Lo stato del progetto è interamente recuperabile su disco. Si legge per primo
`.claude/memory/index.md` (branch, commit di riferimento, stato delle schede, punto di ripresa),
poi `.claude/context/current-work.md` per la feature attiva. Si invoca la skill `sync-context`
per il drift delle schede, e si leggono solo le schede pertinenti al task. `.claude/memory/progress.md`
e `.claude/memory/decisions.md` danno storia e decisioni quando servono. Se la sessione riguarda
una lezione o un ripasso invece di una modifica di struttura, si legge invece `LEARNER_PROFILE.md`
(stato del learner e roadmap pedagogica) e `SOURCES.md` (catalogo delle fonti), e si esegue
`/learn` o `/review` secondo il caso.

## Indice dei file satellite tracciati

Memoria e meta-stato, sotto `.claude/memory/`, letti sempre a inizio sessione.

```
.claude/memory/index.md       snapshot e tabella di sincronizzazione, da leggere per primo
.claude/memory/progress.md    work-log append-only di passi e riconciliazioni
.claude/memory/decisions.md   registro ADR-lite delle decisioni architetturali
```

Schede tecniche, sotto `.claude/context/`, con frontmatter di riconciliazione.

```
.claude/context/STACK.md                  stack di apprendimento: MCP, doc-ingest, vault
.claude/context/design-and-security.md    non applicabile (dichiarato), privacy dei dati personali
.claude/context/deployment.md             non applicabile (dichiarato)
.claude/context/dev-testing.md            verifica pipeline di ingestione e loop di apprendimento
.claude/context/current-work.md           feature attiva, definition of done, domande aperte
.claude/context/roadmap.md                direzione e priorità di progetto (non pedagogiche)
.claude/context/learning-agent-reference.md   documento di riferimento pedagogico e architetturale
```

Stato del learner e fonti, in radice.

```
LEARNER_PROFILE.md   stato del learner: topic, livello, cadenza, profilo cognitivo, roadmap pedagogica
SOURCES.md            catalogo unico di tutte le fonti (personali + di ricerca), da citare sempre
```

Regole modulari sotto `.claude/rules/`, skill sotto `.claude/skills/` (motore di riconciliazione:
`init-project-system`, `sync-context`, `git-sync`, `repo-status`, `onboard`; pacchetto
learning-agent: `build-roadmap`, `learn-topic`, `review-session`). Agenti sotto `.claude/agents/`
(`tutor`, `kb-retriever`, `examiner`). Comandi sotto `.claude/commands/` (`/profile`, `/learn`,
`/review`). Lo standard di sistema completo è in `.claude/PROJECT-SYSTEM.md`.

## Apprendimenti recenti

```
- [2026-07-06] Init del sistema di progetto + attivazione learning-agent + doc-ingest; corpus
  locale estratto da libri.7z (11 PDF, due copie con hash diverso di Spanish Verb Tenses, un
  titolo catalogato "Pronouns and Prepositions" non trovato fisicamente — vedi roadmap.md).
```

## Vincoli di team

Le operazioni di `git add`, commit e push restano sempre manuali dell'utente: l'agente prepara i
file, non committa. L'identità git è impostata a livello locale del repo secondo
`.claude/rules/git-identity-and-repo.md` (profilo `github-personal`, non quello di lavoro). Il
repository è **pubblico**: nessun binario grezzo (libri, docx, xlsx originali) va mai tracciato,
solo i metadati bibliografici in `SOURCES.md` — vedi `.gitignore` e ADR-005 in
`.claude/memory/decisions.md`. Il tutor (`.claude/agents/tutor.md`) deve sempre citare `SOURCES.md`
oltre alla knowledge base prima di erogare una lezione. Lo stile di documentazione è quello di
`.claude/rules/interaction-style.md`. Claude non scrive autonomamente nei file di memoria e di
contesto: li aggiorna solo su richiesta esplicita.
