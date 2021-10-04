from collections import OrderedDict as odict #ordered dictionary would be useful for sorting later

#authors = ["J. K. Rowling", "w. s.", "lewis carroll", "M. M."]
authors = ["J. L.", "J. B. priestley", "L. C.", "Suzanne Collins"]
authors_dict = {} #a bunch of source data and variables

for author in authors:
	splited_a = author.split() #splts list of authors into singular records
	x = 0
	counted_splited_a = []
	for sp_a in splited_a: #splits records of authors, measuring them, uppers letters for further sorting, and gather into arrays
		counted_splited_a.append(sp_a.upper()) 
		x = x + len(sp_a)
	if x == 4: #fills dictionary of authors and the crusial sorting variables
		authors_dict.update({counted_splited_a[0]:author})
	else:
		authors_dict.update({counted_splited_a[-1]:author})

sort_authors = odict(sorted(authors_dict.items())).values() 
print(sort_authors)

