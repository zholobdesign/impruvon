# Impruvon — website structure prototype

A clickable, link-complete prototype of the Impruvon website. **Wireframe only — no visual
design.** Its job is to let the client walk the whole site, see every page, and understand
where each button leads and why.

- Every page is real and linked. Nothing is a dead end.
- The **Show notes** button in the top bar reveals the reasoning behind each page:
  what it is for, who reads it, and what still needs a decision from the client.
- **Sitemap** in the top bar lists every page, the conversion logic, and the open questions.
- Items marked PENDING are waiting on the client (sources, clearances, contact details).

## Structure

Home · Platform (eMAR+, MedBox, Pharmacy, EHR, HRST) · Who we serve (5 verticals) ·
Compare · Pricing · Trust · Resource Center (Supporting DSPs, Guides, Customer stories) ·
About (Story, Commitment, Careers, Contact) · Book a demo · Log in · Sitemap

## Build

```bash
python3 build.py      # regenerates ./docs (served by GitHub Pages)
```

Content is sourced from the Impruvon Discovery Dossier (Stages 1–5) and the
Website Copy v1 draft. Prepared by Toggle.
