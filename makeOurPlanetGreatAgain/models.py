from django.db import models

LICENSES = [('CC', 'CC'),
            ('libre droit', 'libre droit'),
            ('tous droits réservés', 'tous droits réservés'),
            ]


class File(models.Model):
    id = models.ImageField()
    license = models.CharField(max_length=50, choices=LICENSES)


class User(models.Model):
    idUser = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=255)
    adress = models.CharField(max_length=255)
    mail = models.CharField(max_length=255)
    file = models.ForeignKey(File, on_delete=models.CASCADE, related_name='files')


class Demandeur(models.Model):
   idRole = models.CharField(max_length=50, primary_key=True)
   user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')


class Expert(models.Model):
   idRole = models.CharField(max_length=50, primary_key=True)
   user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
   karma = models.IntegerField()


class Financeur(models.Model):
   idRole = models.CharField(max_length=50, primary_key=True)
   user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
   type = models.CharField(max_length=255)


class Projet(models.Model):
    idProject = models.CharField(max_length=255, primary_key=True)
    projectName = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    budget = models.IntegerField()
    note = models.IntegerField()
    demandeur = models.OneToOneField(Demandeur, on_delete=models.CASCADE)
    Expert = models.OneToOneField(Expert, on_delete=models.CASCADE)
    Financeur = models.OneToOneField(Financeur, on_delete=models.CASCADE)
    fichier = models.ForeignKey(File, on_delete=models.CASCADE, related_name='files')




class Meta:
    db_table = "Projet"
    db_table = "Financeur"
    db_table = "File"
    db_table = "User"
    db_table = "Demandeur"
    db_table = "Expert"
