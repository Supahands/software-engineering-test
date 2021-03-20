require 'yaml'
PYNAME = 'seed.py'.freeze
python_output = `python3 #{PYNAME}`

timestamps = YAML.safe_load(python_output)

