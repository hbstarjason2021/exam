
## 
curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.local/bin/env

uv --version 

## 
#sudo apt remove python3-typing-extensions python3-yaml -y 
#pip install  harbor  --break-system-packages --user --ignore-installed pyjwt 

## 
uv tool install harbor

harbor --version
harbor run --help

