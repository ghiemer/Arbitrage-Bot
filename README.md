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

### 4. Configuration
- Copy `.env.example` to `.env` and fill in your API keys, Telegram credentials, etc.
- Edit `config/pairs.yaml` to define your token pairs and spread settings.
- Edit `config/chains.yaml` to adjust chain-specific RPC endpoints if needed.

### 5. Run the bot
```bash
python main.py
```
- In **dryrun** mode, no real swaps are executed, but alerts and logs are generated.
- For live trading: set `MODE=live` in your `.env` and make sure your private keys are secure!

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
