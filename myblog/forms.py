from django import forms
from .models import Post, Category, Comment


# # Hardcoding categories
# choices = [('coding', 'coding'), ('sports', 'sports'),
#            ('entertainment', 'entertainment')]
choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category',
                  'body', 'snippet', 'header_image')

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter a Blog Title'
                }),
            'title_tag': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter a Title Tag'
                }),
            # 'author': forms.Select(attrs={
            #     'class': 'form-control'
            #     }),
            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'value': '',
                'id': 'user_identifier',
                'type': 'hidden'
                }),
            'category': forms.Select(choices=choice_list, attrs={
                'class': 'form-control'
                }),
            'body': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Type Your Post'
                }),
            'snippet': forms.Textarea(attrs={
                'class': 'form-control'
                }),
        }

        
class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body', 'snippet')

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter a Blog Title'
                }),
            'title_tag': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter a Title Tag'
                }),
            'body': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Type Your Post'
                }),
            'snippet': forms.Textarea(attrs={
                'class': 'form-control'
                }),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
