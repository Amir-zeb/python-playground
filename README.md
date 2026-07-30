
# Python Playground

A collection of small Python exercises and mini-projects, built to
strengthen fundamentals through deliberate practice rather than
tutorial-following. Each project lives in its own folder and targets
a specific set of concepts.

## Projects

| Project | Concepts practiced |
|---|---|
| [rock-paper-scissors](./rock-paper-scissors) | functions, dictionaries, exception handling, loops, strict typing (Literal, tuple, dict generics) |
| [heads-or-tails](./heads-or-tails) | functions, dictionaries, exception handling, binary comparison logic, strict typing |
| [atm-simulator](./atm-simulator) | OOP (classes, encapsulation, object references), custom exceptions, `match` statements, forward references, multi-class design (User, Account, Transaction, Bank, Auth) |

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
- Strict typing with `Literal` and typed tuples/dicts, checked with `mypy`

### Run it
\`\`\`bash
uv run python rock-paper-scissors/rock_paper_scissors.py
\`\`\`

You'll be prompted to enter `r`, `p`, or `s` each round. Score is
tracked and shown after every round; type `n` when asked to play
again to exit.

---

## heads-or-tails

A command-line coin-flip game against the computer, with score
tracking across rounds.

### What this practices
- Same core shape as rock-paper-scissors (input, random outcome,
  comparison, scoring loop), applied to a simpler binary case
- Direct equality comparison instead of a win/lose lookup table,
  since a coin flip has no "beats" relationship
- Strict typing with `Literal` for both game outcomes and coin sides

### Run it
\`\`\`bash
uv run python heads-or-tails/heads_or_tails.py
\`\`\`

You'll be prompted to enter `h` or `t` each round. Score is tracked
and shown after every round; type `n` when asked to play again to exit.

---

## atm-simulator

A command-line ATM simulator with login, balance inquiry, cash
withdrawal, and transaction history, built around a proper
multi-class design instead of dictionaries.

### What this practices
- Real OOP design: `User`, `Account`, `Transaction`, `Bank`, and
  `Auth` as distinct classes with clear responsibilities, instead of
  dicts and loose functions
- Object references between classes (`Account` holds a real `User`
  reference; `Transaction` holds a real `Account` reference) instead
  of manually-resolved IDs
- Custom exceptions (`InsufficientFundsError`) alongside built-ins
  (`ValueError`), and catching them at the right layer — where the
  program can respond meaningfully, not where the error originates
- `match` statements for menu handling
- Forward references (`"Account"` as a string type hint) for classes
  that reference each other before both are fully defined
- A `Bank` class as the central ledger, aggregating transactions
  across all accounts rather than each account tracking its own history

### Run it
\`\`\`bash
uv run python atm-simulator/atm_simulator.py
\`\`\`

Log in with one of the seeded users (`amir`/`1122` or `ali`/`4455`),
then use the menu to check balance, withdraw cash, or view
transaction history.