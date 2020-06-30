from django.db.models import Q
from django.shortcuts import render
from .models import FinOption, ThematicArea, Eligibility, FinancingOption

def home(request):
    qs = FinOption.objects.all()
    ta = ThematicArea.objects.all()
    el = Eligibility.objects.all()
    fo = FinancingOption.objects.all()
    totalcount = FinOption.objects.all().count()


    org_contains_query = request.GET.get('org_contains')
    keyword_query = request.GET.get('keyword')
    thematicArea_query = request.GET.get('thematicArea_select')
    eligibility_query = request.GET.get('eligibility_select')
    financingOption_query = request.GET.get('financingOption_select')

    if org_contains_query != '' and org_contains_query is not None:
        print(financingOption_query)
        qs = qs.filter(InstName__icontains=org_contains_query)

    if keyword_query != '' and keyword_query is not None:
        qs = qs.filter(Q(ThemeKeySubsector__icontains=keyword_query) | Q(ThemeArea__icontains=keyword_query) | Q(ThemeTarget__icontains=keyword_query)).distinct()

    if thematicArea_query != '' and thematicArea_query is not None and thematicArea_query != 'Choose thematic area ...':
        qs = qs.filter(FilterThematicArea__icontains=thematicArea_query)
    
    if eligibility_query != '' and eligibility_query is not None and eligibility_query != 'Choose eligibility ...':
        qs = qs.filter(FilterEligble__icontains=eligibility_query)

    if financingOption_query != '' and financingOption_query is not None and financingOption_query != 'Choose financing option ...':
        qs = qs.filter(FilterFinancingOption__icontains=financingOption_query)

    selectedcount = qs.count()

    context = {
        'queryset': qs,
        'tas' : ta,
        'els' : el,
        'fos' : fo, 
        'totalcount' : totalcount,
        'selectedcount': selectedcount
    }

    return render(request, 'main.html', context)

