from brownie import FundMe
from scripts.helpful_scripts import get_accounts


def fund_account():
    fund_me = FundMe[-1]
    entrance_fee = fund_me.getEntranceFee()
    account = get_accounts()
    fund_me.fund({"from": account, "value": entrance_fee})
    print(f"Contract funded with {entrance_fee} wei.")


def withdraw():
    fund_me = FundMe[-1]
    account = get_accounts()
    fund_me.withdraw({"from": account})


def main():
    fund_account()
    withdraw()
