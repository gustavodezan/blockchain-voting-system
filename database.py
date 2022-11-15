import os
from pathlib import Path
from dotenv import load_dotenv
from deta import Deta

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)

deta = Deta(os.getenv("VOTING_DB_KEY"))
voting_db = deta.Base("voting")