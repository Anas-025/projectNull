from django import forms


choices = [
    (0, "Select a format"),
    (1, "UPPERCASE"),
    (2, "lowercase"),
    (3, "Word:3 Count:5")
]


class MyForm(forms.Form):

    text = forms.CharField(label="", help_text="", widget=forms.Textarea(attrs={'placeholder': 'Enter text to transform...'}))
    # formatting = forms.IntegerField(label='Enter number')
    formatting = forms.ChoiceField(label="", choices=choices)
