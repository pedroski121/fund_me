from brownie import FundMe, config,MockV3Aggregator
from scripts.helpful_scripts import get_accounts, deploy_mocks,LOCAL_DEVELOPMENT_ENVIRONMENT, network


def deploy_fundme():
    account = get_accounts() 

    if network.show_active() not in LOCAL_DEVELOPMENT_ENVIRONMENT:
        price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    print(f"Price feed address is {price_feed_address}")
    fund_me = FundMe.deploy(price_feed_address, {"from": account})
    print(f"Contract deployed to {fund_me.address}")

    return fund_me


def main():
    deploy_fundme()
