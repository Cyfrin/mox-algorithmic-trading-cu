# ------------------------------------------------------------------
#                     PORTFOLIO ALLOCATIONS
# ------------------------------------------------------------------
class Allocation:
    def __init__(self, token, percentage):
        self.token = token
        self.percentage = percentage

    def __str__(self):
        return f"{self.token} = {self.percentage}"


PORTFOLIO_ALLOCATIONS = [Allocation("USDC", 0.3), Allocation("ETH", 0.7)]
BUFFER = 0.1
