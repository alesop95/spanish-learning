# Profilo del learner

> Popolato dalla skill `build-roadmap` alla prima esecuzione di `/profile`, 2026-07-06. Riletto e
> aggiornato da `tutor` a ogni sessione di `/learn` e `/review`. È la fonte di verità dello stato
> di apprendimento: non si modifica a mano se non per correggere un errore.

```yaml
topic: "Spagnolo"
category: language
level: beginner
session_minutes: variable   # nessun blocco fisso dichiarato, decide di volta in volta
cadence: "3-4x/settimana"
kb_mcp: none                 # nessuna KB-MCP; retrieval via cache doc-ingest (_notes/.tmp-doc-cache/)
anki_mcp: none                # anki-mcp-server configurato in .mcp.json ma Anki desktop/AnkiConnect non ancora installati
cognitive_profile:
  adhd: false
  autism: false
  dyslexia: false
style: [visual, textual, hands_on]
special_interests: []
goal: >
  Obiettivo generale e progressivo, non un binario unico: si parte dalla conversazione quotidiana
  perché il livello è basico, poi si aggiunge comprensione di libri/letture e di serie
  tv/canzoni in spagnolo man mano che il livello sale. La certificazione DELE non è un binario
  separato ma un riferimento periodico: a ogni checkpoint di livello si guarda cosa lo stesso
  studio già fatto coprirebbe in ottica DELE (vedi SOURCES.md, sezione deleahora.com), senza
  deviare la roadmap verso un percorso d'esame dedicato finché il learner non lo chiede esplicitamente.
progress:
  roadmap_module: null
  anki_deck: null
```

## Roadmap

> Lingua straniera: unità tematiche senza dipendenze rigide, ordinate per frequenza d'uso più che
> per difficoltà (sezione 4.1 di `.claude/context/learning-agent-reference.md`). Ogni unità cita
> le fonti di `SOURCES.md` da cui il tutor deve attingere.

1. **spa-01 — Sopravvivenza e primi contatti**: saluti, presentarsi, numeri, cortesia, alfabeto e
   pronuncia di base (vibrante "r", "j", "ñ"). Fonti: Assimil "Lo spagnolo" (prime lezioni), Butterfly
   Spanish (YouTube), Dreaming Spanish livello Superbeginner.
2. **spa-02 — Falsi amici e interferenza italiano→spagnolo**: introdotto presto apposta, perché un
   italiano parte avvantaggiato ma rischia più interferenza negativa di altri profili. Fonti:
   `SOURCES.md` sezione 7 (lista falsi amici e interferenze grammaticali), da consolidare col mazzo
   Anki dedicato ancora da costruire (nessun deck pubblico esistente lo copre).
3. **spa-03 — Verbi essenziali al presente**: ser/estar, tener, ir, verbi regolari -ar/-er/-ir,
   verbi irregolari comuni. Fonti: "Basic Spanish" e "Spanish Verb Tenses" (Practice Makes Perfect,
   nella cache doc-ingest), Language Transfer (podcast) per l'intuizione grammaticale.
4. **spa-04 — Vocabolario di base per frequenza**: primi strati del deck di frequenza una volta
   collegato Anki. Fonti: mazzo AnkiWeb "New Spanish Top 5000 Vocabulary" (`SOURCES.md`, sezione 5).
5. **spa-05 — Frasi di sopravvivenza pratiche**: ristorante, indicazioni, negozio, presentarsi in
   contesti reali. Fonti: Dreaming Spanish A1-A2, Inklingo, MeloLingua.
6. **spa-06 — Passato: indefinido vs perfecto compuesto**: punto di interferenza tipico per un
   italiano (abitudine al passato prossimo). Fonti: "Spanish Verb Tenses" (cache doc-ingest).
7. **spa-07 — Prima conversazione guidata**: mini-dialoghi e comprensione A2-B1. Fonti: Twilingua,
   ¡Cuéntame!, Español con Juan (podcast/YouTube, `SOURCES.md` sezione 4).
8. **spa-08 — Lettura estensiva graduata**: primo libro leggibile per intero. Fonti: Free Graded
   Readers (A1-A2), poi progressivamente i libri della libreria personale in `SOURCES.md` sezione 2.
9. **spa-09 — Congiuntivo, por/para e altre interferenze intermedie**: quando il livello lo
   permette. Fonti: "Complete Spanish Grammar" (cache doc-ingest).
10. **spa-10 — Serie TV e canzoni in spagnolo**: primo materiale autentico con sottotitoli, poi
    senza. Da introdurre quando spa-07 è consolidato, coerente con l'obiettivo dichiarato.
11. **spa-11 — Checkpoint DELE periodico**: non un modulo da erogare in sequenza, ma un controllo
    ricorrente (a ogni salto di livello percepito) di cosa lo studio fatto finora coprirebbe per la
    certificazione, usando deleahora.com/actividades come riferimento pratico.

Nessuna unità ha prerequisiti rigidi (categoria lingua): il tutor sceglie l'ordine sopra come guida
di frequenza d'uso, ma può anticipare o posticipare un'unità in base a interesse e difficoltà reale
emersa in sessione.
