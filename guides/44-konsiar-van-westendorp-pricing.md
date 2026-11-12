# Konsiar Van Westendorp pricing study

## When to use
Design a price-perception survey for Konsiar, clean real buyer responses, or analyze them with the Van Westendorp Price Sensitivity Meter. This is an authored method-specific skill, distinct from entry 09 Founder Pricing Strategy. Entry 09 covers broader models, tiers, competitors and unit economics; this skill stops at survey evidence, not a final price decision.

## How to use
Read `authored/konsiar-van-westendorp-pricing/SKILL.md`. For a new study, ask:

> Use konsiar-van-westendorp-pricing to prepare a survey for Konsiar. Confirm the exact package and billing unit from my current facts. Do not invent prices, respondents or features, and do not send the survey.

For actual responses, provide the CSV and ask for validation, respondent counts, the stated range convention, crossing events and limitations. The questionnaire's intro must be edited to match the confirmed offer before fielding. USD/month/business is this template's proposed study unit, not a settled packaging decision. No current price, plan limits or pricing status is assumed.

## Files and setup
All four complete reviewed files are normal files in `authored/konsiar-van-westendorp-pricing/`:
- `SKILL.md`: method, Konsiar context, interpretation and sources.
- `vw_analysis.py`: standard-library Python analysis.
- `survey-template.md`: questionnaire, not sent or fielded.
- `SYNTHETIC_example_responses.csv`: synthetic test fixture, never buyer evidence.

`prepare_library.py` copies these files and this guide into one new library folder after checksum verification. No upstream download or package installation is needed for this entry. Python 3 is needed to run the analysis; reading and applying the skill uses existing Claude access. Nothing was installed or activated on your device.

From the skill folder, analyze real data with:

```text
python3 vw_analysis.py responses.csv --curves-out curves.csv
```

Expected columns: `too_cheap,cheap,expensive,too_expensive`. The script rejects nonfinite, negative, nonnumeric and inconsistently ordered responses, reporting the counts. It uses observed-price step functions rather than a fixed grid, retains equality regions and separate crossings, and does not turn intervals into a midpoint decision.

## Scope and interpretation
The default range uses the original 1976 reversed not-cheap/not-expensive convention. `--range-method narrower` selects the documented alternative. Always label which method was used. PSM describes stated price perception, not proven demand, willingness to pay, revenue or a profit-maximizing price. Small samples remain directional. Synthetic test output must never be presented as a Konsiar finding.

No paid tools or extra Python packages are required. No survey, outreach, price update, plan change or account connection is authorized by adding this skill. Use the owner's existing approval scope for any later external action. The source notes and primary/methodological links are preserved in SKILL.md; the papers themselves are not redistributed. Checked 11 November 2026.
