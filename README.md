Trading Bot — Binance Futures Testnet (USDT-M)
A clean, production-structured Python CLI application that places Market, Limit, and Stop-Limit orders on the Binance Futures Testnet. Built with a clear separation between the API/client layer and the CLI layer, structured logging, and robust error handling.

Project Structure
trading_bot/
├── bot/
│   ├── __init__.py
│   ├── client.py        # Binance API wrapper (client/API layer)
│   ├── orders.py        # Order placement logic (business layer)
│   └── validators.py    # Input validation
├── logs/
│   ├── market_order.log # Sample MARKET order log
│   ├── limit_order.log  # Sample LIMIT order log
│   └── trading_bot.log  # Live rotating log (auto-created on first run)
├── cli.py               # CLI entry point
├── logging_config.py    # Shared logger factory
├── requirements.txt
├── .env.example
└── README.md
Setup
1. Clone / download the project
git clone <repo-url>
cd trading_bot
2. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate        # Linux / macOS
venv\Scripts\activate           # Windows
3. Install dependencies
pip install -r requirements.txt
4. Configure Binance Testnet credentials
Register at https://testnet.binancefuture.com and generate API keys.

cp .env.example .env
# Edit .env and fill in your keys
Or export them directly:

export BINANCE_API_KEY=your_key_here
export BINANCE_API_SECRET=your_secret_here
Note: The bot auto-loads .env via python-dotenv if present.

How to Run
All commands are run from the trading_bot/ directory.

Place a MARKET order
# BUY 0.01 BTC at market price
python cli.py place --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01

# SELL 0.1 ETH at market price
python cli.py place --symbol ETHUSDT --side SELL --type MARKET --quantity 0.1
Place a LIMIT order
# BUY 0.01 BTC with a limit price of $60,000
python cli.py place --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.01 --price 60000

# SELL 0.1 ETH with a limit price of $3,200
python cli.py place --symbol ETHUSDT --side SELL --type LIMIT --quantity 0.1 --price 3200
Place a STOP-LIMIT order (Bonus)
# BUY 0.01 BTC: trigger at $64,500, execute at $65,000
python cli.py place --symbol BTCUSDT --side BUY --type STOP_LIMIT \
    --quantity 0.01 --price 65000 --stop-price 64500
Check account balance
python cli.py account
Get help
python cli.py --help
python cli.py place --help
Example Output
── Order Request Summary ──────────────────────────
  Symbol     : BTCUSDT
  Side       : BUY
  Type       : MARKET
  Quantity   : 0.01
───────────────────────────────────────────────────

── Order Response ─────────────────────────────────
  Order ID      : 3274651892
  Status        : FILLED
  Executed Qty  : 0.01
  Avg Price     : 64823.50
  Client OID    : x-testnet-abc123
───────────────────────────────────────────────────

✓ Order placed successfully!
Logging
Console — INFO level and above: clean, human-readable output.
File — DEBUG level and above: full request/response detail, stored in logs/trading_bot.log (rotating, max 5 MB × 3 backups).
Sample log files for a MARKET order and a LIMIT order are included in logs/.

Assumptions
The bot targets the USDT-M Perpetual Futures testnet only (https://testnet.binancefuture.com).
Quantity precision and minimum notional requirements depend on the symbol. The testnet is generally more lenient than mainnet.
STOP_LIMIT maps to Binance's STOP order type with both price and stopPrice fields.
Credentials are read from environment variables or a .env file — never hard-coded.
Evaluation Checklist
Criteria	Implementation
Places MARKET & LIMIT orders on Testnet	bot/orders.py + bot/client.py
BUY and SELL supported	--side BUY|SELL
CLI with argparse	cli.py
Clear output (request + response)	_print_order_summary / _print_order_response
Structured code (client vs CLI layer)	bot/client.py vs cli.py
Logging to file	logging_config.py
Exception handling	bot/orders.py + bot/client.py
Validation	bot/validators.py
Log files included	logs/market_order.log, logs/limit_order.log
Bonus: Stop-Limit order type	STOP_LIMIT in validators + client + CLI
Dependencies
Package	Purpose
binance-futures-connector	Official Binance UM Futures Python SDK
python-dotenv	Load credentials from .env file
