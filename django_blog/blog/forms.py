from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Profile
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']


User = get_user_model()

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email')

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'profile_photo')
class CommentForm(forms.ModelForm):
content = forms.CharField(
label="",
widget=forms.Textarea(attrs={
"rows": 3,
"placeholder": "Write your comment..."
}),
max_length=5000,
)


class Meta:
model = Comment
fields = ["content"]


def clean_content(self):
data = self.cleaned_data["content"].strip()
if not data:
raise forms.ValidationError("Comment cannot be empty.")
return data
