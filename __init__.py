# pyDeFiTools/__init__.py
# This file will initialize the library and import necessary modules.

from .protocols import aave, compound, uniswap
from .yield_farming import get_yield_farming_opportunities
from .staking import stake_tokens, unstake_tokens
from .lending import lend_tokens, borrow_tokens
from .portfolio import get_portfolio_value, get_portfolio_risk
from .risk_assessment import assess_risk
