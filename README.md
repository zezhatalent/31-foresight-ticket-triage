# ForeSight Triage — 31-foresight-ticket-triage
### Built on Forethought Pattern

**Category:** Support Intelligence | **Deployment:** Your Server / Forethought Pattern Cloud | **Sector:** Enterprise-ready, India-tuned

---

## Overview

ForeSight Triage packages a production-grade **Forethought Pattern** agent: Predictive ticket routing + confidence

Ships with an **offline demo / dry-run mode** that runs instantly without credentials — the same code path as live, so you validate before spending on API keys. When ready, add one key and the bridge switches to live platform calls.

> **Honest positioning:** This is an implementation package for Forethought Pattern. You get working code, configs, and the exact Forethought Pattern objects to recreate — not a hosted SaaS clone. Offline mode proves the contract.

## Key Features

- **Offline-first design:** Demo with mock data today; flip to live with one env var
- **Config-driven:** Edit `tickets_mock.json` to add intents/queues/policies without touching code
- **Bridge pattern:** `forethought_triage.py` implements the exact webhook/API contract Forethought Pattern expects
- **India-ready:** INR pricing examples, Hinglish utterances, and +91 phone validation where relevant
- **Production guardrails:** Input validation, error handling, and audit-friendly logging built in

## Business Value

| Metric | Before | After |
|--------|--------|-------|
| Time to first demo | Days (platform setup) | Minutes (`python forethought_triage.py`) |
| Vendor lock-in risk | High (black-box SaaS) | Low (you own the bridge + config) |
| Cost to validate | API spend + onboarding calls | Zero (offline) |

## Architecture

```
User / Trigger ──> forethought_triage.py ──> Forethought Pattern API (live) ─┐
                  └─> MOCK engine (offline) ───────────┘─> JSON result -> downstream
Config: tickets_mock.json ───────────────────────────────────────┘
```

## Folder Structure

```
31-foresight-ticket-triage/
├── .gitignore
├── README.md
├── forethought_triage.py
├── requirements.txt
├── tickets_mock.json
├── .env.example      # copy to .env and add live keys
└── README.md         # you are here
```

## Prerequisites

| Requirement | Version | Needed For | Install |
|-------------|---------|------------|---------|
| **Python** | 3.10+ | All agents | `winget install Python.Python.3.12` |
| **Git** | any | Clone repos | `winget install Git.Git` |
| **Python 3.10+** | latest | This agent (only 03/06) | See below |
| **Forethought Pattern account** | — | Live mode only | Client-provided (offline works without) |

Verify Python:
```powershell
python --version   # expect Python 3.12.x
```

## Installation — Step by Step (Proper)

### Step 1 — Clone / Enter Folder
```powershell
git clone https://github.com/zezhatalent/31-foresight-ticket-triage.git
cd 31-foresight-ticket-triage
# or if already local:
cd "D:\SOFTWARE\ANTIGRAVITY\AI AGENTS\31-foresight-ticket-triage"
```

### Step 2 — Create Isolated Environment (first time only)
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
# if blocked: Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

### Step 3 — Install Dependencies
```powershell
pip install -r requirements.txt
# verify:
pip list
```

### Step 4 — Configure Environment
```powershell
copy .env.example .env
notepad .env
```
Fill per table:

| Variable | Required | Notes |
|---|---|---|
| None for offline demo | No | Runs without keys |

> **Never commit `.env`**. It is git-ignored and per-machine.

### Step 5 — Run Offline Demo (no key needed)
```powershell
python forethought_triage.py
```
**Expected:** JSON or table with mock results printed to console (see “Usage Examples” below). No external calls made.

### Step 6 — Run Live Mode (optional, needs key)
```powershell
# after adding key to .env:
python forethought_triage.py        # or: python forethought_triage.py --live
# For webhook services:
# uvicorn forethought_triage:app --port 8000
# then test:
# curl.exe -X POST http://localhost:8000/webhook -H "Content-Type: application/json" -d '{"test": 1}'
```

### Step 7 — Verify
```powershell
python -m py_compile forethought_triage.py
# should print nothing = success
```

## Configuration

- **Primary config:** `tickets_mock.json` — intents, queues, SLA tables, or workflow nodes. Edit and restart; no rebuild.
- **Env file:** `.env` (from `.env.example`) — live keys only. Offline ignores missing keys and uses `MOCK` data in `forethought_triage.py`.
- **Requirements:** `requirements.txt` — pinned minimal deps; stdlib-only folders use a comment stub.

## Usage Examples

### Example 1 — Offline Demo (instant)
```powershell
python forethought_triage.py
# -> {"status":"offline demo","product":"ForeSight Triage"}
```

### Example 2 — Live Call (after .env)
```powershell
python forethought_triage.py --live
# -> live Forethought Pattern API response with real data
```

### Example 3 — As Webhook (if FastAPI service)
```powershell
uvicorn forethought_triage:app --port 8000
curl.exe -X POST http://localhost:8000/webhook -H "Content-Type: application/json" -d '{"message":"hello"}'
```

## How It Works

1. **Config load:** `forethought_triage.py` reads `tickets_mock.json` at startup (policies, prompts, routing tables).
2. **Input ingest:** CLI args or webhook JSON (`/webhook` / `/events`).
3. **Branch:** If env key present → live Forethought Pattern HTTP call; else → deterministic mock.
4. **Output:** Structured JSON + console summary; webhook returns JSON to platform.

## Customization for Your Business

- **Add intents/queues:** Edit `tickets_mock.json` — add rows; scorer auto-picks them.
- **Connect your systems:** Replace `MOCK` dict in `forethought_triage.py` with your API (CRM/ERP/dialer) — contract unchanged.
- **Language:** Add Hinglish variants in config keyword lists; templates already support en/hi.
- **Scale:** Run behind `uvicorn --workers 4` or Docker; stateless so horizontal.

## Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| `ModuleNotFoundError` | venv not activated or deps not installed | Activate `.venv` and `pip install -r requirements.txt` |
| `401 / invalid_api_key` | Wrong or expired key in `.env` | Re-copy from Forethought Pattern dashboard; no quotes/spaces |
| `port already in use` | Another agent on same port | Change `--port` or stop other service |
| Offline demo shows MOCK | No key in `.env` (expected) | Add key and rerun for live |
| `Activate.ps1 cannot be loaded` | PowerShell policy | `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` |

## What’s Included

- Bridge/runtime: `forethought_triage.py` (`2240 bytes`)
- Config: `tickets_mock.json`
- Env template: `.env.example` + dependency list `requirements.txt`
- This README (client-facing sales sheet) + 1 customization session

---

*Offline first, live when ready — ForeSight Triage on Forethought Pattern with India-ready defaults.*
