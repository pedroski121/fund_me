from brownie import accounts, network, config, MockV3Aggregator

DECIMALS = 8
STARTING_PRICE = 2000000000000
LOCAL_DEVELOPMENT_ENVIRONMENT = ["ganache-local","development"]

def get_accounts():
    if network.show_active() in LOCAL_DEVELOPMENT_ENVIRONMENT:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def deploy_mocks():
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE,{"from":get_accounts()})
        print("Mocks deployed")
