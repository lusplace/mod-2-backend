class CustomUserForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            "username", 
            "first_name", 
            "last_name", 
            "email",
            "password"
            ]