import configuration
import requests

def create_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=order_body)


def order_info_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_TRACK_PATH + str(track))
