# Domain Migration Plan

This document describes the steps to move the `interuista` project under the
PythonMilano GitHub organization and configure GitHub Pages with a custom domain.

## Current State

- Repository: `keobox/interuista`
- GitHub Pages URL: `https://keobox.github.io/interuista`
- `publishconf.py` SITEURL: `https://keobox.github.io/interuista`

## Phase 1: Transfer repository to PythonMilano

1. Go to `https://github.com/keobox/interuista` -> **Settings** -> **General**
2. Scroll to **Danger Zone** -> click **Transfer repository**
3. Select **PythonMilano** as the new owner
4. Confirm the transfer

After transfer:
- The repo will be at `https://github.com/PythonMilano/interuista`
- GitHub automatically redirects the old URL
- You keep contributor access

## Phase 2: GitHub Pages on the org subpath

After the transfer, GitHub Pages will serve the site as a **project site** under
the PythonMilano organization.

Since `PythonMilano/pythonmilano.github.io` uses the custom domain `milano.python.it`,
the site will be available at: `https://milano.python.it/interuista`

Update `publishconf.py`:

```python
SITEURL = "https://milano.python.it/interuista"
```

This is the interim setup until the custom domain is ready.

## Phase 3: Custom domain (`intervistapythonista.com`)

When ready to use the dedicated domain:

### 1. Configure DNS

At your domain registrar for `intervistapythonista.com`, add one of:

**Option A - CNAME (recommended for apex or www):**

| Type  | Name | Value                      |
|-------|------|----------------------------|
| CNAME | @    | pythonmilano.github.io     |

Note: some registrars don't support CNAME on apex domains. In that case use Option B
or set up the CNAME on `www` and redirect apex to www.

**Option B - A records (for apex domain):**

| Type | Name | Value            |
|------|------|------------------|
| A    | @    | 185.199.108.153  |
| A    | @    | 185.199.109.153  |
| A    | @    | 185.199.110.153  |
| A    | @    | 185.199.111.153  |

Optionally add a CNAME for `www`:

| Type  | Name | Value                        |
|-------|------|------------------------------|
| CNAME | www  | pythonmilano.github.io       |

### 2. Configure GitHub Pages custom domain

1. Go to `https://github.com/PythonMilano/interuista` -> **Settings** -> **Pages**
2. Under **Custom domain**, enter `intervistapythonista.com`
3. Click **Save** (this creates a `CNAME` file in the repo)
4. Wait for DNS to propagate (can take up to 24-48 hours)
5. Check **Enforce HTTPS** once the DNS check passes

### 3. Update Pelican configuration

Update `publishconf.py`:

```python
SITEURL = "https://intervistapythonista.com"
```

### 4. Verify

- `https://intervistapythonista.com` serves the site
- HTTPS works correctly
- The org site `milano.python.it` is unaffected

## Notes

- Each project repo under an organization can have its own independent custom domain,
  it won't conflict with `milano.python.it` on the org site.
- If you want a personal fork after the transfer, you can fork it back to your
  personal account from PythonMilano.
