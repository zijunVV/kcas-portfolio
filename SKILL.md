---
name: kcas-portfolio
description: Portfolio construction, portfolio diagnosis, capital allocation, opportunity cost, and risk management layer for the Knowledge Capital Asset System. Use when Codex needs to review current holdings, build a portfolio from available capital, decide where new capital should go, compare candidates versus cash or index funds, diagnose portfolio-level exposures, recommend Increase/Maintain/Reduce/Exit actions, or decide the single best next allocation action through Knowledge Capital. Must reuse KCAS Core outputs and must not evaluate assets in isolation.
---

# KCAS Portfolio

## Purpose

Use this skill to determine what should be owned next through portfolio construction, portfolio diagnosis, capital allocation, and risk management. The primary objective is not to decide whether an individual asset is good; it is to decide how each asset affects the whole portfolio and where the next dollar should go.

Core question:

```text
What should be owned next?
```

## Relationship To KCAS Core

Reuse KCAS Core whenever possible. In this workspace, KCAS Core is the `knowledge-capital-investing` skill.

KCAS Portfolio must reuse these KCAS Core outputs:

- Asset Quality Score
- Investment Attractiveness Score
- Final Allocation Score
- Knowledge Capital Analysis
- Compounding Potential
- Reflexivity

Do not duplicate evaluation logic. Use KCAS Core as the asset evaluation engine, then aggregate results at the portfolio level.

If KCAS Core results are missing for a holding or candidate:

1. Run or emulate KCAS Core for that asset.
2. Mark missing or stale scores as `Preliminary`.
3. Do not make strong allocation recommendations until the core evidence quality is adequate.

## Critical Rules

- Do not evaluate assets in isolation.
- Always consider opportunity cost.
- Always consider existing holdings.
- Always evaluate portfolio-level effects.
- Reward diversification of knowledge capital.
- Reward long-term compounding.
- Avoid concentration created by overlapping exposures.
- Focus on where the next dollar should go.
- Portfolio construction is more important than individual asset analysis.
- Capital allocation is the final objective.
- Never guarantee returns or predict short-term prices.
- Distinguish facts, interpretations, and assumptions.

## Primary Use Cases

- Portfolio Review: current holdings such as `NVDA 30%, PLTR 20%, QQQ 20%, Cash 30%`.
- Portfolio Construction: "I have $100,000. Build a portfolio."
- Capital Allocation: "I can invest $10,000 today. Where should it go?"
- Opportunity Cost Analysis: "Should I buy NVDA, PLTR, MU, or hold cash?"

## Required Inputs

Prefer:

- Current holdings and weights.
- Cash level.
- Candidate assets.
- New capital available.
- Investor horizon.
- Risk constraints.
- Existing KCAS Core outputs for each asset.

If holdings are missing, ask for them or explicitly state assumptions before constructing a portfolio. If the user asks only where new capital should go and no current portfolio is provided, frame the answer as candidate ranking, not portfolio-specific advice.

## Required Portfolio Outputs

### Portfolio Diagnosis

Evaluate each category as `Low`, `Moderate`, or `High`:

- Concentration
- Diversification
- Factor Exposure
- Knowledge Capital Exposure
- Sector Exposure
- Geographic Exposure
- Reflexivity Exposure
- Compounding Exposure

### Portfolio Role Analysis

Assign every asset one role:

- `Core Holding`
- `Satellite Position`
- `Speculative Position`
- `Watchlist`
- `Avoid`

### Exposure Map

Identify exposure percentages to:

- `AI Infrastructure`
- `AI Software`
- `Enterprise Software`
- `Semiconductors`
- `Cloud`
- `Healthcare`
- `Consumer`
- `Industrial`
- `Energy`
- `Creator Economy`
- `Other`
- `Cash`
- `Index Funds`

### Opportunity Cost Ranking

Answer:

```text
What is the highest-conviction use of new capital?
```

Rank current candidates, cash, index funds, and alternative opportunities.

### Allocation Recommendation

For each asset, output exactly one:

- `Increase`
- `Maintain`
- `Reduce`
- `Exit`

Explain why based on portfolio-level effects, not isolated quality.

### Portfolio Risks

Identify:

- Single-asset risk
- Sector risk
- Factor risk
- Valuation risk
- Macro risk
- Reflexivity risk
- Knowledge Capital concentration risk

### Portfolio Score

Generate:

- Portfolio Quality Score
- Portfolio Resilience Score
- Portfolio Compounding Score
- Portfolio Concentration Score

Use `scripts/portfolio_summary.py` when possible to aggregate core scores, exposures, and concentration from structured inputs. Read `references/portfolio-framework.md` for scoring guidance.

### Capital Allocation Decision

Answer:

```text
If only one action could be taken today, what should it be?
```

Explain why.

## Final Recommendation Labels

The final recommendation must always be exactly one:

- `Allocate More`
- `Maintain`
- `Wait`
- `Reduce`
- `Avoid`

## Required Output Structure

Use this structure every time:

1. `# KCAS Portfolio Analysis: [Portfolio / Situation]`
2. `## 1. Executive Summary`
3. `## 2. Current Portfolio Snapshot`
4. `## 3. KCAS Core Inputs`
5. `## 4. Portfolio Diagnosis`
6. `## 5. Exposure Map`
7. `## 6. Portfolio Role Analysis`
8. `## 7. Portfolio Scores`
9. `## 8. Opportunity Cost Ranking`
10. `## 9. Allocation Recommendations`
11. `## 10. Portfolio Risks`
12. `## 11. Capital Allocation Decision`
13. `## 12. Monitoring Dashboard`
14. `## 13. Final Recommendation`

## Boundaries

KCAS Portfolio may recommend increasing, maintaining, reducing, or exiting assets in the context of a portfolio. It must avoid false precision and should not present personalized financial advice as certainty. When data is missing, it must state what is required before confidence can rise.

## Bundled Resources

- Read `references/portfolio-framework.md` for portfolio scoring and diagnosis guidance.
- Read `references/templates.md` for reusable prompts, input schema, and output templates.
- Use `scripts/portfolio_summary.py` to aggregate structured holdings and KCAS Core outputs.
