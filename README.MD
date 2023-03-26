# News

	News
	- title
	- preview
	- photo(ManyToMany)
	- content
	- category (ForeignKey to Category)

	Category
	- title
	- subcategory (ForeignKey to Category (use django-polymorphic))

	Comment
	- sub (ForeignKey to Comment)
	- content
	- photo

	$ news
	$ category
	$ article/№

# Literature

	Author
	- name
	- preview
	- content
	- photo (ManyToMany)
	- genres (ManyToMany to Genre)
	- works (ManyToMany to Work)

	Work
	- title
	- preview
	- content
	- photo
	- genre (ManyToMany to Genre)
	- author (ForeignKey to Author)

	Genre
	- title
	- description

	Comment
	- sub (ForeignKey to Comment)
	- content
	- photo

	$ authors
	$ works
	$ genre
	$ author/№
	$ work/№

# Members

	User
	- likes (add likes field)
	- photo (add photo field)

	$ main
	$ about
	$ user/№
	$ map
	$ search