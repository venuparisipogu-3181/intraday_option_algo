from truedata_ws.websocket.TDWebSocket import TDWebSocket

td = None

def connect_truedata():
    global td
    if td is None:
        td = TDWebSocket(
            login_id="YOUR_ID",
            password="YOUR_PASSWORD"
        )
        td.start_live_data()
    return td
