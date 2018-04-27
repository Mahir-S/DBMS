#north
			"""
			if form_north.cleaned_data.get('tier1_demand')!=0:
				try:
					obj=Tickets.objects.get(match=m,stand='North',user=request.user,tier_no=1)
					obj.number=obj.number+form_north.cleaned_data.get('tier1_demand')
					obj.save()
					ob=Match_book.objects.get(match=m,stand='North')
					ob.tier1_availability=ob.tier1_availability-form_north.cleaned_data.get('tier1_demand')
					ob.save()
				except :
					obj=Tickets(match=m,stand='North',tier_no=1,user=request.user,number=form_north.cleaned_data.get('tier1_demand'))
					obj.save()
					ob=Match_book.objects.get(match=m,stand='North')
					ob.tier1_availability=ob.tier1_availability-form_north.cleaned_data.get('tier1_demand')
					ob.save()

			if form_north.cleaned_data.get('tier2_demand')!=0:
				try:
					obj=Tickets.objects.get(match=m,stand='North',user=request.user,tier_no=2)
					obj.number=obj.number+form_north.cleaned_data.get('tier2_demand')
					obj.save()
					ob=Match_book.objects.get(match=m,stand='North')
					ob.tier2_availability=ob.tier2_availability-form_north.cleaned_data.get('tier2_demand')
					ob.save()
				except :
					obj=Tickets(match=m,stand='North',tier_no=2,user=request.user,number=form_north.cleaned_data.get('tier2_demand'))
					obj.save()
					ob=Match_book.objects.get(match=m,stand='North')
					ob.tier2_availability=ob.tier2_availability-form_north.cleaned_data.get('tier2_demand')
					ob.save()



            #north_east
			if form_north_east.cleaned_data.get('tier1_demand')!=0:
				try:
					obj=Tickets.objects.get(match=m,stand='North-east',user=request.user,tier_no=1)
					obj.number=obj.number+form_north_east.cleaned_data.get('tier1_demand')
					obj.save()
					ob=Match_book.objects.get(match=m,stand='North-east')
					ob.tier1_availability=ob.tier1_availability-form_north_east.cleaned_data.get('tier1_demand')
					ob.save()
				except :
					obj=Tickets(match=m,stand='North-east',tier_no=1,user=request.user,number=form_north_east.cleaned_data.get('tier1_demand'))
					obj.save()
					ob=Match_book.objects.get(match=m,stand='North-east')
					ob.tier1_availability=ob.tier1_availability-form_north_east.cleaned_data.get('tier1_demand')
					ob.save()

			if form_north_east.cleaned_data.get('tier2_demand')!=0:
				try:
					obj=Tickets.objects.get(match=m,stand='North-east',user=request.user,tier_no=2)
					obj.number=obj.number+form_north_east.cleaned_data.get('tier2_demand')
					obj.save()
					ob=Match_book.objects.get(match=m,stand='North-east')
					ob.tier2_availability=ob.tier2_availability-form_north_east.cleaned_data.get('tier2_demand')
					ob.save()
				except :
					obj=Tickets(match=m,stand='North-east',tier_no=2,user=request.user,number=form_north_east.cleaned_data.get('tier2_demand'))
					obj.save()
					ob=Match_book.objects.get(match=m,stand='North-east')
					ob.tier2_availability=ob.tier2_availability-form_north_east.cleaned_data.get('tier2_demand')
					ob.save()



            #east
			if form_east.cleaned_data.get('tier1_demand')!=0:
				try:
					obj=Tickets.objects.get(match=m,stand='East',user=request.user,tier_no=1)
					obj.number=obj.number+form_east.cleaned_data.get('tier1_demand')
					obj.save()
					ob=Match_book.objects.get(match=m,stand='East')
					ob.tier1_availability=ob.tier1_availability-form_east.cleaned_data.get('tier1_demand')
					ob.save()
				except :
					obj=Tickets(match=m,stand='East',tier_no=1,user=request.user,number=form_east.cleaned_data.get('tier1_demand'))
					obj.save()
					ob=Match_book.objects.get(match=m,stand='East')
					ob.tier1_availability=ob.tier1_availability-form_east.cleaned_data.get('tier1_demand')
					ob.save()

			if form_east.cleaned_data.get('tier2_demand')!=0:
				try:
					obj=Tickets.objects.get(match=m,stand='East',user=request.user,tier_no=2)
					obj.number=obj.number+form_east.cleaned_data.get('tier2_demand')
					obj.save()
					ob=Match_book.objects.get(match=m,stand='East')
					ob.tier2_availability=ob.tier2_availability-form_east.cleaned_data.get('tier2_demand')
					ob.save()
				except :
					obj=Tickets(match=m,stand='East',tier_no=2,user=request.user,number=form_east.cleaned_data.get('tier2_demand'))
					obj.save()
					ob=Match_book.objects.get(match=m,stand='East')
					ob.tier2_availability=ob.tier2_availability-form_east.cleaned_data.get('tier2_demand')
					ob.save()	


			#south_east

			if form_south_east.cleaned_data.get('tier1_demand')!=0:
				try:
					obj=Tickets.objects.get(match=m,stand='South-east',user=request.user,tier_no=1)
					obj.number=obj.number+form_south_east.cleaned_data.get('tier1_demand')
					obj.save()
					ob=Match_book.objects.get(match=m,stand='South-east')
					ob.tier1_availability=ob.tier1_availability-form_south_east.cleaned_data.get('tier1_demand')
					ob.save()
				except :
					obj=Tickets(match=m,stand='South-east',tier_no=1,user=request.user,number=form_south_east.cleaned_data.get('tier1_demand'))
					obj.save()
					ob=Match_book.objects.get(match=m,stand='South-east')
					ob.tier1_availability=ob.tier1_availability-form_south_east.cleaned_data.get('tier1_demand')
					ob.save()

			if form_south_east.cleaned_data.get('tier2_demand')!=0:
				try:
					obj=Tickets.objects.get(match=m,stand='South-east',user=request.user,tier_no=2)
					obj.number=obj.number+form_south_east.cleaned_data.get('tier2_demand')
					obj.save()
					ob=Match_book.objects.get(match=m,stand='South-east')
					ob.tier2_availability=ob.tier2_availability-form_south_east.cleaned_data.get('tier2_demand')
					ob.save()
				except :
					obj=Tickets(match=m,stand='South-east',tier_no=2,user=request.user,number=form_south_east.cleaned_data.get('tier2_demand'))
					obj.save()
					ob=Match_book.objects.get(match=m,stand='South-east')
					ob.tier2_availability=ob.tier2_availability-form_south_east.cleaned_data.get('tier2_demand')
					ob.save()


			#south
			if form_east.cleaned_data.get('tier1_demand')!=0:
				try:
					obj=Tickets.objects.get(match=m,stand='East',user=request.user,tier_no=1)
					obj.number=obj.number+form_east.cleaned_data.get('tier1_demand')
					obj.save()
					ob=Match_book.objects.get(match=m,stand='East')
					ob.tier1_availability=ob.tier1_availability-form_east.cleaned_data.get('tier1_demand')
					ob.save()
				except :
					obj=Tickets(match=m,stand='East',tier_no=1,user=request.user,number=form_east.cleaned_data.get('tier1_demand'))
					obj.save()
					ob=Match_book.objects.get(match=m,stand='East')
					ob.tier1_availability=ob.tier1_availability-form_east.cleaned_data.get('tier1_demand')
					ob.save()

			if form_east.cleaned_data.get('tier2_demand')!=0:
				try:
					obj=Tickets.objects.get(match=m,stand='East',user=request.user,tier_no=2)
					obj.number=obj.number+form_east.cleaned_data.get('tier2_demand')
					obj.save()
					ob=Match_book.objects.get(match=m,stand='East')
					ob.tier2_availability=ob.tier2_availability-form_east.cleaned_data.get('tier2_demand')
					ob.save()
				except :
					obj=Tickets(match=m,stand='East',tier_no=2,user=request.user,number=form_east.cleaned_data.get('tier2_demand'))
					obj.save()
					ob=Match_book.objects.get(match=m,stand='East')
					ob.tier2_availability=ob.tier2_availability-form_east.cleaned_data.get('tier2_demand')
					ob.save()	
			"""