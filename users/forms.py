from django import forms

from blog.models import Post


class PostForm(forms.ModelForm):
    """Форма для создания и редактирования статей."""
    class Meta:
        model = Post
        fields = ["title", "text", "publish"]
        # Убрать поля exclude = [""]