from rest_framework import serializers
from django.contrib.auth import get_user_model
from .send_sms import send_activation_sms

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, max_length=20, required=True, write_only=True)
    password_confirmation = serializers.CharField(min_length=6, max_length=20, required=True, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'password_confirmation', 'first_name', 'last_name', 'username', 'avatar')

    def validate(self, attrs):
        password = attrs['password']
        password_confirmation = attrs.pop('password_confirmation')

        if password != password_confirmation:
            raise serializers.ValidationError('Passwords do not match')

        if password.isdigit() or password.isalpha():
            raise serializers.ValidationError('Password must contain letters and numbers')

        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class ActivationSerializer(serializers.Serializer):
    activation_code = serializers.CharField(required=True)

    def validate(self, attrs):
        self.activation_code = attrs['activation_code']
        return attrs

    def save(self, **kwargs):
        try:
            user = User.objects.get(activation_code=self.activation_code)
            user.is_active = True
            user.activation_code = ''
            user.save()
        except:
            self.fail('Incorrect activation code')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password', 'groups')


class RegisterPhoneSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, max_length=20, write_only=True, required=True)
    password_confirmation = serializers.CharField(min_length=6, max_length=20, write_only=True, required=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'avatar', 'phone_number', 'password', 'password_confirmation',
                  'first_name', 'last_name')

    def validate(self, attrs):
        password = attrs['password']
        password_confirmation = attrs.pop('password_confirmation')

        if password != password_confirmation:
            raise serializers.ValidationError('Passwords do not match')

        if password.isdigit() or password.isalpha():
            raise serializers.ValidationError('Password must contain letters and numbers')

        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        send_activation_sms(user.phone_number, user.activation_code)
        return user

