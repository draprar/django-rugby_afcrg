from django.utils import timezone
from django.urls import reverse
from django.test import Client
from django.contrib.auth.models import User
from archive.models import Post
from archive.apps import ArchiveConfig
import pytest


@pytest.mark.django_db
class TestPostModel:
    def test_create_post(self):
        user = User.objects.create(username="testuser")
        post = Post.objects.create(
            author=user,
            title="Test Post",
            text="This is a test post.",
            created_date=timezone.now(),
        )
        assert post.title == "Test Post"
        assert post.text == "This is a test post."
        assert post.published_date is None

    def test_publish_post(self):
        user = User.objects.create(username="testuser")
        post = Post.objects.create(
            author=user,
            title="Publish Test Post",
            text="Publishing test post.",
            created_date=timezone.now(),
        )
        post.publish()
        assert post.published_date is not None
        assert post.published_date <= timezone.now()


@pytest.mark.django_db
class TestPostListView:
    def setup_method(self):
        self.client = Client()

    def test_post_list_view_with_posts(self):
        user = User.objects.create(username="testuser")
        Post.objects.create(
            author=user,
            title="Test Post",
            text="This is a test post.",
            published_date=timezone.now(),
        )
        url = reverse("post_list")
        response = self.client.get(url)
        assert response.status_code == 200
        assert "posts" in response.context
        assert len(response.context["posts"]) == 1

    def test_post_list_view_no_posts(self):
        url = reverse("post_list")
        response = self.client.get(url)
        assert response.status_code == 200
        assert "posts" in response.context
        assert len(response.context["posts"]) == 0

    def test_404_view(self):
        response = self.client.get("/nonexistent-page/")
        assert response.status_code == 200
        assert "Strona nie istnieje" in response.content.decode("utf-8")


class TestArchiveConfig:
    def test_app_name(self):
        assert ArchiveConfig.name == "archive"
        assert isinstance(ArchiveConfig.default_auto_field, str)
        assert ArchiveConfig.default_auto_field == "django.db.models.BigAutoField"
