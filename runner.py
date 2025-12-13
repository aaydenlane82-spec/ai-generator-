import json, os
from datetime import datetime
from ai_client import generate_upgrade

state = json.load(open("state.json")) if os.path.exists("state.json") else {"runs": 0}
state["runs"] += 1

prompt = f"Run #{state['runs']}: Give ONE world-changing AI upgrade idea. Be concise."
result = generate_upgrade(prompt)

print(f"🤖 Run #{state['runs']}\n{result}")

state["last_run"] = datetime.utcnow().isoformat()
json.dump(state, open("state.json", "w"))
