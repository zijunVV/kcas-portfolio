#!/usr/bin/env python3
"""Aggregate KCAS Core outputs into portfolio-level diagnostics."""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path
from typing import Any


CORE_KEYS = {
    "asset_quality_score": "Portfolio Quality Score",
    "compounding_potential_score": "Portfolio Compounding Score",
}


def load_input(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if "holdings" not in data or not isinstance(data["holdings"], list):
        raise ValueError("Input JSON must include a holdings array")
    return data


def normalize_weights(holdings: list[dict[str, Any]]) -> list[dict[str, Any]]:
    total = sum(float(item.get("weight", 0)) for item in holdings)
    if total <= 0:
        raise ValueError("Holding weights must sum to a positive value")
    normalized = []
    for item in holdings:
        copy = dict(item)
        copy["normalized_weight"] = float(item.get("weight", 0)) / total
        normalized.append(copy)
    return normalized


def weighted_average(holdings: list[dict[str, Any]], key: str) -> float | None:
    values = []
    for item in holdings:
        core = item.get("kcas_core", {})
        if key in core and core[key] is not None:
            values.append((item["normalized_weight"], float(core[key])))
    if not values:
        return None
    return sum(weight * score for weight, score in values)


def exposure_map(holdings: list[dict[str, Any]]) -> dict[str, float]:
    exposures: dict[str, float] = defaultdict(float)
    for item in holdings:
        exposure = item.get("primary_exposure", "Other")
        exposures[exposure] += item["normalized_weight"]
    return dict(sorted(exposures.items(), key=lambda pair: pair[1], reverse=True))


def hhi(holdings: list[dict[str, Any]]) -> float:
    return sum(item["normalized_weight"] ** 2 for item in holdings)


def concentration_level(hhi_score: float) -> str:
    if hhi_score >= 0.30:
        return "High"
    if hhi_score >= 0.18:
        return "Moderate"
    return "Low"


def resilience_score(holdings: list[dict[str, Any]], exposures: dict[str, float], hhi_score: float) -> float:
    cash_weight = exposures.get("Cash", 0.0)
    top_exposure = max(exposures.values()) if exposures else 1.0
    concentration_penalty = min(hhi_score / 0.40, 1.0) * 2.0
    exposure_penalty = min(top_exposure / 0.60, 1.0) * 1.5
    cash_bonus = min(cash_weight / 0.25, 1.0) * 1.0
    base = 7.0 + cash_bonus - concentration_penalty - exposure_penalty
    return max(0.0, min(10.0, base))


def portfolio_concentration_score(hhi_score: float, top_exposure: float) -> float:
    penalty = min(hhi_score / 0.40, 1.0) * 3.0 + min(top_exposure / 0.60, 1.0) * 2.0
    return max(0.0, min(10.0, 9.0 - penalty))


def main() -> int:
    parser = argparse.ArgumentParser(description="Summarize a KCAS portfolio input JSON.")
    parser.add_argument("input", type=Path, help="Path to portfolio JSON input.")
    parser.add_argument("--json", action="store_true", help="Output JSON instead of Markdown.")
    args = parser.parse_args()

    data = load_input(args.input)
    holdings = normalize_weights(data["holdings"])
    exposures = exposure_map(holdings)
    hhi_score = hhi(holdings)
    top_exposure = max(exposures.values()) if exposures else 0.0

    quality = weighted_average(holdings, "asset_quality_score")
    compounding = weighted_average(holdings, "compounding_potential_score")
    resilience = resilience_score(holdings, exposures, hhi_score)
    concentration = portfolio_concentration_score(hhi_score, top_exposure)

    result = {
        "portfolio_name": data.get("portfolio_name", "KCAS Portfolio"),
        "exposure_map": {key: round(value * 100, 2) for key, value in exposures.items()},
        "concentration_hhi": round(hhi_score, 4),
        "concentration_level": concentration_level(hhi_score),
        "portfolio_quality_score": None if quality is None else round(quality, 2),
        "portfolio_resilience_score": round(resilience, 2),
        "portfolio_compounding_score": None if compounding is None else round(compounding, 2),
        "portfolio_concentration_score": round(concentration, 2),
    }

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0

    print(f"# {result['portfolio_name']}")
    print()
    print("## Exposure Map")
    print()
    print("| Exposure | Percent |")
    print("|---|---:|")
    for exposure, pct in result["exposure_map"].items():
        print(f"| {exposure} | {pct:.2f}% |")
    print()
    print(f"Concentration HHI: {result['concentration_hhi']}")
    print(f"Concentration Level: {result['concentration_level']}")
    print(f"Portfolio Quality Score: {result['portfolio_quality_score']}/10")
    print(f"Portfolio Resilience Score: {result['portfolio_resilience_score']}/10")
    print(f"Portfolio Compounding Score: {result['portfolio_compounding_score']}/10")
    print(f"Portfolio Concentration Score: {result['portfolio_concentration_score']}/10")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
