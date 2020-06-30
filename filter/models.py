from django.db import models

class FinOption(models.Model):
    InstName = models.CharField(max_length=100, blank=True)
    InstType = models.CharField(max_length=100, blank=True)
    InstCategory = models.CharField(max_length=100, blank=True)
    InstPartnerStatus = models.CharField(max_length=100, blank=True)
    Status = models.CharField(max_length=100, blank=True)
    ThemeKeySubsector = models.CharField(max_length=2000, blank=True)
    ThemeArea = models.CharField(max_length=300, blank=True)
    FilterThematicArea = models.CharField(max_length=100, blank=True)
    ThemeTarget = models.CharField(max_length=300, blank=True)
    ThemePlannedAllocations = models.CharField(max_length=300, blank=True)
    OptionFinancingOption = models.CharField(max_length=300, blank=True)
    FilterFinancingOption = models.CharField(max_length=100, blank=True)
    OptionAidModalities = models.CharField(max_length=300, blank=True)
    OptionTenor = models.CharField(max_length=100, blank=True)
    OptionTenorYears = models.CharField(max_length=100, blank=True)
    OptionFundTitle = models.CharField(max_length=300, blank=True)
    EligibilityApplicants = models.CharField(max_length=2000, blank=True)
    EligibilityGov = models.CharField(max_length=100, blank=True)
    FilterEligble = models.CharField(max_length=100, blank=True)
    EligibilityNonGov = models.CharField(max_length=200, blank=True)
    EligibilityCriteria = models.CharField(max_length=2000, blank=True)
    EligibilityProjectType = models.CharField(max_length=1000, blank=True)
    EligibilityProjectValueRange = models.CharField(max_length=300, blank=True)
    EligibilityProjectPreparationLevel = models.CharField(max_length=300, blank=True)
    ApplicationProcessDates = models.CharField(max_length=500, blank=True)
    ApplicationProcessSteps = models.CharField(max_length=2000, blank=True)
    ApplicationProcessDuration = models.CharField(max_length=300, blank=True)
    ApplicationProcessPotentiality = models.CharField(max_length=100, blank=True)
    ContactRecommendations = models.CharField(max_length=100, blank=True)
    ContactComment = models.CharField(max_length=500, blank=True)
    ContactWebsite = models.CharField(max_length=300, blank=True)
    ContactGuidelinesDownload = models.CharField(max_length=300, blank=True)
    ContactEmail = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.InstName

class ThematicArea(models.Model):
    ThematicArea = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.ThematicArea

class Eligibility(models.Model):
    Eligibility = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.Eligibility

class FinancingOption(models.Model):
    FinancingOption = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.FinancingOption