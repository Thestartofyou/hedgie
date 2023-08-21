class HedgeFund:
    def __init__(self, name, strategy):
        self.name = name
        self.strategy = strategy
        self.investors = []

    def add_investor(self, investor_name):
        self.investors.append(investor_name)

class Investor:
    def __init__(self, name, net_worth):
        self.name = name
        self.net_worth = net_worth
        self.investments = []

    def make_investment(self, hedge_fund_name):
        self.investments.append(hedge_fund_name)

def main():
    hedge_funds = [
        HedgeFund("Fund A", "Equity Long/Short"),
        HedgeFund("Fund B", "Global Macro"),
        HedgeFund("Fund C", "Fixed Income")
    ]

    investors = [
        Investor("Investor X", 5000000),
        Investor("Investor Y", 8000000),
        Investor("Investor Z", 10000000)
    ]

    # Simulate investors making investments in hedge funds
    investors[0].make_investment("Fund A")
    investors[0].make_investment("Fund B")

    investors[1].make_investment("Fund B")
    investors[1].make_investment("Fund C")

    investors[2].make_investment("Fund A")
    investors[2].make_investment("Fund C")

    # Associate investors with their investments in hedge funds
    for investor in investors:
        for hedge_fund in hedge_funds:
            if hedge_fund.name in investor.investments:
                hedge_fund.add_investor(investor.name)

    # Display information about hedge funds and their investors
    for hedge_fund in hedge_funds:
        print(f"{hedge_fund.name} ({hedge_fund.strategy}):")
        print("Investors:")
        for investor_name in hedge_fund.investors:
            print(f"  {investor_name}")
        print()

if __name__ == "__main__":
    main()

