# Static Next.js export remediation notes

Use when editing a deployed/static-exported Next.js site without the original source tree.

## Key lesson

Editing `index.html` alone is often not enough. Static Next exports include hydrated React/RSC payloads and route chunks under `_next/static/chunks/...`; the browser may render stale text from those chunks even when the HTML source has been patched.

## Workflow

1. Back up the export first:
   ```bash
   ditto -c -k --sequesterRsrc --keepParent site-dir site-dir-backup.zip
   ```
2. Patch both visible HTML files and route mirror/payload files (`*.txt`, route chunks, layout chunks) with scripted replacements.
3. Search for old strings across `*.html`, `*.txt`, and `*.js`:
   ```bash
   python3 - <<'PY'
   from pathlib import Path
   root=Path('site-dir')
   terms=['old phrase 1','old CTA','old page title']
   files=list(root.rglob('*.html'))+list(root.rglob('*.txt'))+list(root.rglob('*.js'))
   for term in terms:
       hits=[str(p.relative_to(root)) for p in files if term in p.read_text(errors='ignore')]
       print(term, len(hits), hits[:10])
   PY
   ```
4. If route chunks are modified, cache-bust by renaming the modified chunk and updating all references. Otherwise the browser/CDN may keep serving stale code.
5. Verify no broken JS references:
   ```bash
   python3 - <<'PY'
   from pathlib import Path
   import re
   root=Path('site-dir')
   missing=[]
   for p in list(root.rglob('*.html'))+list(root.rglob('*.txt'))+list(root.rglob('*.js')):
       s=p.read_text(errors='ignore')
       for m in re.findall(r'/_next/static/[^"\']+\.js', s):
           if not (root/m.lstrip('/')).exists():
               missing.append((str(p.relative_to(root)), m))
   print('missing js refs', missing[:10], len(missing))
   PY
   ```
6. Serve locally and verify rendered DOM, not just source:
   ```bash
   cd site-dir
   python3 -m http.server 8765
   ```
   Use browser DOM/snapshot checks and cache-busting query strings (`?v=2`, `?v=3`) to confirm the live rendered text changed.
7. Zip the updated export for deployment:
   ```bash
   ditto -c -k --sequesterRsrc --keepParent site-dir site-dir-updated.zip
   ```

## Pitfalls

- Broad text replacements can corrupt filenames or chunk hashes (e.g. replacing a numeric/string token inside `_next/static/...js`). Always run the missing-reference check.
- Browser snapshots can show stale hydrated content even when `curl` shows the patched HTML. Inspect loaded script URLs and route chunks.
- Static fallback form attributes are less important if the route chunk contains a real `onSubmit` handler. Verify the hydrated form handler and field names in the DOM.
- Prefer original Next source when available. Static export patching is a tactical workaround, not the clean long-term workflow.
