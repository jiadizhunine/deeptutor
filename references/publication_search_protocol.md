# Publication Search & Disambiguation Protocol

This protocol exists because of a costly past failure: a narrow keyword search found only 8 papers for a professor who actually had 30+, including top-tier journals. The professor had an independent research line AND a collaborative line in a different field, and the narrow search missed the entire collaborative output.

## Step 1: Comprehensive Initial Search (MANDATORY FIRST STEP)

Before any analysis, get the full picture. Do not add field-specific keywords to the initial search.

| Action | How | Why |
|--------|-----|-----|
| PubMed full search | `"Author Full Name" "Institution"` — no field keywords | Scholars often participate in multiple research directions |
| Name variant search | Search ALL variants (see template below) | Chinese scholars use inconsistent romanization across papers |
| Multi-database cross | PubMed + Scopus + Google Scholar + Baidu Scholar | Different databases have different coverage and indexing speed |
| Author ID anchoring | Find Scopus/ORCID/Semantic Scholar Author ID, then search by ID | Far more precise than name-based search |

**Only after the full-count search is done should you proceed to per-paper analysis.**

## Chinese Scholar Name Variant Template

For a scholar with surname "Zhang" and given name "三丰" (Sanfeng), search ALL of these:

```
"Zhang Sanfeng"     (full name, no space in given name)
"Zhang San-Feng"    (hyphenated)
"Zhang SF"           (initials — very common in author lists)
"Zhang S" + institution  (single initial — must pair with affiliation)
"SanFeng Zhang"      (CamelCase, Western order)
"San-Feng Zhang"     (hyphenated, Western order)
"Sanfeng Zhang"      (no space, Western order)
```

Adapt this template for the actual scholar's name. The key insight: PubMed indexes whatever format the journal used, and different journals format differently.

## Step 2: Disambiguation — Include vs Exclude

The goal is to avoid two opposite errors:
- **False inclusion:** attributing someone else's paper to the target
- **False exclusion:** missing the target's real paper because the topic looks unfamiliar

### Include if:
- Author affiliation explicitly matches the target's institution AND department
- Even if the research direction differs from what you already know — scholars have multiple lines (independent + collaborative is the most common pattern)

### Exclude only if:
- Affiliation is in a completely different city/institution/department
- No overlap with any known collaborators
- The research field has zero plausible connection

### Gray zone (affiliation info missing):
- If co-authors overlap with known collaborators → include
- If no co-author overlap and no affiliation → mark as "待确认", do NOT exclude

**The key lesson:** don't use research topic as a filter. A computational researcher can be middle-author on a top-tier experimental paper because they provided analysis support. If the affiliation matches the target's department, it's the same person regardless of whether the paper topic matches their "known" direction.

## Step 3: Publication Gap Verification (6-Step Mandatory Checklist)

Before concluding that a scholar has a publication gap, ALL six steps must be completed:

- [ ] **1. Author ID re-search:** Use Semantic Scholar, ORCID, Scopus Author IDs to search again
- [ ] **2. Broad PubMed search:** `"Name" + institution` with NO field restriction — browse all results manually
- [ ] **3. All name variants:** Search every variant from the template above
- [ ] **4. Collaborator new papers:** Search for recent papers by known students and co-authors (the target may be a middle author)
- [ ] **5. Cross-database verification:** Verify with at least 3 independent databases (PubMed, Semantic Scholar/OpenAlex, Baidu Scholar/CNKI)
- [ ] **6. Funding check:** Search for recent grant reports or mid-term reviews (may reference unpublished work)

**Only when ALL six steps return no new findings can you conclude there's a genuine gap.**

## Illustrative Failure Scenarios

### Scenario A: Over-disambiguation (narrow search misses collaborative output)
- Narrow keyword search for a computational biology professor: only 8 papers found
- Broad PubMed search with just name + institution: 39 results returned
- After careful review: ~30 papers confirmed, including collaborations in top-tier journals (IF > 10)
- Root cause: the professor had two research lines (independent statistical analyses + collaborative experimental research with a clinical department), and the narrow search missed the entire collaborative line
- Wrong conclusion initially reached: "3-year publication gap" — actually had papers every year

### Scenario B: Under-disambiguation (common name floods results)
- PubMed search with a common two-character surname + initial + institution: 200+ results
- Only 2-3 belonged to the target researcher
- Root cause: extremely common name; needed field-specific keywords + Author ID to filter
- Wrong conclusion initially reached: "publication gap" because recent papers were buried among hundreds from other scholars with the same abbreviated name
