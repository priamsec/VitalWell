SEO Quick-Edit Plan for boldly-balanced

Goal: Make the boldly-balanced site SEO-friendly with non-destructive, safe edits and a governance cadence.

1) Inventory snapshot (documented in this file)
- Target: all HTML/MD/MDX/JSX under ~/.openclaw/shared/boldly-balanced
- Deliverable: list of crawled pages and gaps

2) Technical fixes (non-destructive)
- Canonical URLs: add rel="canonical" tag to pages lacking them
- Meta tags: ensure each page has unique title and meta description; generate defaults based on page content
- Open Graph: add basic og:title, og:description, og:url on pages
- Robots & Sitemap: ensure robots.txt exists and references sitemap.xml; generate a basic sitemap.xml if missing
- Accessibility: ensure images have alt text; ensure semantic headings; ARIA as fallback if needed
- Structured data: add lightweight JSON-LD for FAQ/Article on applicable pages
- Mobile: verify responsive layout hints (meta viewport, flexible widths)

3) On-page optimization
- Headings: ensure proper H1 per page, then H2/H3 hierarchy
- Internal linking: add context-rich internal links where relevant
- Content freshness: flag thin/duplicate content; propose refresh

4) Governance & cadence
- Create a 2-week SEO content calendar draft (topics, owners, cadence)
- Commit changes via micro-Edits.md and a plan to review weekly

5) Artifacts to deliver
- Updated micro-Edits.md with concrete edits
- robots.txt (basic) at site root
- sitemap.xml (basic) at site root
- Optional: a template for meta description and title generation

Usage notes:
- These are safe, non-destructive edits intended for immediate improvement. All changes should be reviewable in Git and reversible.
