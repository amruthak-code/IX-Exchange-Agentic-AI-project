"""
Checks that your environment variables are set up correctly.
Run AFTER pasting your Gemini key into .env:
    ./venv/bin/python check_env.py
"""
import os
from dotenv import load_dotenv

load_dotenv()

def status(name, placeholder_hints=()):
    val = os.environ.get(name, "")
    if not val or any(h in val for h in placeholder_hints):
        print(f"  ✗ {name:16} — not set yet")
        return None
    masked = val[:4] + "…" + val[-3:] if len(val) > 8 else "set"
    print(f"  ✓ {name:16} — {masked}")
    return val

print("Environment variables:")
key = status("GEMINI_API_KEY", ("PASTE", "your_gemini"))
status("MYSQL_DATABASE")
status("MYSQL_USER")


if key:
    print("\nTesting Gemini API...")
    try:
        from google import genai
        client = genai.Client(api_key=key)
        resp = client.models.generate_content(
            model="gemini-2.5-flash",
            contents="Reply with exactly: OK",
        )
        print(f"   Gemini replied: {resp.text.strip()}")
        print("\n Gemini is working.")
    except Exception as e:
        print(f"   Gemini call failed: {e}")
else:
    print("\n→ Paste your key into .env (GEMINI_API_KEY and GOOGLE_API_KEY), then re-run.")
