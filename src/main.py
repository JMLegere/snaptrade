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
    
    


if __name__ == "__main__":
    main()