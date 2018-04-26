 from book.models import Match,Match_book
 a=['North','North-east','East','South-East','South','South-West','West','North-West'] def populates(id):
    g=Match.objects.get(match_no=id)
    for st in a:
        data=Match_book(match=g,stand=st)
        data.save()
