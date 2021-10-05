from django.db import models


class ProjectModel(models.Model):
    CLASS_CHOICES = [
        ("BE", "BE"),
        ("TE", "TE"),
        ("SE", "SE"),
    ]

    project_Year = models.IntegerField(
        choices=[(r, r) for r in range(2015, 2026)], default=2021
    )
    project_Class = models.CharField(max_length=2, choices=CLASS_CHOICES, default="BE")
    project_Members = models.CharField(max_length=500)
    project_Title = models.CharField(max_length=500)
    project_Mentor = models.CharField(max_length=100)
    project_Abstract = models.CharField(max_length=2000)
    project_Publication = models.CharField(max_length=300)
    project_Domain = models.CharField(
        max_length=300, default="Big Data Analytics and Machine Learning"
    )
    project_Video = models.CharField(max_length=400, default="")

    def __str__(self) -> str:
        return f"{self.project_Title} : {self.project_Year}, {self.project_Class}"
