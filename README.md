# password-generator
This is a project with Vue and Fastapi to create secure passwords

# Run backend
### Create env

python -m venv venv

### Activate env

venv/Scripts/Activate.ps1

### Install dependencies

pip install -r .\requirements.txt

### Run project

uvicorn main:app --reload

# Run Frontend

### Install dependencies

npm install

### Run project

npm run dev

# Run both projects

./run-both.sh
