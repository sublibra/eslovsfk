#!/bin/bash
pip install selenium
pip install pysftp
pip install decouple
# brew install geckodriver # macos
## Raspberry
wget https://github.com/mozilla/geckodriver/releases/download/v0.23.0/geckodriver-v0.23.0-arm7hf.tar.gz
tar -xvzf geckodriver-v*
chmod +x geckodriver
sudo cp geckodriver /usr/local/bin/