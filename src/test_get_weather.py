from get_weather import make_report


def test_make_report_gives_correct_sentence():
    fake_weather = {"city": "Dubai", "temperature": 30, "wind": 10}
    result = make_report(fake_weather)
    assert result == "In Dubai it is 30 °C, with wind at 10 km/h."