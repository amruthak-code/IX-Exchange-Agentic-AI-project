# IDX Exchange — Agentic AI Project

A multi-agent real estate AI assistant built on the [OpenClaw](https://github.com/openclaw/openclaw)
runtime, over two MLS datasets in MySQL. Part of the IDX Exchange AI Agentic Engineer
internship (12-week program).

## Stack

- **OpenClaw** — multi-channel AI gateway / agent runtime
- **Google Gemini** — LLM provider
- **MySQL** — `idx_exchange` database (active listings + sold comps)
- **Python** — data access, embeddings, analytics

## Setup

1. **Clone & enter the project**
   ```bash
   git clone https://github.com/amruthak-code/IDX-Exchange-Agentic-AI-project.git
   cd IDX-Exchange-Agentic-AI-project
   ```

2. **Python environment**
   ```bash
   python3 -m venv venv
   ./venv/bin/pip install -r requirements.txt
   ```

3. **Environment variables** — copy the template and fill in your values:
   ```bash
   cp .env.example .env
   ```
   - `GEMINI_API_KEY` — get one free at https://aistudio.google.com/apikey
   - `MYSQL_*` — your local MySQL connection
   - `EMAIL_*` — only needed from Week 11

4. **Database** — import the MLS `.sql` dumps (not included in this repo) into the
   `idx_exchange` schema, then verify:
   ```bash
   mysql -u idx_user -p idx_exchange < sql/verify.sql
   ```

## Verify your setup

```bash
./venv/bin/python check_env.py   # checks env vars + live-tests Gemini
./venv/bin/python test_db.py     # confirms Python <-> MySQL connection
```

## Not in this repo (intentionally)

- `.env` — secrets
- `sql/*.sql` raw datasets — too large; provided separately
- `openclaw/` — install via `npm install -g openclaw`
- The internship handbook PDF — confidential
