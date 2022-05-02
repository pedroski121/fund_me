from scripts.helpful_scripts import get_accounts, LOCAL_DEVELOPMENT_ENVIRONMENT
from scripts.deploy import deploy_fundme
from brownie import accounts, network, exceptions
import pytest


def test_fund_and_withdraw():
    account = get_accounts()
    fund_me = deploy_fundme()
    entrance_fee = fund_me.getEntranceFee()
    fund_me.fund({"from": account, "value": entrance_fee})
    amount_funded = fund_me.addressToAmountFunded(account)
    assert amount_funded == entrance_fee
    fund_me.withdraw({"from": account})
    assert fund_me.addressToAmountFunded(account) == 0


def test_only_owner_can_withdraw():
    if network.show_active() not in LOCAL_DEVELOPMENT_ENVIRONMENT:
        pytest.skip("only for testing")
    fund_me = deploy_fundme()
    hacker = accounts.add()
    with pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdraw({"from": hacker})
