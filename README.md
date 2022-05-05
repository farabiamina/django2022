# django2022
1. Description: The book review project – simple online book review, books will be taken from book-store websites like “meloman”. Users can make publications of book reviews, licenses, comments in book-discussions. 
Models: User, Book, Comments, Publication, License, general abstract class for License and Comment, Author, Article.
You can find description and comments for the books, maybe you want to write the license. Also you can read different articles about authors and so on.
Main functions are related to publications, they are editing, posting, deleting. Get will be the main function because the website is a read-site.
2. class diagram: src="https://user-images.githubusercontent.com/78636367/166850695-9f238822-0132-438d-b778-ac17de988b8e.png"
3. Minimum 6 models: Profile, Author, Genre, Publisher, Book, Publications, Comment, Licanse, Article
   Model inheritense: Profile -> Author; Publications -> Comment, Article, License
   Abstract Models: User(build-in), Publications
4. 4/4 Model Managers 
5. 7/6 relations (ForeignKey)
6. JWT Auth
7. Srializers: 
    a. 2/2 serializers.Serializer
    b. 9/2 serializers.ModelSerializer
    c. 4/4 serializer inheritence
    d. nested serializers
8. Views: 2/2 fbv, 4/4 cbv, 5/6 viewsets
9. Logging module
10. Postman requests with all methods
11. GitHub repository
