# ⚠️ This application is still in development. Use at your own risk! Features, APIs, and security may change at any time.

# Arbitrage Bot (Async, Python 3.11+, Docker-ready)

A fully asynchronous, modular starter framework for crypto arbitrage bots on EVM-compatible chains.

## Features
- **Async/await**: Fast price polling & parallel tasks
- **Modular**: Each core module in its own file
- **Dryrun/Live mode**: Safe testing without risk
- **Docker-ready**
- **Telegram notifications**
- **CSV logging**
- **Easy extensibility**

## Directory Structure
```
.
├── main.py
├── scheduler.py
├── provider.py
├── price_scanner.py
├── spread_analyzer.py
├── gas_manager.py
├── profit_calc.py
├── swap_simulator.py
├── swap_executor.py
├── risk_guard.py
├── logger.py
├── notifier.py
├── config
│   ├── chains.yaml
│   └── pairs.yaml
├── .env.example
├── requirements.txt
├── README.md
└── .gitignore
```

## Setup

### 1. Install Python 3.11+ (recommended: via pyenv)

### 2. Clone the repository
```bash
git clone <repo-url>
cd Arbitrage_Bot
```

### 3. Create a virtual environment and install dependencies
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 4. Configure Environment Variables
- Copy `.env.example` to `.env` and fill in all required keys as described below.
- Edit `config/pairs.yaml` to define your token pairs and spread settings.
- Edit `config/chains.yaml` to adjust chain-specific RPC endpoints if needed.

## Environment Variables: How to Obtain All Required Keys

Below is a guide for each key in your `.env` file:

### 1. DEXSCREENER_API
- **Default:** `https://api.dexscreener.io/latest/dex/pairs`
- **No key needed.** This is a public endpoint.

### 2. ONEINCH_API
- **Default:** `https://api.1inch.dev/swap/v5.2`
- **API Key required for higher rate limits.**
- **How to get:**
  - Register at [1inch Developer Portal](https://portal.1inch.dev/).
  - Create a new app/project to get your API key.
  - You may need to append your key as a header or query param depending on 1inch’s docs.

### 3. ALCHEMY_KEY
- **How to get:**
  - Go to [Alchemy](https://dashboard.alchemy.com/).
  - Sign up and create a new app for each chain you want (e.g., Ethereum, Polygon, Arbitrum).
  - Copy the HTTP API key and paste it here.

### 4. QUICKNODE_KEY
- **How to get:**
  - Go to [QuickNode](https://www.quicknode.com/).
  - Sign up and create a new endpoint for your desired chain (e.g., BSC, Polygon, etc.).
  - Copy the HTTP Provider key and paste it here.

### 5. MODE
- **Options:** `dryrun` or `live`
- **Set to `live` only if you want to execute real trades and have set up all keys securely.**

### 6. MIN_PROFIT_USD
- **Set your minimum profit threshold in USD.**

### 7. TELEGRAM_TOKEN
- **How to get:**
  - Open Telegram and search for `@BotFather`.
  - Start a chat and use `/newbot` to create a new bot.
  - Copy the token provided by BotFather.

### 8. TELEGRAM_CHAT_ID
- **How to get:**
  - Add your bot to a group or use it in a private chat.
  - Send a message to the bot.
  - Use the [getUpdates API](https://api.telegram.org/bot<YOUR_TOKEN>/getUpdates) to find your chat ID, or use a Telegram tool/bot like `@userinfobot`.

### 9. PRIVATE_KEY
- **How to get:**
  - Export the private key from your wallet (e.g., MetaMask, TrustWallet).
  - **Warning:** Never share or commit this key! Use only for test wallets unless you know what you’re doing.

## Usage
- The bot will continuously scan prices, analyze spreads, simulate swaps, and (in live mode) execute trades.
- All trades are logged to `trades.csv`.
- Alerts are sent via Telegram if configured.
- Adjust the logic in each module to fit your strategy or integrate new DEXs/APIs.

## Module Overview
- **main.py**: Entry point, orchestrates all modules
- **provider.py**: RPC management & failover
- **scheduler.py**: Parallel task management
- **price_scanner.py**: Price polling (DexScreener)
- **spread_analyzer.py**: Spread calculation & profitability check
- **gas_manager.py**: Gas price polling
- **profit_calc.py**: Net profit calculation
- **swap_simulator.py**: 1inch dryrun simulation
- **swap_executor.py**: (Stub) Transaction execution
- **risk_guard.py**: Blacklisting on errors
- **logger.py**: CSV logging
- **notifier.py**: Telegram alerts

## Configuration
- **.env**: API keys, mode, Telegram, etc.
- **config/chains.yaml**: Chain-specific RPCs
- **config/pairs.yaml**: Token pairs & spread settings

## Security
- **Never commit your private keys!**
- `.env` and `trades.csv` are protected by `.gitignore`.

## TODO: Steps for a Production-Ready Version
- [ ] Integrate real second-DEX price sources (e.g., 1inch quotes) in `process_tick`
- [ ] Implement atomic router contract and integrate in `swap_executor.py`
- [ ] Replace 1inch dryrun with Tenderly simulation for accurate slippage checks
- [ ] Add error handling and retry logic for all network calls
- [ ] Add unit and integration tests for all modules
- [ ] Implement monitoring/dashboard (e.g., FastAPI + Grafana) for latency and PnL visualization
- [ ] Add Dockerfile and CI/CD pipeline for automated deployment
- [ ] Harden security (key management, secrets, etc.)
- [ ] Add support for more DEXs and chains
- [ ] Optimize for gas and latency

## License
MIT
