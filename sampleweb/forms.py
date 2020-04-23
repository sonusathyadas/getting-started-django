from sampleweb.models import Todo
from django import forms

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title', 'is_done',) # added_date is not required, it is added by code when submitted
