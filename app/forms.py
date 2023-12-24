from django import forms


choices = [
    (0, "--select--"),
    (1, "uppercase"),
    (2, "lowercase"),
    (3, "word count")
]


class MyForm(forms.Form):

    text = forms.CharField(label='Enter text', max_length=10)
    # formatting = forms.IntegerField(label='Enter number')
    formatting = forms.ChoiceField(choices=choices)
