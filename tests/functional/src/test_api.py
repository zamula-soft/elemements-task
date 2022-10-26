from http import HTTPStatus
import json
import pytest
import random
from elements.models import ImageData

pytestmark = pytest.mark.asyncio


async def test_get_images(make_get_request):
    response = await make_get_request('/images')

    result = response.body['result']
    assert response.status == HTTPStatus.OK
    assert len(result) == 8


async def test_get_image_by_id(make_get_request):
    items = list(ImageData.objects.all())
    random_image_data = random.choice(items)
    response = await make_get_request(f"/images/{random_image_data.id}")
    assert response.status == HTTPStatus.OK
    assert response.body["title"] == random_image_data.title
    assert response.body["description"] == random_image_data.description
    assert response.body["image"] == random_image_data.image
