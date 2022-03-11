from rest_framework import serializers

from .models import Women, Genre, Category

"""class WomenSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    cat_id = serializers.IntegerField()

    def create(self, validated_data):
        return Women.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.content = validated_data.get("content", instance.content)
        instance.time_update = validated_data.get("time_update", instance.time_update)
        instance.is_published = validated_data.get("is_published", instance.is_published)
        instance.cat_id = validated_data.get("cat_id", instance.cat_id)
        instance.save()
        return instance"""


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name')

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def validate(self, attrs):
        return attrs


class WomenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Women
        fields = "__all__"
        read_only_fields = ['user']

    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get("title", instance.title)
    #     instance.content = validated_data.get("content", instance.content)
    #     instance.time_update = validated_data.get("time_update", instance.time_update)
    #     instance.is_published = validated_data.get("is_published", instance.is_published)
    #     instance.cat_id = validated_data.get("cat_id", instance.cat_id)
    #     instance.save()
    #     return instance

    def create(self, validated_data):
        women, created = Women.objects.get_or_create(user=self.context.get('request').user, **validated_data)
        return women

    # def validate(self, attrs):
    #     women = Women.objects.all()
    #     for a in women:
    #         print(a.content)
    #
    #     print(attrs)
    #     return attrs


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'women', 'name', 'parent')

    def validate(self, attrs):
        print(attrs['parent'])
        return attrs

    def create(self, validated_data):
        return Genre.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.women = validated_data.get("women", instance.women)
        instance.name = validated_data.get("name", instance.name)
        instance.parent = validated_data.get("parent", instance.parent)
        instance.save()
        return instance


class GenreListSerializer(serializers.ModelSerializer):
    women = WomenSerializer(read_only=True)

    class Meta:
        model = Genre
        fields = ('id', 'women', 'name', 'parent')

    # def create(self, validated_data):
    #     return Genre.objects.create(user=self.context.get('request').user, **validated_data)