from django import forms


from .models import Article, Comment


class ArticleModelForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'title',
            'content',
        ]


class CommentModelForm(forms.ModelForm):

    class Meta:
        model=Comment
        fields=[
            'content',
        ]
        labels = {
            "content": "Leave a comment:"
        }
        widgets = {
            'content': forms.Textarea(attrs={'rows':5, 'cols':2})
        }
