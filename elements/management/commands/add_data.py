from io import BytesIO
import os
import requests
import pandas as pd
from django.core.management.base import BaseCommand

from celery.utils.log import get_task_logger
from elements.models import ImageData

FILE_PATH = "https://docs.google.com/spreadsheet/ccc?key=0Aqg9JQbnOwBwdEZFN2JKeldGZGFzUWVrNDBsczZxLUE&single=true&gid" \
            "=0&output=csv&urp=gmail_link "
CHUNK_SIZE = 100

columns = [
    "title",
    "description",
    "image"
]


class Command(BaseCommand):
    def handle(self, *args, **options):
        logger = get_task_logger(__name__)
        logger.info("The process of adding data begins.")

        self.stdout.write("The process of adding data begins.")

        req = requests.get(FILE_PATH)
        csv_data = req.content

        ImageData.objects.all().delete()

        for df in pd.read_csv(BytesIO(csv_data), index_col=False, names=columns,
                              skiprows=1, header=None, chunksize=CHUNK_SIZE):
            for row in df.itertuples():
                ImageData.objects.create(
                    id=row[0],
                    title=row[1],
                    description=row[2],
                    image=row[3]
                )

