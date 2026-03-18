---
name: python_38_compat
description: Repo must remain compatible with Python 3.8
type: project
---

This repo must stay compatible with Python 3.8. Avoid syntax or stdlib features added in 3.9+ (e.g., `dict | dict` union, `list[int]` generics, `str.removeprefix`/`str.removesuffix`, `zoneinfo`, etc.).

**Why:** Explicit user requirement.
**How to apply:** Before using any Python feature, verify it exists in 3.8. When in doubt, check the docs or use a 3.8-safe alternative.
