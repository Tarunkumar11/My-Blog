                                    #Bloglane

BlogLane Lets you create and publish blogs and comment, as your authenticated self. Forgot your password?Reset it. Not sure about a Comment/Post? Store it as a draft for now. Written in python(Django), BlogLane is an open-source blogging website.<br /><br />
![FoxitReader_x8MiFSTPNg](https://user-images.githubusercontent.com/50740247/118387454-3f3a2400-b63c-11eb-929b-1a3467704f98.png)

The Database,As depicted above in Fig 1. has been arranged into tables as follows:<br />
#1 Auth User Table has 5 columns which are name, Username & Alias(Primary key), Email and your password which is ​PBKDF2 encrypted.<br />
#2 Blog Post Table stores all the published/draft blogs with author_id as foregin key linked to Auth User Table to know to which blog belongs to which author.<br />
#3 Comment Table has each comment ever made with ​post_id as foregin key. Attribute approved_comment ​let’s us know if the comment is a draft or a published comment.<br />
#4 Query  Stores customer feedback in Real Time. It contains 4 attributes and Email is one of its attributes which is used to send responses through email.<br />

<br />
#View
<br />
![FoxitReader_WOKqkTOiMN](https://user-images.githubusercontent.com/50740247/118387484-68f34b00-b63c-11eb-8aa6-0c44c280e4eb.png)

<br />
<br />

Key Features include<br/><br/>
-User Registration with a unique username (as it is the primary key in ​Auth User Table​).<br/>
-And security checks on password length and it being different from the users’ username has been applied.<br/>
-Date act’s is a differentiation between published and drafted posts/comments.<br/>
-Editing of a blog which is posted by the user edits are authentication centric and user edits the content row in the ​Blog Post Table​.<br/>
-Password reset uses SMTP .i.e. using gmail as a domain name to send password reset links via email.
