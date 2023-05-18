# Main

	$ mainpage
	$ about
	$ map
	$ search

# News

	Article
	- title
	- preview
	- photo
	- content
	- categories (ManyToMany to Category)
	- likes (ManyToMany to Profile)

	Category
	- title

	ArticleComment
	- content
	- likes
	- date

	$ news
	$ category
	$ article/№

# Literature

	Author
	- name
	- alias
	- date_of_birth
	- date_of_death
	- preview
	- content
	- photo
	- genres (ManyToMany to Genre)
	- works (ManyToMany to Work)

	AuthorComment
	- author (FK to Author)
	- user (FK to User)
	- content
	- date
	- likes (ManyToMany to Profile)

	Genre
	- title
	- preview
	- content
	- photo

	GenreComment
	- content
	- date
	- likes (ManyToMany to Profile)

	Work
	- title
	- preview
	- content
	- photo
	- genres (ManyToMany to Genre)
	- authors (ManyToMany to Author)

	WorkComment
	- content
	- date
	- likes (ManyToMany to Profile)


	$ authors
	$ author/#

	$ works
	$ work/#

	$ genres
	$ genre/#

# Members

	Profile
	- user (FK to User)
	- avatar
	- bio
	- newsLikes (ManyToMany to News.Article)
	- authorLikes (ManyToMany to Literature.Author)
	- genreLikes (ManyToMany to Literature.Genre)
	- workLikes (ManyToMany to Literature.Work)

	$ user/№
	$ edit_user
	$ login
	$ register
	$ change_password
	$ send_email
	$ email_sent
	$ set_password
	$ done