# Run stuff


# Create venv
python3 -m venv venv/

# Activate venv
source venv/bin/activate

# Update pip
pip install --upgrade pip

# Create requirements.txt
touch requirements.txt

# Install requirements.txt
pip install -r requirements.txt

# Deactivate venv
deactivate

# Actualizar requirements
pip freeze > requirements.txt

# pip and venv problems?
rm -rf venv && rm -rf __pycache__ && rm -rf .vscode && python3 -m venv venv/ && source venv/bin/activate && pip install --upgrade pip 



# Info about more commands
https://realpython.com/comparing-python-command-line-parsing-libraries-argparse-docopt-click/

