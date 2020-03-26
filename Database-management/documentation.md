# Database Documentation

The books database for datascience is a PostgreSQL instance hosted on Amazon Web Services RDS.

## Tables schemata

### Table: "authors": 733,0339 rows
Primary key: AuthorID

| Label    	| Type       	|
|----------	|------------	|
| Name     	| text       	|
| Works    	| text array 	|
| key      	| text       	|
| AuthorID 	| serial     	|

### Table: "editions": 26,574,661 rows
Primary key: EditionID

| Label            	| Type       	|
|------------------	|------------	|
| EditionTitle     	| text       	|
| Authors          	| text array 	|
| Genre            	| text array 	|
| Subjects         	| text array 	|
| PublishedYear    	| text       	|
| Publisher        	| text       	|
| Pages            	| integer    	|
| Ratings          	| integer    	|
| Popularity       	| integer    	|
| Reviews          	| text array 	|
| OriginalLanguage 	| text array 	|
| Nationality      	| text       	|
| Translators      	| text array 	|
| WorkTitles        | text array  |
| Works             | text array  |
| Languages         | text array  |
| ISBN13            | text        |
| EditionID         | serial      |

### Table: "works": 18,572,829 rows
Primary key: WorkID

| Label            	| Type       	|
|------------------	|------------	|
| WorkTitle        	| text       	|
| Authors          	| text array 	|
| Subjects         	| text array 	|
| Description      	| text       	|
| FirstPublishDate 	| text       	|
| Editions         	| text array 	|
| OtherTitles      	| text array 	|
| TranslatedTitles 	| text array 	|
| WorkID           	| serial     	|
