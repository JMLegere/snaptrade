import os
import uuid
from pprint import pprint
from snaptrade_client import SnapTrade

def main():
    snaptrade = SnapTrade(
        consumer_key="X9dfpfcBTpoU4vj7NA0a7WUSjTVkXR37QxboBOMflrTixwLPKH",
        client_id="JEREMYLEGERE",
    )

    api_response = snaptrade.api_status.check()
    pprint(api_response.body)
    
    user_id = str (uuid.uuid4())
    register_response = snaptrade.authentication.register_snap_trade_user(
        body={"userId": user_id}
    )
    pprint(register_response.body)
    
    user_secret = register_response.body["userSecret"]
    redirect_uri = snaptrade.authentication.login_snap_trade_user(
        query_params={"userId": user_id, "userSecret":user_secret}
    )
    pprint(redirect_uri.body)
    snaptrade.portfolio_management.create(
        query_params = {
            "userId": user_id,
            "userSecret": user_secret,
        },
        body = {
            "id": str(uuid.uuid4()),
            "name": "MyPortfolio"
        },
    )
    res = snaptrade.portfolio_management.list(
    query_params={"userId": user_id, "userSecret": user_secret}
    )
    pprint(res.body)
    
    holdings = snaptrade.account_information.get_all_user_holdings(
        query_params={"userId": user_id, "userSecret": user_secret}
    )
    pprint(holdings.body)
    
    deleted_response = snaptrade.authentication.delete_snap_trade_user(
    query_params={"userId": user_id}
    )
    pprint(deleted_response.body)

if __name__ == "__main__":
    main()