from django.test import TestCase
from .models import EHR, Documents
# Create your tests here.

class EHRTestCase(TestCase):
    def setUp(self):
        ehr = EHR.objects.create(
            user_id=1,
            date_time="2023-01-01 12:00:00",
            folder_id=1,
            folder_name="Example Folder",
            parent_id=0,
            priority=1
        )
        Documents.objects.create(
            ehr_id=ehr,
            file=b'PDF_CONTENT_IN_BINARY_FORMAT'
        )

    def test_document_count(self):
        ehr = EHR.objects.get(folder_name="Example Folder")
        document_count = Documents.objects.filter(ehr_id=ehr).count()
        self.assertEqual(document_count, 1)

    def test_document_content(self):
        ehr = EHR.objects.get(folder_name="Example Folder")
        document = Documents.objects.get(ehr_id=ehr)
        self.assertEqual(document.file, b'PDF_CONTENT_IN_BINARY_FORMAT')

