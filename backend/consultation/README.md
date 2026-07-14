# Consultation AI

The Consultation AI converts English customer enquiry text into deterministic,
structured facts for the current Consultation Engine and future RIP consumers.
It identifies reported symptoms; it does not diagnose medical conditions.

## Public interface

```python
from consultation import ConsultationAnalyzer

analysis = ConsultationAnalyzer().analyze(customer_text)
```

The result uses schema version `1.0`. It includes normalized demographics,
scalp problems, hair-loss symptoms, duration, budget, severity, missing fields,
ambiguities, red flags, and a human-review signal. The legacy `hair_loss`,
`oily_scalp`, `dandruff`, `sensitive_scalp`, and `thinning` booleans remain
available for existing consumers.

## Confidence

`confidence_score` measures how many requested facts were explicitly extracted,
with a penalty for contradictory evidence. It ranges from `0.0` to `1.0`. It is
not diagnostic confidence and must not be used as evidence that a treatment is
appropriate.

## Safety

Messages containing conservative red-flag wording or contradictory extracted
facts set `requires_human_review` to `True`. The recommender then returns no
automatic treatment guidance, and the WhatsApp generator requests professional
review. Red flags are routing indicators, not diagnoses.

## Limitations

- Version 1 supports English text only.
- Rules cannot determine a medical condition or treatment outcome.
- Missing details remain `None` or empty lists; they are never invented.
- Treatment, package, and pricing rules remain separate business policies.

## Tests

From the project root:

```text
PYTHONDONTWRITEBYTECODE=1 python3 -B -m unittest discover -s backend/tests -p 'test_*.py'
```
