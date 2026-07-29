
# Python Playground

A collection of small Python exercises and mini-projects, built to
strengthen fundamentals through deliberate practice rather than
tutorial-following. Each project lives in its own folder and targets
a specific set of concepts.

## Projects

| Project | Concepts practiced |
|---|---|
| [rock-paper-scissors](./rock-paper-scissors) | functions, dictionaries, exception handling, loops |

More exercises will be added as I work through core Python and into
FastAPI fundamentals.

---

## rock-paper-scissors

A command-line rock-paper-scissors game against the computer, with
score tracking across rounds.

### What this practices
- Functions and separation of concerns (input, computer choice,
  win/lose logic, game loop)
- Dictionaries for clean lookups instead of hardcoded index-matching
  or long if/elif chains
- Exception handling (`KeyError`) for invalid user input, with a
  retry loop instead of crashing or silently failing
- `while` loops for both input validation and the main game loop

### Run it
\`\`\`bash
python rock-paper-scissors/rock_paper_scissors.py
\`\`\`

You'll be prompted to enter `r`, `p`, or `s` each round. Score is
tracked and shown after every round; type `n` when asked to play
again to exit.
