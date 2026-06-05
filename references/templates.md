# KCAS Portfolio Templates

## Portfolio Review Prompt

```markdown
Use $kcas-portfolio to review this portfolio:

- NVDA: 30%
- PLTR: 20%
- QQQ: 20%
- Cash: 30%

Reuse KCAS Core outputs where possible.
Diagnose concentration, knowledge capital exposure, reflexivity exposure, compounding exposure, and opportunity cost.
Tell me where the next dollar should go.
```

## Portfolio Construction Prompt

```markdown
Use $kcas-portfolio to construct a portfolio from $100,000.

Candidate assets:
- [Asset 1]
- [Asset 2]
- [Asset 3]
- Cash
- Index funds

Investor horizon:
Risk tolerance:
Existing holdings:

Reuse KCAS Core outputs where possible.
Focus on portfolio construction, risk management, and where the next dollar should go.
```

## Capital Allocation Prompt

```markdown
Use $kcas-portfolio to decide where $10,000 should go today.

Current holdings:
- ...

Candidates:
- ...
- Cash
- Index funds

Reuse KCAS Core outputs.
Always consider opportunity cost and portfolio-level effects.
```

## Structured Input Schema

```json
{
  "portfolio_name": "Example Portfolio",
  "new_capital": 10000,
  "holdings": [
    {
      "asset": "NVDA",
      "weight": 0.3,
      "primary_exposure": "AI Infrastructure",
      "kcas_core": {
        "asset_quality_score": 9.0,
        "investment_attractiveness_score": 6.5,
        "final_allocation_score": 8.0,
        "knowledge_capital_score": 9.0,
        "compounding_potential_score": 9.0,
        "reflexivity_score": 9.0
      }
    }
  ],
  "candidates": ["NVDA", "PLTR", "MU", "Cash", "QQQ"],
  "constraints": [
    "Always consider opportunity cost",
    "Avoid overlapping exposures",
    "Focus on where the next dollar should go"
  ]
}
```

## Full Output Template

```markdown
# KCAS Portfolio Analysis: [Portfolio / Situation]

## 1. Executive Summary

- Current portfolio condition:
- Main strength:
- Main risk:
- Highest-conviction use of new capital:
- Final recommendation:

## 2. Current Portfolio Snapshot

| Asset | Weight | Exposure | KCAS Core Status | Key Note |
|---|---:|---|---|---|

## 3. KCAS Core Inputs

| Asset | Asset Quality | Investment Attractiveness | Final Allocation | Knowledge Capital | Compounding | Reflexivity | Confidence |
|---|---:|---:|---:|---:|---:|---:|---|

## 4. Portfolio Diagnosis

| Category | Level | Explanation |
|---|---|---|
| Concentration | Low/Moderate/High | ... |
| Diversification | Low/Moderate/High | ... |
| Factor Exposure | Low/Moderate/High | ... |
| Knowledge Capital Exposure | Low/Moderate/High | ... |
| Sector Exposure | Low/Moderate/High | ... |
| Geographic Exposure | Low/Moderate/High | ... |
| Reflexivity Exposure | Low/Moderate/High | ... |
| Compounding Exposure | Low/Moderate/High | ... |

## 5. Exposure Map

| Exposure | Percent | Notes |
|---|---:|---|

## 6. Portfolio Role Analysis

| Asset | Role | Why |
|---|---|---|

## 7. Portfolio Scores

Portfolio Quality Score: x/10  
Portfolio Resilience Score: x/10  
Portfolio Compounding Score: x/10  
Portfolio Concentration Score: x/10

## 8. Opportunity Cost Ranking

1. ...
2. ...
3. Cash
4. Index funds

## 9. Allocation Recommendations

| Asset | Recommendation | Why |
|---|---|---|
| ... | Increase/Maintain/Reduce/Exit | ... |

## 10. Portfolio Risks

- Single-asset risk:
- Sector risk:
- Factor risk:
- Valuation risk:
- Macro risk:
- Reflexivity risk:
- Knowledge Capital concentration risk:

## 11. Capital Allocation Decision

If only one action could be taken today:
- ...

Why:
- ...

## 12. Monitoring Dashboard

Positive triggers:
- ...

Negative triggers:
- ...

## 13. Final Recommendation

Recommendation: Allocate More / Maintain / Wait / Reduce / Avoid

Why:
- ...
```
