from django import forms
from .models import Auction
from django.utils import timezone

class AuctionForm(forms.ModelForm):
    class Meta:
        model = Auction
        fields = ['jewelry', 'start_time', 'end_time']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Giới hạn queryset của jewelry chỉ hiển thị các jewelry có trạng thái 'APPROVED'
        self.fields['jewelry'].queryset = self.fields['jewelry'].queryset.filter(
            status='APPROVED', 
            seller_approved=True
        )
        self.fields['start_time'].widget = forms.DateTimeInput(attrs={'type': 'datetime-local'})
        self.fields['end_time'].widget = forms.DateTimeInput(attrs={'type': 'datetime-local'})
    def clean(self):
        cleaned_data = super().clean()
        start_time = cleaned_data.get("start_time")
        end_time = cleaned_data.get("end_time")

        if start_time and end_time:
            if start_time >= end_time:
                self.add_error('end_time', "End time must be greater than start time.")

            if end_time <= timezone.now():
                self.add_error('end_time', "End time must be in the future.")

        return cleaned_data