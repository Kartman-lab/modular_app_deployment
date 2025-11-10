from django.urls import reverse, resolve


def test_letting_index_url():
    path = reverse("lettings:index")
    assert path == "/lettings/"
    assert resolve(path).view_name == "lettings:index"


def test_letting_detail_url():
    path = reverse("lettings:letting", kwargs={"letting_id": 1})
    assert path == "/lettings/1/"
    assert resolve(path).view_name == "lettings:letting"
