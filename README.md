# KCAS Portfolio

> *A portfolio-construction framework for deciding what to own, what to add, and where the next dollar of capital should go — built on top of KCAS Core.*
>
> Part of the four-part **Knowledge Capital Ecosystem** — a journey from asset observer to allocator to creator: **evaluate** (Core) → **research** (Research) → **allocate** (Portfolio) → **create** (KCAB OS).

KCAS Portfolio is a portfolio construction and capital allocation system built on top of KCAS Core.

It helps investors determine:

- What should be owned next
- Where the next dollar should go
- Which exposures are over-concentrated
- How knowledge-capital assets fit together

## What is KCAS Portfolio?

KCAS Portfolio is NOT a stock screener.

KCAS Portfolio is NOT a stock analysis framework.

It is a portfolio-level decision system.

It answers:

- What should I own?
- What should I add?
- What should I reduce?
- What role does each asset play?

## Relationship to KCAS Ecosystem

Knowledge Capital Ecosystem

```text
KCAS Core
-> evaluates assets

KCAS Research
-> researches assets

KCAS Portfolio
-> allocates capital

KCAB OS
-> creates assets
```

## Core Features

### Portfolio Diagnosis

Evaluate:

- Concentration
- Diversification
- Sector Exposure
- Factor Exposure
- Knowledge Capital Exposure
- Reflexivity Exposure
- Geographic Exposure

### Portfolio Role Analysis

Assign:

- Core Holding
- Satellite Position
- Speculative Position
- Watchlist
- Avoid

### Opportunity Cost Ranking

Answer:

```text
What is the best use of the next dollar?
```

### Allocation Recommendation

Output:

- Increase
- Maintain
- Reduce
- Exit

### Portfolio Scores

Generate:

- Portfolio Quality Score
- Portfolio Resilience Score
- Portfolio Compounding Score
- Portfolio Concentration Score

## Folder Structure

```text
kcas-portfolio/
├── README.md
├── LICENSE
├── SKILL.md
├── agents/
│   └── openai.yaml
├── assets/
│   └── example-input.json
├── references/
│   ├── portfolio-framework.md
│   └── templates.md
└── scripts/
    └── portfolio_summary.py
```

## Installation

Manual installation:

```bash
mkdir -p ~/.codex/skills
cp -R kcas-portfolio ~/.codex/skills/kcas-portfolio
```

If the skill does not appear automatically:

Restart Codex.

GitHub installation:

```bash
git clone https://github.com/<your-username>/kcas-portfolio.git
cp -R kcas-portfolio ~/.codex/skills/kcas-portfolio
```

## Usage Examples

### Portfolio Review

```markdown
Use $kcas-portfolio to review:

NVDA 30%
PLTR 20%
QQQ 20%
Cash 30%
```

### Capital Allocation

```markdown
Use $kcas-portfolio.

Current Portfolio:

NVDA 30%
PLTR 20%
QQQ 20%
Cash 30%

Where should the next $10,000 go?
```

### Opportunity Cost Analysis

```markdown
Use $kcas-portfolio.

Candidates:

NVDA
PLTR
MU
Cash

Rank the best use of capital.
```

### Portfolio Construction

```markdown
Use $kcas-portfolio.

Available Capital: $100,000

Build a portfolio focused on long-term knowledge-capital compounders.
```

## Decision Philosophy

KCAS Portfolio rewards:

- Knowledge capital accumulation
- Long-term compounding
- Diversified exposure
- Reflexivity
- Durable moats

KCAS Portfolio avoids:

- Narrative chasing
- Excessive concentration
- Overlapping exposures
- Short-term prediction
- Ignoring opportunity cost

## Disclaimer

KCAS Portfolio is a decision-support framework.

It does not provide financial, legal, tax, or investment advice.
