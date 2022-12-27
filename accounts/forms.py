from django import forms
from django.core.exceptions import ValidationError

from accounts.models import Payment, Profile


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['amount', 'transaction_code']
        # or: exclude = ['profile', 'transaction_time']

    def clean(self):
        super().clean()
        amount = self.cleaned_data.get('amount')
        code = self.cleaned_data.get('transaction_code')
        if amount is not None and code is not None:
            if int(code.spilit('-')[1]) != amount:
                raise ValidationError('مبلغ و رسید تراکنش با هم همخوانی ندارند')

    def clean_amount(self):
        """
        Represents that amount has to be positive and multiple of 1000
        """
        amount = self.cleaned_data.get('amount')
        if amount < 0:
            raise ValidationError('باید مثبت باشد')
        elif amount % 1000 != 0:
            raise ValidationError('مقدار تراکنش باید مضربی از هزار تومان باشد')
        return amount

    def clean_transaction_code(self):
        """
        Checking format of transaction_code
        """
        code = self.cleaned_data.get('transaction_code')
        try:
            assert code.startswith('bank-')
            assert code.endswith('#')
            parts = code.split('-')
            assert len(parts) == 3
            int(parts[1])
        except:
            raise ValidationError('قالب رسید تراکنش معتبر نیست')
        return code


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['mobile', 'gender', 'address', 'profile_image']
