#!/bin/bash
# SocMed Booster Ultimate - Installation Script

echo "🚀 Installing SocMed Booster Ultimate..."

# Colors
RED='\033[1;31m'
GREEN='\033[1;32m'
YELLOW='\033[1;33m'
BLUE='\033[1;34m'
NC='\033[0m'

echo -e "${BLUE}[1] Updating system...${NC}"
sudo apt-get update && sudo apt-get upgrade -y

echo -e "${BLUE}[2] Installing Python and dependencies...${NC}"
sudo apt-get install -y python3 python3-pip git curl wget

echo -e "${BLUE}[3] Installing Python packages...${NC}"
pip3 install --upgrade pip
pip3 install requests beautifulsoup4 lxml pandas numpy cryptography

echo -e "${BLUE}[4] Cloning repository...${NC}"
git clone https://github.com/darkai-projects/socmed-booster.git
cd socmed-booster

echo -e "${BLUE}[5] Setting up directories...${NC}"
mkdir -p {accounts,logs,results,proxies}

echo -e "${BLUE}[6] Downloading user agents...${NC}"
curl -o user_agents.txt https://raw.githubusercontent.com/darkai-projects/user-agents/main/user_agents.txt

echo -e "${BLUE}[7] Setting permissions...${NC}"
chmod +x socmed_booster.py proxy_manager.py

echo -e "${GREEN}✅ Installation complete!${NC}"
echo -e "${YELLOW}📁 Directory: $(pwd)${NC}"
echo -e "${YELLOW}🚀 Run: python3 socmed_booster.py${NC}"
