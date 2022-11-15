# Simple decentralized voting system with python

## Goal:
Create a python decentralized voting system with blockchain in a p2p connection
- [x] Blockchain
- [X] Data storage
- [ ] p2p connection

## Specifications:
Python system developed with fastapi framework and data storage on deta

## How to use:
- Install Deta CLI:\
Linux: `curl -fsSL https://get.deta.dev/cli.sh | sh`\
Windows: `iwr https://get.deta.dev/cli.ps1 -useb | iex`

- Create a new project on deta and save it's key

- Create a file named: .env and save the key as: VOTING_DB_KEY={key}

- Install dependencies: `pip install -r requirements.txt`

- Run it locally with: uvicorn main:app --reload
