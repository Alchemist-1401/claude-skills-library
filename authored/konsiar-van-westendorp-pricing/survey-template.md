# Konsiar pricing survey (Van Westendorp) - questionnaire template

## Intro shown to every respondent - EDIT BEFORE FIELDING

The paragraph below is a placeholder draft. Confirm the exact feature and
package description with the user before fielding; do not field an
invented feature list.

> Konsiar is a subscription tool for small businesses. It reads incoming
> Instagram and WhatsApp customer messages and replies automatically in
> the business's own voice. It comes with a live demo and a free two-week
> trial.

## Screening (keep only yes-answers)

S1. Do you run or manage a business that gets customer enquiries through
Instagram or WhatsApp DMs? (Yes / No)

## The four Van Westendorp questions (in this order)

Each answer is a monthly price in USD. Numeric entry, any non-negative
amount, no upper limit. Never suggest, pre-fill, or show example prices.
Offer an explicit "I don't know" option and record it separately.

Q1. At what monthly price would you begin to experience Konsiar as too
    cheap - so that you say "at this price the quality cannot be good"?
    $ ____ / month

Q2. At what monthly price would you begin to experience Konsiar as too
    expensive - so that you would never consider it yourself?
    $ ____ / month

Q3. At what monthly price are you beginning to experience Konsiar as
    expensive?  $ ____ / month

Q4. At what monthly price are you beginning to experience Konsiar as
    cheap (a bargain for the money)?  $ ____ / month

## Data handling

Export one row per respondent with columns:
too_cheap, cheap, expensive, too_expensive (from Q1, Q4, Q3, Q2).
"Don't know" answers are excluded from the CSV but their count is
reported alongside the results - the level of "don't know" indicates
general price-consciousness. Keep the rejection count the analysis
script reports - it is part of the result.
