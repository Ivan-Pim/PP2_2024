movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

### end of dictionary


def over_average(a):
    if isinstance(a, int):
        return (movies[a]['imdb'] > 5.5)
    elif isinstance(a, str):
        for i in movies:
            if i['name'] == a:
                return (i['imdb'] > 5.5)
        print("Sorry, i couldn't find this film")
    else:
        print("Sorry, that doesn't specify a movie")
    return False


def all_over_average():
    result = [m['name'] for m in movies if m['imdb'] > 5.5]
    return result


def filter_category(cat):
    result = [m['name'] for m in movies if m['category'] == cat]
    return result

def average_score(mvs):
    result = 0
    for mv in mvs:
        result += mv['imdb']
    result /= len(mvs)
    return result

def average_score_by_category(cat):
    result = 0
    cnt = 0
    for mv in movies:
        if mv['category'] == cat:
            result += mv['imdb']
            cnt += 1
    return (result / cnt)

search_query = input()
print(over_average(search_query))

print("Here are all movies with over average score:")
print(all_over_average())

category = input()
filtered = filter_category(category)
if len(filtered) != 0:
    print(filtered)

print(average_score(movies))

print(average_score_by_category(input()))