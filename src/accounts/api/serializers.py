
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

from rest_framework import serializers


User = get_user_model()

class UserDisplaySerializer(serializers.ModelSerializer):
    follower_count = serializers.SerializerMethodField()
    url = serializers.SerializerMethodField()
<<<<<<< HEAD

=======
>>>>>>> 95749ba6f1abb5428cb20106f9298bddb642af6f
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'follower_count',
            'url',
            # 'email',
        ]

    def get_follower_count(self, obj):
        return 0

    def get_url(self, obj):
<<<<<<< HEAD
        return reverse_lazy("profiles:detail", kwargs={"username": obj.username})
=======
        return reverse_lazy("profiles:detail", kwargs={"username": obj.username })
>>>>>>> 95749ba6f1abb5428cb20106f9298bddb642af6f

