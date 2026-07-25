
## 
curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.local/bin/env

uv --version 

## 
sudo apt remove python3-typing-extensions python3-yaml -y 
pip install --pre harbor  --break-system-packages --user --ignore-installed pyjwt 

harbor --version
harbor run --help

