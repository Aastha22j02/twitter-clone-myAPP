from rest_framework import serializers
from userAuth.models import userAuthModal


# Create serilizers for UserAuth

class userAuthSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = userAuthModal
        fields = "__all__"
