from django.db import models
class Mem():
    pass
class Tag():
    pass
class Sphere():
    pass

class User(models.Model):
    Nickname = models.CharField(max_length = 100)
    Birth_Date = models.DateField()
    Education = models.CharField(max_length = 100)
    Sex = models.IntegerField()
    Area_of_Interests = models.CharField(max_length = 100)


    def __str__(self):
        return self.Nickname

class Source(models.Model):
    Name = models.CharField(max_length = 100)
    Format = models.CharField(max_length = 100)
    Rating = models.IntegerField()

    user = models.ManyToManyField(User)

    def __str__(self):
        return self.Name

class Creator(models.Model):
    Nickname = models.CharField(max_length = 100)
    Popularity = models.IntegerField()
    Relation_to_Memes = models.CharField(max_length = 100)

    User = models.ForeignKey(User, on_delete=models.CASCADE)

    source = models.ManyToManyField(Source)

    def __str__(self):
        return self.Nickname

class Mem(models.Model):
    Name = models.CharField(max_length = 100)
    Birth_Date = models.DateField()
    Popularity_Dynamics = models.CharField(max_length = 100)
    Existence_of_Creator = models.IntegerField()
    Localisation = models.CharField(max_length = 100)
    Picture = models.CharField(max_length=500)

    Creator = models.ForeignKey(Creator, on_delete=models.CASCADE)

    source = models.ManyToManyField(Source)
    Mem.User_watches_Mem = models.ManyToManyField(User)
    is_liked_by_user = models.ManyToManyField(User)

    def __str__(self):
        return self.Name
class Tag(models.Model):
    Name = models.CharField(max_length = 100)
    Frequence_of_usage = models.CharField(max_length = 100)

    Tag.User = models.ForeignKey(User, on_delete=models.CASCADE)

    mem = models.ManyToManyField(Mem)
    user = models.ManyToManyField(User)

    def __str__(self):
        return self.Name

class Sphere(models.Model):
    Theme = models.CharField(max_length = 100)
    Relevance = models.CharField(max_length = 100)
    Depth = models.IntegerField()


    source = models.ManyToManyField(Source)
    mem = models.ManyToManyField(Mem)
    tag = models.ManyToManyField(Tag)
    def __str__(self):
        return self.Theme

'''
class Sphere_Source(models.Model):
    Sphere_id = models.ForeignKey(Sphere)
    Source_id = models.ForeignKey(Source)

class Sphere_Mem(models.Model):
    Sphere_id = models.ForeignKey(Sphere)
    Mem_id = models.ForeignKey(Mem)

class Mem_Tag(models.Model):
    Mem_id = models.ForeignKey(Mem)
    Tag_id = models.ForeignKey(Tag)

class Sphere_Tag(models.Model):
    Sphere_id = models.ForeignKey(Sphere)
    Tag_id = models.ForeignKey(Tag)

class User_Source(models.Model):
    User_id = models.ForeignKey(User)
    Source_id = models.ForeignKey(Source)

class User_Watches_Mem(models.Model):
    User_id = models.ForeignKey(User)
    Mem_id = models.ForeignKey(Mem)

class User_likes_Mem(models.Model):
    User_id = models.ForeignKey(User)
    Mem_id = models.ForeignKey(Mem)

class Creator_Source(models.Model):
    Creator_id = models.ForeignKey(Creator)
    Source_id = models.ForeignKey(Source)

class User_Tag(models.Model):
    User_id = models.ForeignKey(User)
    Tag_id = models.ForeignKey(Tag)
'''
