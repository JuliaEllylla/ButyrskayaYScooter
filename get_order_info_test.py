#Юлия Бутырская, 10-я когорта - Финальный проект. Инженер по тестированию плюс

import sender_stand_request
import data


def get_order_info_test():
    track = sender_stand_request.create_order(data.order_body).json()['track']
    response = sender_stand_request.order_info_track(track)
    assert response.status_code == 200
