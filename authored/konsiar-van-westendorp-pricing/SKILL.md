---
name: konsiar-van-westendorp-pricing
description: Run a Van Westendorp Price Sensitivity Meter study for Konsiar (AI auto-replies for Instagram/WhatsApp business inboxes). Use when designing the pricing survey, cleaning or analyzing real responses, or interpreting the acceptable price range. Works only with real respondent data - never invents respondents or a price.
---

# Konsiar pricing study (Van Westendorp PSM)

Goal: find the price range that Konsiar's target buyers perceive as
acceptable, from real survey responses. The method gives a perception
range, not a final price. Final pricing is a separate synthesis step
(costs, competitors, packaging, strategy) that this skill does not
perform.

## Product context

- Konsiar: the user's SaaS - AI auto-replies for Instagram and WhatsApp
  business inboxes, for small businesses that sell through DMs.
- Offer framing: live demo + two-week trial.
- Buyer: owner/manager of a small business that gets customer DMs
  (e.g. jewellery, boutiques, local services), not enterprise.
- Study unit: one subscription priced as USD per month per business. This
  is the unit this survey is designed around - not a confirmed packaging
  decision. If Konsiar's packaging changes (annual billing, per-seat,
  tiers), adapt the wording with the user first.
- Do not assume Konsiar's pricing status, tiers, plan limits, seat
  counts, or competitor prices unless the user supplies them. Confirm the
  current state with the user instead of asserting it.

## The four questions (core instrument)

Per respondent, in this order (the original 1976 ordering), each answered
with a monthly price. Keep the "beginning to / starting to" framing - it
is what makes the curves interpretable:

1. Too cheap: At what monthly price would you begin to experience Konsiar
   as too cheap - so that you say "at this price the quality cannot be
   good"?
2. Too expensive: At what monthly price would you begin to experience
   Konsiar as too expensive - so that you would never consider it
   yourself?
3. Expensive: At what monthly price are you beginning to experience
   Konsiar as expensive?
4. Cheap: At what monthly price are you beginning to experience Konsiar
   as cheap (a bargain for the money)?

The original used a 25-40 step price scale spanning impossibly low to
impossibly high, with the scale direction alternated between questions.
Open numeric entry is standard modern practice; either way, never suggest
or pre-fill prices.

Show a short product description before the questions so answers are
about the same product. survey-template.md has a full questionnaire.
EDIT ITS INTRO PARAGRAPH WITH THE USER BEFORE FIELDING: the exact
feature/package description must be confirmed, not invented.

## Survey rules

- Real respondents from the target market only. Never generate, simulate,
  or "enrich" responses with an LLM. Synthetic data is for testing the
  script only and must be labeled as such.
- Screen respondents (runs a business that gets customer enquiries via
  Instagram or WhatsApp DMs). Out-of-market answers pollute the range.
- Accept any non-negative numeric answer, no upper cap; clipping or
  suggested values anchor respondents and cut off genuine answers.
- Register "don't know" answers separately and do not process them; their
  level is itself an indicator of price-consciousness (van Westendorp).
- Per respondent the four answers must satisfy
  too_cheap <= cheap <= expensive <= too_expensive. The script removes
  violating rows and reports the count - report it, never silently fix or
  drop. (The 1976 paper auto-corrected "impossible answers"; removal with
  a reported count is standard modern practice, e.g. the R
  pricesensitivitymeter package's validate step.)
- Small samples are directional only. State the n with every result.

## Analysis - and the convention question (read this)

Two definitions of the range endpoints exist in the wild. They give
different numbers. This skill defaults to van Westendorp's own 1976
definitions ("original"); pass --range-method narrower for the variant
used by some modern tools (Conjointly, Quantilope, Milieu). Never mix
the two, and say which one any reported range used.

Collect responses into a CSV, one row per respondent, columns:
too_cheap, cheap, expensive, too_expensive (numbers, USD/month). Run:

    python3 vw_analysis.py responses.csv --curves-out curves.csv

The script (stdlib only) builds cumulative-frequency curves - "too cheap"
and "cheap" inverted, per convention - and finds:

- PMC, point of marginal cheapness (lower bound)
  original: "too cheap" x "not cheap". Below it, more respondents say
  too cheap than not cheap.
  narrower: "too cheap" x "expensive".
- PME, point of marginal expensiveness (upper bound)
  original: "too expensive" x "not expensive". Above it, more respondents
  say too expensive than not expensive.
  narrower: "cheap" x "too expensive".
- IDP, indifference price point: "cheap" x "expensive". Equal shares rate
  it cheap and expensive. Van Westendorp found the IDP usually tracks the
  median price actually paid in the market or a market leader's price.
- OPP, optimal price point: "too cheap" x "too expensive". Equal shares
  rate it too cheap and too expensive - least resistance at both extremes.
  In van Westendorp's words "optimal" means least resistance and has "no
  relation to the optimum-theory in economy". It is NOT a revenue or
  profit optimum.

The curves are step functions evaluated exactly at observed prices (no
grid, no interpolation - one huge outlier cannot compress resolution).
When curves coincide over a stretch, the script reports the equality
region as [a, b) or "a and above", never a fake precise point or an
averaged midpoint. curves.csv holds all six curves at observed prices for
the classic four-line chart (plus the two reversed "not-" curves for the
original range points). Ties count toward the expensive-side curves and
the cheap-side curves use strict >, making not-cheap exactly 1 - cheap,
so the original method's "reversed graphs" are literal complements.

## Interpretation rules (hold these every time)

- Report the acceptable range (PMC..PME), the IDP, the n, and which
  range method was used. Those are the load-bearing outputs.
- PSM measures stated price perception, not willingness to pay, demand,
  or revenue. Never claim any intersection maximizes profit.
- Keep survey evidence separate from the final pricing recommendation.
  This skill ends at "the range the market perceives as acceptable".
- If there is no data yet, say so and help run the survey. Do not produce
  a number from assumptions and present it as a finding.

## Files

- vw_analysis.py - analysis script (usage above)
- survey-template.md - questionnaire template; intro paragraph must be
  confirmed with the user before fielding
- SYNTHETIC_example_responses.csv - SYNTHETIC test data, not real buyers

## Sources

- Van Westendorp, P. (1976). "NSS-Price Sensitivity Meter (PSM) - A new
  approach to study consumer perception of price." Proceedings of the
  ESOMAR 29th Congress, 139-167. Full text:
  https://archive.researchworld.com/a-new-approach-to-study-consumer-perception-of-price/
  Abstract: https://ana.esomar.org/documents/nss-pricesensitivity-meter-psm-
  (Question wording and ordering, don't-know handling, IDP/OPP/PMC/PME
  definitions with the reversed "not cheap"/"not expensive" curves, and
  the "no relation to the optimum-theory" caution are from this paper.)
- R pricesensitivitymeter package, psm_analysis() reference:
  https://search.r-project.org/CRAN/refmans/pricesensitivitymeter/html/psm_analysis.html
  (Original vs "narrower" acceptable_range definitions, response
  validation practice.)
- elucidate (2023). "Van Westendorp Price Sensitivity Meter: Are We Using
  It Incorrectly?" - documents the PMC/PME divergence with worked numbers:
  https://www.elucidatenow.com/resources/van-westendorp-price-sensitivity-meter-are-we-using-it-incorrectly
- Conjointly, "Calculation of Van Westendorp results" (the narrower
  variant's step-by-step):
  https://conjointly.com/guides/manual-calculation-of-van-westendorp/
