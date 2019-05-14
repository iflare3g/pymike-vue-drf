from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    author = serializers.CharField()
    title = serializers.CharField()
    description = serializers.CharField()
    body = serializers.CharField()
    location = serializers.CharField()
    publication_date = serializers.DateField()
    draft = serializers.BooleanField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        """
        Creates and returns a new Article instance based on validated_data
        """
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Updates and returns a new updated
        Article instance based on validated_data
        """
        instance.author = validated_data.get("author", instance.author)
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.body = validated_data.get("body", instance.body)
        instance.location = validated_data.get("location", instance.location)
        instance.draft = validated_data.get("draft", instance.draft)
        instance.publication_date = validated_data.get(
            "publication_date", instance.publication_date
        )

        instance.save()
        return instance

    def validate(self, data):
        if data["title"] == data["description"]:
            raise serializers.ValidationError(
                "Title and Description must be different!"
            )
        return data

    def validate_title(self, value):
        if len(value) < 60:
            raise serializers.ValidationError("Title has min-length set to 60 chars")
        return value
