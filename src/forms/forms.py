from django import forms

from .models import Post
################################################FORM 1######
class PostModelForm(forms.ModelForm):
    class Meta: #It means that data which is not field
        model = Post
        fields = ["user", "title", "image"]
        exclude = []




################################################FORM 2######
BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
    ('db-value','Display-value ')
]
INTS_CHOICES = [tuple([x,x]) for x in range(0,100)]

YEAR = [x for x in range(1980,2040)]
class TextData(forms.Form):
    some_date = forms.DateField(label="Enter your year", initial="2010-02-12", widget=forms.SelectDateWidget(years=YEAR))
    some_text = forms.CharField(label="Enter your name", widget = forms.Textarea(attrs={"rows":4, "cols":10}))
    integer = forms.IntegerField(initial=12) #Initial Value of integer = 12
    boolean = forms.BooleanField()
    email = forms.EmailField()
    choices = forms.CharField(label="options", widget=forms.Select(choices = INTS_CHOICES))
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    favorite_colors = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=FAVORITE_COLORS_CHOICES,
    )

    def __init__(self, *args, **kwargs):
        super(TextData, self).__init__(*args, **kwargs)
        self.fields['email'].initial = "test@test.com"   #Initial Value of email

    def clean_some_text(self, *args, **kwargs):
        some_data = self.cleaned_data.get("some_text")
        if len(some_data) < 10:
            raise forms.ValidationError("Ensure size of data is more than 10")
        return some_data

    def clean_integer(self, *args, **kwargs):
        integer = self.cleaned_data.get("integer")
        if integer < 10:
            raise forms.ValidationError("Integer greater than 10")
        return integer