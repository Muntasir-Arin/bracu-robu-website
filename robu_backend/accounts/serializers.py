from djoser.serializers import UserCreateSerializer
from accounts.models import User
from rest_framework import serializers
from django.core.signing import TimestampSigner
from django.conf import settings
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
import threading
import hashlib
from urllib.parse import urlencode

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ( "email", 'name', 'is_verified', 'date_of_birth', 'insta_link', 'position', 'robu_department','is_admin', 'student_id', 'secondary_email', 'phone_number', 'rs_status', 'facebook_profile', 'linkedin_link', 'bracu_start' , 'blood_group', 'gender', 'org', 'avatar')
        read_only_fields = ('robu_department','is_admin','position', 'is_verified')

class UserNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'is_verified')
        read_only_fields = ('name', 'is_verified')       

class RobuSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class PublicUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'name', 'date_of_birth', 'student_id',
                  'position', 'department', 'avatar', 'rs_status', 'facebook_profile', 'linkedin_link',
                  'robu_start', 'robu_end', 'blood_group', 'gender',  'org')



class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'name', 'org', 'password')

    def create(self, validated_data):
        user = super().create(validated_data)
        user.is_verified = False
        user.save()
        threading.Thread(target=self.send_verification_email, args=(user,)).start()
        return user

    def send_verification_email(self, user):
        signer = TimestampSigner()
        user_id = urlsafe_base64_encode(force_bytes(user.id))
        token = signer.sign(user_id)
        user.verification_token = token
        user.avatar = self.gravatar_url(user.email)
        user.save()
        subject = 'Verify your email'
        message = render_to_string('email/verification_email.html', {'user': user, 'token': token})
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [user.email]
        send_mail(subject, message, from_email, recipient_list, html_message=message, fail_silently=True)
        print('Email sent')
    
    def gravatar_url(self, email):
        default = "https://i.imgur.com/p50u9jD.jpeg"  # Default image URL
        email_encoded = email.lower().encode('utf-8')
        email_hash = hashlib.sha256(email_encoded).hexdigest()
        params = urlencode({'d': default})  # Using default image if no Gravatar is found
        return f"https://www.gravatar.com/avatar/{email_hash}?{params}"


class PanelSerializer(serializers.Serializer):
    year = serializers.IntegerField()
    president = serializers.IntegerField()
    vp = serializers.IntegerField()
    ags = serializers.IntegerField()
    gso = serializers.IntegerField()
    gsa = serializers.IntegerField()